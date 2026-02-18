# File Reorganization Guide

To complete the professional setup of this repository, please perform the following file moves:

## Required File Operations

### 1. Move Notebook to notebooks/ folder
```bash
mv cpsc-572-facebook-ego-network-analysis.ipynb notebooks/facebook-ego-network-analysis.ipynb
```

### 2. Move Report to docs/ folder
```bash
mv Report.md docs/technical-report.md
```

### 3. Move Visualizations to visualizations/ folder
```bash
mv data/*.png visualizations/
```
This will move:
- day1_results.png
- day2_results.png
- day3_results.png
- part1_results.png
- part2_results.png

### 4. Optional: Clean up Archive folder
```bash
# Either delete if not needed:
rm -rf Archive/

# Or keep but add a README:
echo "# Archive\n\nPrevious versions of the project for reference." > Archive/README.md
```

## Final Directory Structure

After completing these moves, your project should look like:

```
Facebook-Ego-Network-Analysis-for-Political-Outreach-Optimization/
├── README.md                          # Main project documentation
├── CONTRIBUTING.md                    # Contribution guidelines
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
├── notebooks/
│   └── facebook-ego-network-analysis.ipynb  # Main analysis notebook
├── data/
│   ├── facebook_combined.txt          # Combined network data
│   ├── *.edges                        # Edge lists
│   ├── *.circles                      # Social circles
│   ├── *.feat                         # Node features
│   ├── *.featnames                    # Feature names
│   └── network_communities.html       # Interactive visualization
├── visualizations/
│   ├── day1_results.png               # Analysis results
│   ├── day2_results.png
│   ├── day3_results.png
│   ├── part1_results.png
│   └── part2_results.png
├── docs/
│   ├── README.md                      # Documentation index
│   └── technical-report.md            # Detailed technical report
└── Archive/                           # Optional: Previous versions
    └── cpsc572project.ipynb
```

## Verification

After running these commands, verify the changes:
```bash
# Check notebook location
ls notebooks/

# Check docs location
ls docs/

# Check visualizations
ls visualizations/

# Verify data folder still has data files
ls data/*.edges
```

## Git Commands

After reorganizing, commit the changes:
```bash
git add .
git commit -m "Reorganize project structure for professional presentation"
git push origin main
```

## Alternative: Using Git MV

If you want to preserve file history in git, use `git mv` instead:
```bash
git mv cpsc-572-facebook-ego-network-analysis.ipynb notebooks/facebook-ego-network-analysis.ipynb
git mv Report.md docs/technical-report.md
# Note: For *.png files, you'll need to move them individually with git mv
```
