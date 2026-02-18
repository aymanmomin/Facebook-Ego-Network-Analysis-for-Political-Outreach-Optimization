# Quick Start Guide

Get up and running with Facebook Ego Network Analysis in 5 minutes!

## Prerequisites Check

Ensure you have:
- ✅ Python 3.8 or higher (`python --version`)
- ✅ pip package manager (`pip --version`)
- ✅ Jupyter Notebook or JupyterLab

## Installation (3 steps)

### 1. Clone the Repository
```bash
git clone https://github.com/aymanmomin/Facebook-Ego-Network-Analysis-for-Political-Outreach-Optimization.git
cd Facebook-Ego-Network-Analysis-for-Political-Outreach-Optimization
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- NetworkX (graph analysis)
- pandas & NumPy (data manipulation)
- matplotlib (visualizations)
- python-louvain (community detection)
- scikit-learn (metrics)
- PyVis (interactive visualizations)
- tqdm (progress bars)

### 3. Launch Jupyter
```bash
jupyter notebook
# or
jupyter lab
```

## Running the Analysis

1. **Open the notebook**: 
   - Navigate to `cpsc-572-facebook-ego-network-analysis.ipynb`
   - (Or `notebooks/facebook-ego-network-analysis.ipynb` if reorganized)

2. **Run all cells**: 
   - Click "Kernel" → "Restart & Run All"
   - Or use keyboard shortcut: `Command/Ctrl + Shift + Enter`

3. **View results**:
   - Visualizations appear inline
   - Interactive network graph saved as HTML
   - Metrics printed in output cells

## What You'll See

### Network Statistics
- 333 nodes, 2,519 edges (for ego network 0)
- Clustering coefficient: 0.51
- Average path length: 3.75
- Degree distribution and centrality rankings

### Community Detection
- 13 communities identified with Louvain algorithm
- Comparison with 24 user-defined circles
- Adjusted Rand Index (ARI) analysis

### Influence Simulation
- Threshold model demonstration
- Targeted seeding: **92.2% coverage**
- Random seeding: **25.2% coverage**
- Efficiency comparison charts

## Customization

### Analyze Different Ego Networks
In the notebook, change:
```python
EGO_NODE = "0"  # Try: "107", "1684", "1912", etc.
```

### Adjust Activation Threshold
```python
threshold = 0.20  # Try: 0.15, 0.25, 0.30
```

### Modify Seeding Strategy
```python
seed_size = 0.05  # Top 5% → try 0.10 (10%) or 0.03 (3%)
```

## Troubleshooting

### Import Errors
```bash
# Reinstall specific package
pip install --upgrade networkx
```

### Kernel Issues
- Restart kernel: "Kernel" → "Restart"
- Clear outputs: "Cell" → "All Output" → "Clear"

### Memory Issues (Large Networks)
- Close other applications
- Analyze smaller ego networks first
- Run cells individually instead of "Run All"

## Next Steps

1. **Read the full README**: Understand methodology and applications
2. **Explore docs/technical-report.md**: Dive into detailed analysis
3. **Customize the analysis**: Modify parameters and visualizations
4. **Apply to your data**: Adapt code for your own networks

## Need Help?

- 📖 **Full Documentation**: See [README.md](README.md)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/aymanmomin/Facebook-Ego-Network-Analysis-for-Political-Outreach-Optimization/issues)
- 💬 **Questions**: Open a discussion or issue

## Quick Commands Reference

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook

# View dataset structure
ls data/

# Check Python version
python --version
```

Happy analyzing! 🎉
