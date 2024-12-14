# generate subsets of an array
def generate_subsets(array):
    n = len(array)
    subsets = []

    # Iterate through all possible bitmasks (2^n combinations)
    for mask in range(1 << n):  # 1 << n is 2^n
        subset = []
        for i in range(n):
            # Check if the i-th bit is set in the mask
            if mask & (1 << i):
                subset.append(array[i])
        subsets.append(subset)

    return subsets

# Example usage
array = [1, 2, 3]
all_subsets = generate_subsets(array)
print("All subsets:", all_subsets)