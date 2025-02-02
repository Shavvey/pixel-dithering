type Matrix = list[list[int]]

def to_string(m: Matrix) -> str:
    s = "{"
    for _ in m:
        for columns in m:
            s = s + f" {columns} "
        s = s + "\n}"
    return s
