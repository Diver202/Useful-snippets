#Give nth fibonacci number modulo MOD
#Remove MOD for no modulo
MOD = 10**9 + 7

def mat_mult(A, B, mod=MOD):
    """Performs matrix multiplication (modulo mod)."""
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, 
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, 
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]

def mat_pow(matrix, power, mod=MOD):
    """Performs matrix exponentiation (modulo mod)."""
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = matrix
    while power:
        if power % 2 == 1:
            result = mat_mult(result, base, mod)
        base = mat_mult(base, base, mod)
        power //= 2
    return result

def fibonacci(n, mod=MOD):
    """Computes the nth Fibonacci number modulo mod."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Transformation matrix
    T = [[1, 1], [1, 0]]
    # Compute T^(n-1)
    T_n_minus_1 = mat_pow(T, n-1, mod)
    # Result is F(n)
    return T_n_minus_1[0][0]

# Example usage
print(fibonacci(int(input())))