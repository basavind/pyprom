def parse(input_file):
    result = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            line = line.split()
            if line not in result:  # some sequence only counts once
                result.append(line)
    return result
