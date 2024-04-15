# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest

N = int(input())
points = list(map(int, input().split(' ')))
score_counts = {0:1}

for point in points:
    current_scores = list(score_counts.keys()).copy()
    for score in current_scores:
        new_score = score + point
        score_counts[new_score] = score_counts.get(new_score, 0) + score_counts[score]

print(len(score_counts))