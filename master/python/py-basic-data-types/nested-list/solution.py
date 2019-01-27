name_scores = []
scores = set()
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    name_scores.append([name, score])
    scores.add(score)


scores.remove(min(scores))
second_min = min(scores)
for (name, score) in sorted(name_scores, key=lambda x : x[0]):
    if score == second_min:
        print(name)