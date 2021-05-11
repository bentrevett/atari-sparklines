import argparse
import gym
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--game', default='MsPacman', type=str)
parser.add_argument('--n_frames', default=600, type=int)
parser.add_argument('--n_rows', default=16, type=int)
parser.add_argument('--n_cols', default=8, type=int)
parser.add_argument('--fig_height', default=16, type=int)
parser.add_argument('--fig_width', default=24, type=int)
args = parser.parse_args()

env = gym.make(f'{args.game}-ram-v4')

def get_ram_values(env, n_frames):
    values = np.zeros(shape=(n_frames, 128))
    state = env.reset()
    i = 0
    while i < n_frames:
        values[i] = state
        action = env.action_space.sample()
        state, _, done, _ = env.step(action)
        if done:
            i += 1
            if i < n_frames:
                values[i] = state
            state = env.reset()
        i += 1
    return values

values = get_ram_values(env, args.n_frames)

height, width = args.n_rows, args.n_cols
x, y = values.shape
assert height * width == y
fig, axs = plt.subplots(height, width, figsize=(args.fig_width,args.fig_height))
for i, ax in enumerate(axs):
    for j, a in enumerate(ax):
        index = i*width + j
        axs[i, j].plot(values[:,index], color='black', linewidth=0.7)
        axs[i, j].set_axis_off()

plt.savefig('sparklines')