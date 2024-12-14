def derangement(n):
    MOD = 10**9 + 7

    if n == 0:
        return 1
    if n == 1:
        return 0

    prev2, prev1 = 1, 0  # D(0) = 1, D(1) = 0
    for i in range(2, n + 1):
        current = (i - 1) * (prev1 + prev2) % MOD
        prev2, prev1 = prev1, current

    return prev1

print(derangement(int(input())))