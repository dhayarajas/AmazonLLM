# 📝 Manual Guide: Remove Author Papers

## ⚠️ Important Note

The automated script had issues. This manual guide is SAFER and gives you full control.

---

## 🎯 Task

Remove all papers by:
- **M. Nasir** (3 papers: ref5, ref31, ref34)
- **D.-N. Nguyen** (2 papers: ref16, ref38)
- **S. G. K. Patro** (2 papers: ref28, ref36)

**Total to remove:** 7 references

---

## ✅ Step-by-Step Instructions

### Step 1: Open Your LaTeX File

```bash
# Open in your editor
code Amazon_review.tex
# or
vim Amazon_review.tex
# or use any text editor
```

### Step 2: Remove Bibliography Entries

**Find and DELETE these 7 entries from the bibliography section:**

1. **Search for:** `\bibitem{ref5}`
   - Delete the entire entry (2 lines):
   ```latex
   \bibitem{ref5} M. Nasir and C. I. J. S. C. S. Ezeife, ``A survey and taxonomy of sequential recommender systems for e-commerce product recommendation,'' \textit{J SN Computer Science}, vol. 4, no. 6, p. 708, 2023.
   
   ```

2. **Search for:** `\bibitem{ref16}`
   - Delete the entire entry (2 lines):
   ```latex
   \bibitem{ref16} D.-N. Nguyen, V.-H. Nguyen, T. Trinh, T. Ho, H.-S. J. J. o. O. I. T. Le, Market,, and Complexity, ``A personalized product recommendation model in e-commerce based on retrieval strategy,'' \textit{Journal of Open Innovation: Technology, Market, Complexity}, vol. 10, no. 2, p. 100303, 2024.
   
   ```

3. **Search for:** `\bibitem{ref28}`
   - Delete the entire entry (2 lines):
   ```latex
   \bibitem{ref28} S. G. K. Patro \textit{et al.}, ``A hybrid action-related K-nearest neighbour (HAR-KNN) approach for recommendation systems,'' \textit{IEEE Access}, vol. 8, pp. 90978-90991, 2020.
   
   ```

4. **Search for:** `\bibitem{ref31}`
   - Delete the entire entry (2 lines):
   ```latex
   \bibitem{ref31} M. Nasir, C. I. Ezeife, A. J. S. N. A. Gidado, and Mining, ``Improving e-commerce product recommendation using semantic context and sequential historical purchases,'' \textit{Social Network Analysis Mining}, vol. 11, no. 1, p. 82, 2021.
   
   ```

5. **Search for:** `\bibitem{ref34}`
   - Delete the entire entry (2 lines):
   ```latex
   \bibitem{ref34} M. Nasir, C. I. J. I. J. o. D. S. Ezeife, and Analytics, ``Semantic enhanced Markov model for sequential E-commerce product recommendation,'' \textit{International Journal of Data Science Analytics}, vol. 15, no. 1, pp. 67-91, 2023.
   
   ```

6. **Search for:** `\bibitem{ref36}`
   - Delete the entire entry (2 lines):
   ```latex
   \bibitem{ref36} S. G. K. Patro, B. K. Mishra, S. K. Panda, R. Kumar, H. V. Long, and D. J. S. C. Taniar, ``Cold start aware hybrid recommender system approach for E-commerce users,'' \textit{Soft Computing}, vol. 27, no. 4, pp. 2071-2091, 2023.
   
   ```

7. **Search for:** `\bibitem{ref38}`
   - Delete the entire entry (2 lines):
   ```latex
   \bibitem{ref38} D.-N. Nguyen, V.-H. Nguyen, T. Trinh, T. Ho, and H.-S. J. Le, ``A personalized product recommendation model in e-commerce based on retrieval strategy,'' \textit{Journal of Open Innovation: Technology, Market, Complexity} vol. 10, no. 2, p. 100303, 2024.
   
   ```

### Step 3: Remove Citations from Text

**Search for and DELETE these citations from the text:**

Use Find function (Cmd/Ctrl + F) to find and delete:

1. `~\cite{ref5}` - DELETE this text (appears in Introduction)
2. `~\cite{ref16}` - DELETE this text (appears in Introduction)
3. `~\cite{ref28}` - DELETE this text (appears in Literature Review)
4. `~\cite{ref31}` - DELETE this text (appears in Literature Review)
5. `~\cite{ref34}` - DELETE this text (appears in Literature Review AND Problem ID)
6. `~\cite{ref36}` - DELETE this text (appears in Literature Review)
7. `~\cite{ref38}` - DELETE this text (appears in Literature Review)

**Note:** Some may appear twice (ref34 is cited in two places) - delete ALL occurrences.

### Step 4: Clean Up Spacing

After deleting citations, you may have:
- Double spaces: `word  word` → change to `word word`
- Space before punctuation: `word .` → change to `word.`

Use Find & Replace:
- Find: `  ` (two spaces) → Replace: ` ` (one space)
- Repeat until no more double spaces

---

## ⚠️ DO NOT RENUMBER

**Important:** Do NOT renumber the remaining references yet. Leave them as is:
- ref1-ref4 stay the same
- ref6-ref15 stay the same (skip deleted ref5)
- ref17-ref27 stay the same (skip deleted ref16)
- etc.

LaTeX will handle the numbering automatically!

---

## 🔄 Alternative: Use Latexdiff

If manual deletion is too tedious, you can use a reference management approach:

### Option A: Comment Out Instead of Delete

Instead of deleting, comment out the bibliography entries and citations:

```latex
% \bibitem{ref5} M. Nasir ...
% \cite{ref5}
```

This preserves the structure and you can easily restore if needed.

### Option B: Use Bibliography Management Tools

If you're comfortable with BibTeX:
1. Convert to .bib format
2. Remove entries there
3. Let BibTeX handle numbering

---

## ✅ After Manual Deletion

### Step 5: Compile LaTeX

```bash
cd "/Users/dhaya/PhD/Learnings/Amazon-LLM"
pdflatex Amazon_review.tex
pdflatex Amazon_review.tex  # Run twice
```

### Step 6: Check Output

- PDF should compile successfully
- References should show as [?] or warnings for deleted citations
- Page count should be reduced

---

## 📊 Expected Result

After manual deletion:
- **Bibliography:** 45 entries (from 52)
- **Removed:** ref5, ref16, ref28, ref31, ref34, ref36, ref38
- **Remaining:** All others (with gaps in numbering - this is OK!)

---

## ⚠️ Why Manual is Better

1. **Safe:** You see exactly what you're deleting
2. **Control:** You decide what to keep/remove
3. **No bugs:** No automated script errors
4. **Reversible:** Easy to undo (Cmd/Ctrl + Z)
5. **Transparent:** You understand every change

---

## 🚨 If You Make a Mistake

### Restore from backup:
```bash
cp Amazon_review_backup_before_removal.tex Amazon_review.tex
```

---

## 💡 Pro Tip: Use Version Control

Before making changes:
```bash
git add Amazon_review.tex
git commit -m "Before removing author papers"
# Make changes
git diff  # Review changes
git commit -m "Removed M. Nasir, D.-N. Nguyen, S. G. K. Patro papers"
```

---

## ✅ Verification Checklist

After deletion, verify:
- [ ] Deleted all 7 `\bibitem` entries
- [ ] Deleted all citations to those refs
- [ ] Cleaned up double spaces
- [ ] LaTeX compiles without errors
- [ ] Bibliography has 45 entries
- [ ] Page count reduced

---

## 📞 Need Help?

If you encounter issues:
1. Check LaTeX log for errors: `Amazon_review.log`
2. Restore from backup if needed
3. Try commenting out instead of deleting first

---

**Time Required:** 10-15 minutes  
**Difficulty:** Easy (basic find & delete)  
**Risk:** Low (backup exists)  
**Result:** 7 papers removed, ~1 page saved

---

**Status:** Manual guide ready  
**Recommended:** Use this instead of automated script  
**Backup:** Amazon_review_backup_before_removal.tex exists
