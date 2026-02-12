if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from common.gridworld import GridWorld

env = GridWorld()
print("height:" f"{env.height}" ", width:" f"{env.width}")
print("shape:" f"{env.shape}")
print('===')
for action in env.actions():
    print("action:" f"{action}")

print('===')
for state in env.states():
    print("state:" f"{state}")

env.render_v()