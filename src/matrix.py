class Matrix:
    m: list[list[int]]

    def __init__(self, m: list[list[int]]):
        self.m = m

    def to_string(self) -> str:
        s = "\n"
        for rows in self.m:
            s = s + "{"  # open matrix brackets
            for cols in rows:
                s = s + f" {cols} "
            s = s + "}\n"
        return s
