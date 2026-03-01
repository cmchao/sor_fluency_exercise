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

---

# Real Word Detection Feature

## Status: COMPLETED

## Task
Check if each generated word is a real English word and highlight/mark real words differently from nonsense words.

## Approach
Embed a list of English words as a JavaScript `Set` for O(1) lookup. Works offline (file:// protocol) with no external dependencies.

## Word List Generation
Used `generate_wordlist.py` to:
1. Generate all 11,880 possible combinations from head/vowel/tail data
2. Check each against `/usr/share/dict/words` (75,145 words)
3. Found 1,218 real English words

## Changes Made to `index.html`

### 1. CSS styles for real word highlighting
```css
.real-word-marker {
    text-decoration: underline;
    text-decoration-color: #4CAF50;
    text-decoration-thickness: 3px;
    text-underline-offset: 4px;
}
```

### 2. Print styles (in @media print)
```css
.real-word-marker {
    text-decoration: underline !important;
    text-decoration-color: #4CAF50 !important;
    text-decoration-thickness: 3px !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}
```

### 3. UI toggle in Extra options section
```html
<div class="option-group color-option">
    <label>
        <input type="checkbox" id="highlight-real-words">
        Mark <span style="color: #4CAF50; text-decoration: underline;">real words</span>
    </label>
</div>
```

### 4. Word list and detection function
- `realWords` - Set containing 1,218 dictionary-verified words
- `isRealWord(word)` - Returns true if word is in the Set

### 5. Modified `generateWord()` function
Added `isReal` property to the returned word object:
```javascript
wordObj.isReal = isRealWord(wordObj.full);
```

### 6. Modified `formatWord()` function
Wraps output in marker span if word is real and option is enabled:
```javascript
if (highlightRealWords && wordObj.isReal) {
    html = `<span class="real-word-marker">${html}</span>`;
}
```

## Files
- `index.html` - Main application with real word detection
- `generate_wordlist.py` - Utility script to regenerate word list from dictionary

## Verification
1. Check "Mark real words" option in Extra section
2. Generate words - real words have green underline
3. Print/PDF - verify underline appears
4. Words like "bat", "bind", "dog" are marked; nonsense words are not

---

# UI Enhancements

## Status: COMPLETED

## Changes Made

### 1. Title Rename
Changed from "SOR Spelling Exercise Generator" to "Taiwan SOR Fluency Exercise Generator"

### 2. Statistics Bar Charts
Replaced text-based statistics chips with horizontal bar charts:
- Each bar's width is proportional to max count in category
- Labels on left, bars in middle, count/percentage on right
- Light blue (#87CEEB) for consonants, red (#C41E3A) for vowels

### 3. Header Fields (Author & Tutor)
Added optional fields in output header row:
- "Show Author field" checkbox - adds Author: with fill-in line
- "Show Tutor field" checkbox - adds Tutor: with fill-in line
- Fields appear left-aligned in same row as Score (right-aligned)
- Score label aligns with score column grid

### 4. Fixed Acknowledgements Section
Added always-visible acknowledgements block at bottom of page:
- Fixed position, not affected by scrolling
- Styled to match other sections (white background, rounded corners, shadow)
- Credits Wen Hsiao and Taiwan SOR team with links to:
  - facebook.com/wen.hsiao.100
  - milinguall.com
  - milinguall.org

### 5. Label Updates
- "Elements per group" → "Words per group"

## Files Modified
- `index.html` - All UI changes

## Verification
1. Title displays "Taiwan SOR Fluency Exercise Generator"
2. Statistics section shows bar charts after generation
3. Author/Tutor checkboxes add header fields when enabled
4. Acknowledgements block fixed at bottom, always visible
5. All features print correctly
