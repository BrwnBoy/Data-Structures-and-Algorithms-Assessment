def remove_duplicates(sequence):
    seen = set()
    result = []
    for item in sequence:
        # If the item hasn't been encountered before, add it to the result and set
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result