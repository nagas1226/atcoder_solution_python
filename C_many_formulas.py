# https://atcoder.jp/contests/abc045/tasks/arc061_a

from itertools import product

S = input()
N = len(S)

ans = 0
for bits in product([0,1], repeat=N-1): # itertoolsを使ったbit全探索
    s = 0
    a = S[0]
    for i, bit in enumerate(bits):
        if bit:
            s += int(a)
            a = S[i+1]
        else:
            a += S[i+1]
    s += int(a)
    ans += s
print(ans)

# ans = 0
# for bit in range(1 << (N-1)): # bit全探索
#     s = 0
#     a = S[0]
#     for i in range(N-1):
#         if not ((bit >> i) & 1):
#             a += S[i+1]
#         else:
#             s += int(a)
#             a = S[i+1]
#     s += int(a)
#     ans += s
# print(ans)            
