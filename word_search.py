# Solution 02242019
# Word Search exercise from Exercism\python\word-search
# Words can be hidden in all kinds of directions: left-to-right, right-to-left, vertical and diagonal.
# Given a puzzle and a list of words return the location of the first and last letter of each word.

# Strategy taken is to identify lines (connections between two points) which have a valid start letter,
# stop letter, orientation, length then evaluate if they have the correct word.

class Point(object):
# Contains two 2d coordinates and information around x/y equality.

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.y == other.x and self.x == other.y

class Line(object):
# Contains two points and functions/variables assessing a line's length and orientation.
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.orientation_test()

    # Determine if line follows one of 8 2D directions
    def orientation_test(self):
        xd = self.end.x - self.start.x
        yd = self.end.y - self.start.y
        self.d = [xd,yd]
        self.orientation = xd == 0 or yd == 0 or abs(xd) == abs(yd)

    # Determine if line is the correct length
    def test_length(self, length):
        if self.orientation:
            return length == max([abs(self.d[0]), abs(self.d[1])])
        return False

    # Setup Unit Direction of a Line
    def unit_movement(self):
        u = [0,0]
        u[0] = self.unit_sign(self.d[0])
        u[1] = self.unit_sign(self.d[1])
        return u

    # Quick unit direction calculation for 8 2D coordinates
    def unit_sign(self, value):
        if value > 0:
            return 1
        elif value < 0:
            return -1
        return 0


class WordSearch(object):
# Identifies matching words in a puzzle using points and lines.

    def __init__(self, puzzle):
        self.puzzle = [list(i) for i in puzzle]

    # Identify every instance where a letter is found.
    def get_points(self, letter):
        return [Point(row,col) for row, val in enumerate(self.puzzle) for col, i in enumerate(val) if i == letter]

    # Searches for words following a line.
    def search(self, word):
        potential_start = self.get_points(word[:1])
        potential_end = self.get_points(word[-1])
        word_length = len(word)-1

        # Creates lines - could improve with initial filter prior to making line. Since this scales O(N^2)
        lines = [Line(s,e) for s in potential_start for e in potential_end]

        # Filters lines first based on orientation then based on length.
        matches = [line for line in lines if line.test_length(word_length)]

        # Identify correct sequence
        for line in matches:
            u = line.unit_movement()
            if ''.join([self.puzzle[line.start.x+i*u[0]][line.start.y+i*u[1]] for i in range(len(word))]) == word:
                return line.start, line.end