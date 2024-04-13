# https://atcoder.jp/contests/dp/tasks/dp_a

N = int(input())
h = list(map(int, input().split(' ')))

a = [0] * N
a[1] = abs(h[0] - h[1])

for i in range(2, N):
    a[i] = min(
        a[i-1] + abs(h[i-1] - h[i]),
        a[i-2] + abs(h[i-2] - h[i])
        )

print(a[-1])