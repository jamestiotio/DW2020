class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    lines = []
    max_mag = Coordinate()
    min_mag = Coordinate()

    for line in f:
        lines.append(line)

    # Initialize values
    max_mag.x = float(lines[0].split("\t")[0])
    max_mag.y = float(lines[0].split("\t")[1])
    min_mag.x = float(lines[0].split("\t")[0])
    min_mag.y = float(lines[0].split("\t")[1])

    # Check for max
    for line in lines:
        x = float(line.split("\t")[0])
        y = float(line.split("\t")[1])
        if (x ** 2 + y ** 2) > (max_mag.x ** 2 + max_mag.y ** 2):
            max_mag.x = x
            max_mag.y = y

    # Check for min
    for line in lines:
        x = float(line.split("\t")[0])
        y = float(line.split("\t")[1])
        if (x ** 2 + y ** 2) < (min_mag.x ** 2 + min_mag.y ** 2):
            min_mag.x = x
            min_mag.y = y

    return (max_mag, min_mag)