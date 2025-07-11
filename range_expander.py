# range_expander.py

def expand_range(input_str):
    result = []
    # Strip whitespaces and ignore empty parts
    parts = [p.strip() for p in input_str.split(",") if p.strip()]
    
    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            result.extend(range(int(start), int(end) + 1))
        else:
            result.append(int(part))
    return result
