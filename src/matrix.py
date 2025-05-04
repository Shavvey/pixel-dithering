class Matrix(list[list[float]]):
    """MxN generic matrix, represented as a 2D list"""

    def __str__(self) -> str:
        """method that will turn the matrix into a string representation"""
        s = "\n"
        for rows in self:
            s = s + "{"  # open matrix brackets, open row
            for cols in rows:
                s = s + f" {cols} "
            s = s + "}\n"  # closing brackets, end row
        return s

    def print(self):
        print(self)  # use `__str__` to print out matrix

    def length(self) -> int:
        # return length based on number of rows
        # (which will be the same as the number of cols)
        return len(self[0])
