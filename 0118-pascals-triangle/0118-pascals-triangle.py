class Solution:
    def generate_row(self, rowIndex: int) -> List[int]:
        row = [1]  
        for i in range(1, rowIndex + 1):
            next_val = row[i - 1] * (rowIndex - i + 1) // i
            row.append(next_val)
        return row

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            triangle.append(self.generate_row(i))
        return triangle