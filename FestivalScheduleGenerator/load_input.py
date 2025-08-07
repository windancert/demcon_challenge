def load_input(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            # Remove trailing newline and split by spaces
            parts = line.strip().split()
            # Convert to tuple with appropriate types
            parts = (parts[0], int(parts[1]), int(parts[2]))
            result.append(parts)
    return result
