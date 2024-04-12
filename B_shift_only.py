N = int(input())
A = list(map(int, input().split(' ')))

ans = 0
is_even = True
while is_even:
    for i in range(N):
        if A[i] % 2 != 0:
            is_even = False
        else:
            A[i] = A[i] // 2
    if is_even:
        ans += 1
print(ans)
