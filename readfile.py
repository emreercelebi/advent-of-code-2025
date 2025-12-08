def read_file(path):
    lines = []
    f = open(path, "r")
    for line in f:
        lines.append(line.strip())
    return lines