class Matrix(list[list[int]]):
    def __init__(self, m: list[list[int]]):
        self = m

    def to_string(self) -> str:
        s = "\n"
        for rows in self:
            s = s + "{"  # open matrix brackets
            for cols in rows:
                s = s + f" {cols} "
            s = s + "}\n"
        return s
