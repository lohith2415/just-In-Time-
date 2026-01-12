## 🧬 Just-in-Time (JIT) Motif Cascade Analysis

This script performs Just-in-Time (JIT) analysis on cis-regulatory motif enrichment results across multiple time points and visualizes the temporal motif activation cascade as a heatmap.
It automatically infers time points from filenames, computes the earliest strongest motif activation, and highlights each motif’s JIT time.

```📁 Directory Structure
project/
├── jit_motif.py
├── motif/                # Input motif enrichment files
│   ├── Motif_15min.xls
│   ├── Motif_30min.xls
│   └── Motif_60min.xls
└── jit_output/
    └── JIT_motif.png
```

## 📥 Input Requirements

Place motif enrichment files in the motif/ folder.
Filename format
```
Motif_<TIME>min.xls
```
Example:
```
Motif_15min.xls
Motif_60min.tsv
```
Required columns inside each file
Class → Motif / cis-element name
PValue → Statistical significance

Files must be tab-separated.

## ⚙️ Workflow Overview
# 1️⃣ Automatic Timepoint Detection

>The script extracts numeric time values directly from filenames (e.g. 15, 30, 60) and sorts them chronologically.

# 2️⃣ Motif Signal Processing
>For each time point:
>Motifs are grouped by Class
>The minimum P-value per motif is retained
>Signal strength is converted to
–log₁₀(P-value)

# 3️⃣ JIT Time Computation

For each motif:
>The time point with the maximum signal is assigned as its JIT time
>Motifs are ordered to reveal a temporal regulatory cascade
>Early motifs first
>Stronger motifs ranked higher within each time

# 4️⃣ Visualization

A heatmap is generated where:
>Rows = motifs
>Columns = time points
>Color intensity = –log₁₀(P-value)
>Red boxes mark each motif’s JIT time
>Output file:
```
jit_output/JIT_motif.png
```
# 🖼 Output

High-resolution (600 DPI) JIT heatmap
Clear visualization of early, intermediate, and late motif activation

## 🚀 How to Run
```
chmod +x ./jit_motif.py
python3 jit_motif.py
```

Follow the prompt and press ENTER after placing files in the motif/ directory.

## 📦 Installation (All Required Tools)
🔹 System Requirements

Python ≥ 3.8

🔹 Install Dependencies
pip install pandas numpy matplotlib


# (Optional but recommended)

pip install --upgrade pip

## 📊 Scientific Use Case
This pipeline is ideal for:
Time-series RNA-seq motif analysis
Stress-response regulatory studies
Cis-element cascade discovery
Regulatory network inference support
