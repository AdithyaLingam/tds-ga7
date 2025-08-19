# analysis.py
# Author: Data Scientist
# Contact: 24f1002079@ds.study.iitm.ac.in
# 
# This Marimo notebook demonstrates an interactive data analysis
# with variable dependencies and dynamic outputs.

import marimo as mo

# Cell 1: Define dataset parameters
# This cell creates a slider widget that controls the number of samples.
num_samples = mo.ui.slider(10, 500, 100, label="Number of Samples")

# Cell 2: Generate synthetic dataset
# This cell depends on num_samples.value from Cell 1
import numpy as np
x = np.linspace(0, 10, num_samples.value)
y = np.sin(x) + np.random.normal(0, 0.1, num_samples.value)

# Cell 3: Compute summary statistics
# Depends on x and y from Cell 2
mean_y = np.mean(y)
std_y = np.std(y)

# Cell 4: Dynamic Markdown output
# Shows stats and updates automatically when slider changes
mo.md(f"""
### 📊 Data Analysis Report
- Samples: **{num_samples.value}**
- Mean of y: **{mean_y:.3f}**
- Std. deviation of y: **{std_y:.3f}**
""")

# Cell 5: Visualization
# Interactive plot that depends on x, y
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x, y, label="y = sin(x) + noise")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
mo.mpl(fig)
