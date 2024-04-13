# https://atcoder.jp/contests/abc114/tasks/abc114_c

# from itertools import product
# N = input()
# l = len(N)
# N = int(N)

# ans = 0
# if l<3:
#     print(0)
# else:    
#     for n_digits in range(3, l+1):
#         for num in product(['7', '5', '3'], repeat=n_digits):
#             if ('7' in num) and ('5' in num) and ('3' in num):                
#                 num = int(''.join(num))
#                 if num <= N:
#                     print(num)
#                     ans += 1
# print(ans)


# # 再帰を使った全探索
def func(N, cur, use, counter):
    if cur > N:
        return
    if use == 0b111:
        counter[0] += 1

    func(N, cur * 10 + 7, use | 0b001, counter)
    func(N, cur * 10 + 5, use | 0b010, counter)
    func(N, cur * 10 + 3, use | 0b100, counter)

def main():
    N = int(input())
    counter = [0]
    func(N, 0, 0, counter)
    print(counter[0])
    
if __name__=='__main__':
    main()
