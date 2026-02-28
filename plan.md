# SOR Spelling Test Generator - Implementation Plan

## Overview
Single-page web application that generates CVC (Consonant-Vowel-Consonant) spelling exercises for Science of Reading.

## Tech Stack
- **HTML5** - Structure
- **CSS3** - Styling (no framework, keep simple)
- **Vanilla JavaScript** - Logic (no dependencies for easy browser compatibility)
- Single `index.html` file with embedded CSS/JS for portability

## Data Structure (3 levels: Category → Group → Sub-group)

### Head Consonants
| Group | Sub-group | Elements |
|-------|-----------|----------|
| 140 | 1 | b, p, m, n |
| 140 | 2 | d, t, n, l |
| 140 | 3 | g, k, h |
| 140 | 4 | s, th, r |
| 280 | 1 | dr, tr, br, pr |
| 280 | 2 | bl, pl, kl, sl |
| 280 | 3 | sm, sn, sp, st, sg, str |

### Vowels
| Group | Sub-group | Elements |
|-------|-----------|----------|
| Basic | 1 | e, ai, a, ou |
| Basic | 2 | i, oo, oa |
| Basic | 3 | o, er, ar |
| 8800 | 1 | a, e, i, o, u |
| 8800 | 2 | a_e, e_e, i_e, o_e, u_e |
| 8800 | 3 | ar, er, ir, or, ur |
| 8800 | 4 | ee, oo, ou, oi, air |

### Tail Consonants (no level 2 sub-groups)
| Group | Elements |
|-------|----------|
| Single | s, ss, b, p, d, t, g, ck, st, sp |
| Nose | m, mb, mp, n, nd, nt |
| Extra | ph, ch, sh, th |

## Word Generation Logic

### Standard Pattern
`head + vowel + tail` → "bat" (b + a + t)

### Magic-e Pattern (vowel contains "_")
The `_` indicates where tail consonant inserts:
- `b + i_e + nt` → `b + i + nt + e` → "binte"
- `p + a_e + k` → `p + a + k + e` → "pake"

## UI Layout

```
┌─────────────────────────────────────────────────────────┐
│  SOR Spelling Exercise Generator                        │
├─────────────────────────────────────────────────────────┤
│  HEAD CONSONANTS (light blue)                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │ [✓] 140                                         │   │
│  │     [✓] Sub-1  ☐b ☐p ☐m ☐n                     │   │
│  │     [✓] Sub-2  ☐d ☐t ☐n ☐l                     │   │
│  │     [✓] Sub-3  ☐g ☐k ☐h                        │   │
│  │     [✓] Sub-4  ☐s ☐th ☐r                       │   │
│  │ [✓] 280                                         │   │
│  │     [✓] Sub-1  ☐dr ☐tr ☐br ☐pr                 │   │
│  │     [✓] Sub-2  ☐bl ☐pl ☐kl ☐sl                 │   │
│  │     [✓] Sub-3  ☐sm ☐sn ☐sp ☐st ☐sg ☐str       │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  VOWELS (red)                                          │
│  ┌─────────────────────────────────────────────────┐   │
│  │ [✓] Basic                                       │   │
│  │     [✓] Sub-1  ☐e ☐ai ☐a ☐ou                   │   │
│  │     [✓] Sub-2  ☐i ☐oo ☐oa                      │   │
│  │     [✓] Sub-3  ☐o ☐er ☐ar                      │   │
│  │ [✓] 8800                                        │   │
│  │     [✓] Sub-1  ☐a ☐e ☐i ☐o ☐u                  │   │
│  │     [✓] Sub-2  ☐a_e ☐e_e ☐i_e ☐o_e ☐u_e        │   │
│  │     [✓] Sub-3  ☐ar ☐er ☐ir ☐or ☐ur             │   │
│  │     [✓] Sub-4  ☐ee ☐oo ☐ou ☐oi ☐air            │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  TAIL CONSONANTS (light blue)                          │
│  ┌─────────────────────────────────────────────────┐   │
│  │ [✓] Single   ☐s ☐ss ☐b ☐p ☐d ☐t ☐g ☐ck ☐st ☐sp│   │
│  │ [✓] Nose     ☐m ☐mb ☐mp ☐n ☐nd ☐nt             │   │
│  │ [✓] Extra    ☐ph ☐ch ☐sh ☐th                   │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  OPTIONS                                                │
│  Elements per group: [3 ▼]                             │
│  Number of groups:   [5 ▼]                             │
│                                                         │
│  [ Generate ]  [ Print/PDF ]                            │
├─────────────────────────────────────────────────────────┤
│  OUTPUT                                                 │
│  1. brike, tam, soat                                   │
│  2. plam, dike, foop                                   │
│  3. ...                                                │
└─────────────────────────────────────────────────────────┘
```

## Implementation Steps

### Step 1: Create HTML structure
- File: `index.html`
- Three selection sections (head, vowel, tail)
- Options section
- Generate button
- Output area

### Step 2: Add CSS styling
- Embedded in `<style>` tag
- Light blue for consonants (#87CEEB or similar)
- Red for vowels (#DC143C or similar)
- Checkbox styling
- Responsive layout

### Step 3: Implement JavaScript logic
- Data structure with 3 levels: Category → Group → Sub-group
- Render checkboxes dynamically with nested indentation
- 3-level select/unselect functionality:
  - Group checkbox: toggles all sub-groups and elements within
  - Sub-group checkbox: toggles all elements within
  - Element checkbox: individual toggle
- Word generation algorithm (handles `_` pattern)
- Random selection from checked elements
- Random grouping (words don't need to rhyme)

## Output Files
- `index.html` - Single file containing all HTML, CSS, and JavaScript

## Print/PDF Support
- Add print button that triggers `window.print()`
- CSS `@media print` styles for clean PDF output
- Hide UI controls (checkboxes, buttons) when printing
- Show only the generated word groups
- Clean typography for worksheet format

## Verification
1. Open `index.html` in Chrome
2. Open `index.html` in Edge
3. Test: Select some elements from each section, click Generate
4. Verify magic-e pattern works (select a_e, i_e etc.)
5. Verify group/ungroup selection works
6. Verify color coding (consonants blue, vowels red)
7. Click Print/PDF button, verify clean output (controls hidden)
8. Save as PDF, verify formatting
