class Matrix(list[list[int]]):
    """2D matrix of integers, represented as a 2D list"""

    def to_string(self) -> str:
        """Method that will turn the matrix into a string representation"""
        s = "\n"
        for rows in self:
            s = s + "{"  # open matrix brackets, open row
            for cols in rows:
                s = s + f" {cols} "
            s = s + "}\n"  # closing brackets, end row
        return s
