# https://atcoder.jp/contests/abc032/tasks/abc032_d

N, W = list(map(int, input().split(' ')))

v, w = [], []
for i in range(N):
    v_i, w_i = list(map(int, input().split(' ')))
    v.append(v_i)
    w.append(w_i)


dp = [[0]*(W+1) for _ in range(N)]

for i in range(N):
    for j in range(W+1):
        if i == 0:            
            dp[i][j] = v[i] if (w[i] <= j) else 0
        else:
            if j-w[i] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

print(dp[N-1][W])