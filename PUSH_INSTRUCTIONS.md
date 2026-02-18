# Clean Repository & Push to GitHub

Run this to clean up and push everything to GitHub:

```bash
chmod +x push-to-github.sh
./push-to-github.sh
```

## What it does:

1. ✅ Removes all Render deployment files (app.py, render.yaml, etc.)
2. ✅ Removes deployment troubleshooting docs
3. ✅ Removes coursework materials (Guides folder)
4. ✅ Commits all changes
5.✅ Pushes to GitHub

## Or do it manually:

```bash
# Remove render files
rm -f app.py render.yaml Procfile runtime.txt fix-deployment.sh .streamlit/config.toml
rm -f DEPLOYMENT.md DEPLOYMENT_FIX.md TROUBLESHOOTING.md
rm -rf .streamlit Guides/

# Add and commit
git add -A
git commit -m "Clean repo: Remove Render files, update for GitHub portfolio"
git push origin main
```

## Your Resume One-Liner:

```
Facebook Ego Network Analysis for Political Outreach Optimization | 
GitHub: github.com/aymanmomin/Facebook-Ego-Network-Analysis-for-Political-Outreach-Optimization | 
Python, NetworkX, scikit-learn, pandas, NumPy, matplotlib
```

## What's Included:

✅ **Comprehensive README** - Professional project overview  
✅ **Jupyter Notebook** - Complete analysis with visualizations  
✅ **Technical Report** - Detailed methodology and results  
✅ **Resume Examples** - Ready-to-use bullets and LinkedIn posts  
✅ **Documentation** - Quick start, contributing guidelines, changelog  
✅ **Clean Structure** - No deployment or coursework clutter  

Your repository is portfolio-ready!
