# 68. Softmax Function
import numpy as np


def softmax(scores):
    exp_scores = np.exp(scores - np.max(scores))
    return exp_scores / np.sum(exp_scores)


n = int(input("Enter size: "))
scores = np.random.uniform(0, 1, n)

print("Scores:", scores)
print("Probabilities:", softmax(scores))
