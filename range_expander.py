def expand_range(input_str):
    result = []
    parts = input_str.split(",")
    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            result.extend(range(int(start), int(end) + 1))
        else:
            result.append(int(part))
    return result
