#!/bin/bash

echo "=== Cleaning up and pushing to GitHub ==="
echo ""

# Remove Render deployment files
echo "1. Removing Render-specific files..."
rm -f app.py render.yaml Procfile runtime.txt fix-deployment.sh
rm -f DEPLOYMENT.md DEPLOYMENT_FIX.md TROUBLESHOOTING.md
rm -rf .streamlit
echo "   ✅ Cleaned deployment files"

# Remove coursework materials
echo ""
echo "2. Removing coursework materials..."
rm -rf Guides/
echo "   ✅ Removed Guides folder"

# Stage all changes
echo ""
echo "3. Staging changes..."
git add -A
git status

# Commit
echo ""
echo "4. Committing changes..."
git commit -m "Clean repo: Remove Render files, update docs for GitHub-only deployment"

# Push
echo ""
echo "5. Pushing to GitHub..."
git push origin main

echo ""
echo "=== Done! ==="
echo ""
echo "Your repository is now clean and pushed to:"
echo "https://github.com/aymanmomin/Facebook-Ego-Network-Analysis-for-Political-Outreach-Optimization"
echo ""
echo "✅ All Render deployment files removed"
echo "✅ Documentation updated"
echo "✅ Ready for portfolio presentation"
