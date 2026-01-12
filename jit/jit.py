#!/usr/bin/env python3

import os
import re
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ==========================
# USER SETTINGS
# ==========================
MOTIF_DIR = "motif"
OUT_DIR = "jit_output"
OUT_FIG = "JIT_motif.png"
COLORMAP = "Blues"

# ==========================
# HELPERS
# ==========================
def extract_time(filename):
    """
    Extract numeric time from filename.
    Example: Motif_15min.xls -> 15
    """
    m = re.search(r"(\d+)", filename)
    if not m:
        raise ValueError(f"No time found in filename: {filename}")
    return int(m.group(1))


def wait_for_files():
    if not os.path.exists(MOTIF_DIR):
        os.makedirs(MOTIF_DIR)
        print(f"📂 Created folder: {MOTIF_DIR}/")

    print(f"\n➡️ Put motif files into '{MOTIF_DIR}/'")
    print("➡️ Filenames must contain time (e.g. Motif_15min.xls)")
    input("⏳ Press ENTER when ready ")

    files = os.listdir(MOTIF_DIR)
    if not files:
        sys.exit("❌ No files found. Exiting.")


def infer_timepoints():
    """
    Infer and sort timepoints from motif filenames.
    """
    times = []
    for f in os.listdir(MOTIF_DIR):
        if f.lower().endswith((".xls", ".txt", ".tsv")):
            times.append(extract_time(f))

    if not times:
        sys.exit("❌ No valid motif files with timepoints detected.")

    return sorted(set(times))


# ==========================
# LOAD DATA
# ==========================
def load_motif_tables(timepoints):
    motif_tables = {}

    for f in os.listdir(MOTIF_DIR):
        if not f.lower().endswith((".xls", ".txt", ".tsv")):
            continue

        t = extract_time(f)
        df = pd.read_csv(os.path.join(MOTIF_DIR, f), sep="\t")

        # Keep strongest motif signal
        tmp = df.groupby("Class")["PValue"].min().reset_index()
        tmp[str(t)] = -np.log10(tmp["PValue"])
        motif_tables[t] = tmp[["Class", str(t)]]

    # Merge tables in inferred time order
    jit = motif_tables[timepoints[0]]
    for t in timepoints[1:]:
        jit = jit.merge(motif_tables[t], on="Class", how="outer")

    jit = jit.fillna(0)
    return jit


# ==========================
# JIT COMPUTATION
# ==========================
def compute_jit(jit, timepoints):
    time_cols = [str(t) for t in timepoints]

    # JIT definition
    jit["JIT_time"] = jit[time_cols].idxmax(axis=1)
    jit["peak_val"] = jit[time_cols].max(axis=1)
    jit["JIT_time_num"] = jit["JIT_time"].astype(int)

    # Sort = temporal cascade
    jit = jit.sort_values(
        by=["JIT_time_num", "peak_val"],
        ascending=[True, False]
    ).reset_index(drop=True)

    return jit, time_cols


# ==========================
# PLOTTING
# ==========================
def plot_jit(jit, time_cols):
    os.makedirs(OUT_DIR, exist_ok=True)

    fig, ax = plt.subplots(
        figsize=(0.5 * len(time_cols), 0.3 * len(jit))
    )

    data = jit[time_cols].values
    im = ax.imshow(data, aspect="auto", cmap=COLORMAP)

    ax.set_xticks(range(len(time_cols)))
    ax.set_xticklabels([f"{t} min" for t in time_cols], rotation=45)
    ax.set_yticks(range(len(jit)))
    ax.set_yticklabels(jit["Class"])

    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label(r"$-\log_{10}$(P-value)")

    # Draw red box at JIT time
    for i, row in jit.iterrows():
        col = time_cols.index(row["JIT_time"])
        ax.add_patch(Rectangle(
            (col - 0.5, i - 0.5),
            1, 1,
            fill=False,
            edgecolor="red",
            linewidth=2
        ))

    ax.set_title("Just-in-Time Cis-element Cascade")
    plt.tight_layout()

    out_path = os.path.join(OUT_DIR, OUT_FIG)
    plt.savefig(out_path, dpi=600)
    plt.show()

    print(f"📁 Plot saved to: {out_path}")


# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    print("🚀 Running JIT analysis (auto time inference)")

    wait_for_files()

    TIMEPOINTS = infer_timepoints()
    print("⏱ Detected timepoints:", TIMEPOINTS)

    jit = load_motif_tables(TIMEPOINTS)
    jit, time_cols = compute_jit(jit, TIMEPOINTS)

    plot_jit(jit, time_cols)

    print("✅ DONE")

