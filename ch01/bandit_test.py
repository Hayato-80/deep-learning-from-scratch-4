import numpy as np
from bandit import Bandit

bandit = Bandit()
Q = 0
Qs = np.zeros(10)
ns = np.zeros(10)

# for n in range(1,11):
#     reward = bandit.play(0)
#     Q += (reward - Q) / n
#     print(Q)
    # print(bandit.play(0))

for n in range(10):
    action = np.random.randint(0, 10)
    reward = bandit.play(action)
    ns[action] += 1
    Qs[action] += (reward - Qs[action]) / ns[action]
    print(Qs)