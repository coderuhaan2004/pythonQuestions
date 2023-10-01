def hilbert_curve(n):
    if n <= 0:
        return [(0, 0)]

    smaller_curve = hilbert_curve(n - 1)
    size = 2 ** (n - 1)
    result = []

    # Build the top-left quadrant of the current curve
    for x, y in smaller_curve:
        result.append((y, x))
    
    # Build the top-right quadrant of the current curve
    for x, y in smaller_curve:
        result.append((x, y + size))
    
    # Build the bottom-right quadrant of the current curve
    for x, y in smaller_curve:
        result.append((x + size, y + size))
    
    # Build the bottom-left quadrant of the current curve
    for x, y in smaller_curve:
        result.append((size * 2 - 1 - y, size - 1 - x))
    
    return result

# Example usage:
n = 3  # Replace with the desired order
curve = hilbert_curve(n)

# Visualization
grid_size = 2 ** n
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

for x, y in curve:
    grid[y][x] = 'X'

for row in grid:
    print(''.join(row))

