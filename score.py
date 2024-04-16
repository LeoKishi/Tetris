

class Score:
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







if __name__ == '__main__':








    ...