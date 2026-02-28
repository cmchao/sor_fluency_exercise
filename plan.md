# SOR Spelling Test Generator - Fix Plan

## Status: COMPLETED

## Problem
The original `index.html` had rich features that were accidentally removed. Need to restore them while keeping the new 3-level data structure.

## Original Options (to restore)

### Num of test
- **Elements per group:** number input (default: 3, min: 1)
- **Number of groups:** dropdown (3, 5, 8, 10, 15, 20) - default: 5

### Format
- **Consonants in light blue:** checkbox (default: checked)
- **Vowels in red:** checkbox (default: checked)
- **Show score column:** checkbox (default: unchecked)
- **Font size:** dropdown - Small (16pt), Medium (24pt), Large (32pt), Extra Large (48pt) - default: Medium
- **Font style:** dropdown - Serif, Sans-serif, Monospace, Cursive - default: Serif

### Print
- **Page orientation:** dropdown - Landscape, Portrait - default: Landscape

### Extra
- **Seed:** number input (default: 1, min: 1) - for reproducible random generation

### Buttons
- **Generate** button
- **Print / PDF** button (calls `printPage()` function)

### Other Features
- **Statistics section:** shows distribution of head/vowel/tail elements used
- **Grid-based output:** words displayed in columns with colored parts
- **Seeded RNG:** Mulberry32 algorithm for reproducible results

## Word Generation Algorithm

Generate words with uniform distribution across all selected elements:

```
a. Generate all possible combinations (head x vowel x tail)
b. Shuffle the combinations 20 times
c. Pick sequentially from index 0 to end
d. When pool exhausted, repeat steps a-c until enough words generated
```

This ensures every combination has equal probability before any repeats occur.

## What to Restore

### 1. Restore original index.html from git
```bash
git checkout HEAD -- index.html
```

### 2. Update data structure to use 3-level hierarchy
Change from 2-level (category -> subgroup) to 3-level (category -> group -> sub-group):

**Head Consonants:**
- 140: Sub-1 (b,p,m,n), Sub-2 (d,t,n,l), Sub-3 (g,k,h), Sub-4 (s,th,r)
- 280: Sub-1 (dr,tr,br,pr), Sub-2 (bl,pl,kl,sl), Sub-3 (sm,sn,sp,st,sg,str)

**Vowels:**
- Basic: Sub-1 (e,ai,a,ou), Sub-2 (i,oo,oa), Sub-3 (o,er,ar)
- 8800: Sub-1 (a,e,i,o,u), Sub-2 (a_e,e_e,i_e,o_e,u_e), Sub-3 (ar,er,ir,or,ur), Sub-4 (ee,oo,ou,oi,air)

**Tail Consonants:** (keep flat - no sub-groups)
- Single, Nose, Extra groups

### 3. Update rendering functions
- Add `renderNestedCategory()` for head/vowels with group -> sub-group hierarchy
- Keep `renderFlatCategory()` for tail consonants
- Update toggle functions for 3-level checkbox behavior

## Files to Modify
- `index.html` - restore from git, then update data structure and rendering

## Verification
1. All original options visible (color toggles, font size/style, seed, score column, page orientation)
2. Print/PDF button works
3. 3-level checkbox hierarchy works (group -> sub-group -> elements)
4. Statistics section appears after generation
