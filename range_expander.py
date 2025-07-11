# range_expander.py

def expand_range(input_str, delimiters=('-', '..', 'to', '~')):
    result = []
    parts = [p.strip() for p in input_str.split(',') if p.strip()]
    
    for part in parts:
        # Look for matching delimiter
        delimiter_used = next((d for d in delimiters if d in part), None)

        if delimiter_used:
            try:
                start, end = part.split(delimiter_used)
                result.extend(range(int(start), int(end) + 1))
            except ValueError:
                raise ValueError(f"Invalid range part: '{part}'")
        else:
            result.append(int(part))

    return result
