# Word Search in Python
#### This is word search exercise from the Python track of exercism.io.  Goal was to make a python script to find words hidden in a crossword puzzle in any linear orientation.  Right now implementation first finds all letters that have the same start and stop as a word, then assesses orientation/length then assesses content.  Liekly would need to optimize by removing the O(N^2) scaling where N is the number of start stop letters found.
#### Implementation code is in word_search.py
#### Example tests from exercism where showing input and output as first and second parameters into assertEqual.
```
    def setUpClass(cls):
        puzzle = ['jefblpepre',
                  'camdcimgtc',
                  'oivokprjsm',
                  'pbwasqroua',
                  'rixilelhrs',
                  'wolcqlirpc',
                  'screeaumgr',
                  'alxhpburyi',
                  'jalaycalmp',
                  'clojurermt']
        cls.example = WordSearch(puzzle)

    def test_diagonal_upper_bottom_right_to_top_left(self):
        self.assertEqual(
            self.example.search('lua'),
            (Point(7, 8), Point(5, 6))
        )

```