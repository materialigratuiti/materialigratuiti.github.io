# Story Pages Word Search (interactive page)

Two files, nothing to build:

- `index.html` is the page (English). Do not edit it to change puzzles.
- `puzzles.js` holds the puzzles. **The file here has 3 SAMPLE puzzles.** Replace it with the real puzzles of the book.

## puzzles.js format

```js
window.PUZZLES = [
  {
    "title": "The Front Porch",                       // theme shown above the grid
    "prompt": "Who sat with you on the porch?",       // the Story Page question
    "grid": ["OOMZSCREEN", "ORAILINGOD", ...],        // one string per row, all rows the same length
    "words": ["PORCH", "ROCKER", ...]                 // the page finds each word in the grid by itself
  },
  ...
];
```

- Any number of puzzles (the book has 60) and any grid size: letters scale with the grid.
- `words` can also be `{ "w": "PORCH", "s": [row, col], "e": [row, col] }` (0-based) if a word must be placed exactly.
- Open the browser console: the page warns if a word is missing from the grid or appears more than once.
- Progress, name and story texts are saved in the visitor's browser (localStorage), nothing is sent anywhere.
