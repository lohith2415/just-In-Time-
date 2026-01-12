## Research Article Plant Biology

# Temporal transcriptional logic of dynamic regulatory networks underlying nitrogen signaling and use in plants

https://doi.org/10.1073/pnas.1721487115

# 🧬 Just-in-Time (JIT) Motif Cascade Analysis

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

# 📥 Input Requirements

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

# ⚙️ Workflow Overview
## 1️⃣ Automatic Timepoint Detection

The script extracts numeric time values directly from 

filenames (e.g. 15, 30, 60) and sorts them chronologically.

## 2️⃣ Motif Signal Processing
For each time point:

Motifs are grouped by Class

The minimum P-value per motif is retained

Signal strength is converted to
–log₁₀(P-value)

## 3️⃣ JIT Time Computation

For each motif:

The time point with the maximum signal is assigned as its JIT time

Motifs are ordered to reveal a temporal regulatory cascade

Early motifs first

Stronger motifs ranked higher within each time

## 4️⃣ Visualization

A heatmap is generated where:
Rows = motifs

Columns = time points

Color intensity = –log₁₀(P-value)

Red boxes mark each motif’s JIT time
Output file:
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
# Example (sample)
Before running the pipeline 
<img width="572" height="369" alt="Screenshot from 2026-01-12 17-00-42" src="https://github.com/user-attachments/assets/f26553bf-01d7-4966-ba1f-c83a0001c1cd" />

# Motif files arrangement 
Files should be named as per their timeline 
<img width="1676" height="578" alt="Screenshot from 2026-01-12 17-03-23" src="https://github.com/user-attachments/assets/745b2482-642c-4248-af25-18a305e12f94" />

# After pipeline (plot)
<img width="1676" height="578" alt="Screenshot from 2026-01-12 17-04-39" src="https://github.com/user-attachments/assets/dc4cd7ca-c1c4-4d05-b861-eae06dfca485" />

Final Just-In-Time plot 

<img width="4800" height="2700" alt="JIT_motif" src="https://github.com/user-attachments/assets/734a5aac-63ed-4533-90b5-807b388d817c" />
