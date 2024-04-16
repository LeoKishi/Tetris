

class Points:
    lines = 0
    level = 0
    score = 0


    def search_completed_lines(self, array: list[list[int]]) -> list[int]:
        '''Returns a list with the indices of all completed horizontal lines'''
        completed_lines = []

        for i, line in enumerate(array):
            values_in_line = {val[0] for val in line}
            if values_in_line == {2}:
                completed_lines.append(i)

        return completed_lines


    def clear_and_collapse(self, array: list[list[int]], completed_lines: list[int]):
        '''Clears the line and drops the line above.'''
        for i in completed_lines:
            array.pop(i)
            array.insert(0, [[0, ' '] for width in range(10)])


    def get_points(self, completed_lines: list[int]):
        '''Returns the amount of points earned for the completed lines.'''
        one_line = 40 * (self.level+1)
        two_lines = (one_line*2) + int(one_line/2)
        three_lines = two_lines * 3
        four_lines = three_lines * 4

        line_count = len(completed_lines)

        self.lines += line_count
        self.level = self.lines//10

        if line_count == 1:
            return one_line
        elif line_count == 2:
            return two_lines
        elif line_count == 3:
            return three_lines
        else:
            return four_lines




if __name__ == '__main__':







    ...