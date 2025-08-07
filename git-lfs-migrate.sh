#!/bin/bash

# 1. CONFIGURATION
SIZE_LIMIT=50 # in MB
TEMP_FILE="large_files.txt"

echo "🔍 Scanning for files larger than $SIZE_LIMIT MB in Git history..."

# 2. FIND LARGE FILES IN HISTORY
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk -v limit="$SIZE_LIMIT" '$1=="blob" && $3 > (limit * 1024 * 1024) {print $4}' | \
  sort | uniq > "$TEMP_FILE"

if [ ! -s "$TEMP_FILE" ]; then
  echo "✅ No files larger than $SIZE_LIMIT MB found in Git history."
  rm "$TEMP_FILE"
  exit 0
fi

echo "⚠️ Large files found:"
cat "$TEMP_FILE"

# 3. TRACK THESE FILES WITH LFS
echo "📦 Migrating these files to Git LFS..."
while IFS= read -r file; do
  git lfs track "$file"
done < "$TEMP_FILE"

# 4. COMMIT THE .gitattributes file
git add .gitattributes
git commit -m "🔄 Track large files with Git LFS"

# 5. REWRITE GIT HISTORY TO REMOVE LARGE FILES
echo "🧹 Rewriting history to remove old blobs..."
git filter-repo --path <(cat "$TEMP_FILE") --invert-paths --force

# 6. CLEAN UP
rm "$TEMP_FILE"

# 7. FINAL MESSAGE
echo "✅ Done. Now push with:"
echo "   git push origin --force"