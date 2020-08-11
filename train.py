"""https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html"""

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T
from dqn import DQN
from replay_memory import ReplayMemory, Transition
from game.environment import Environment

BATCH_SIZE = 128
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 200
TARGET_UPDATE = 10

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

env = Environment()
screen_height, screen_width = env.screen_shape
n_actions = env.size_action_space

policy_net = DQN(screen_height, screen_width, n_actions).to(device)
target_net = DQN(screen_height, screen_width, n_actions).to(device)
target_net.load_state_dict(policy_net.state_dict())
target_net.eval()

optimizer = optim.RMSprop(policy_net.parameters())
memory = ReplayMemory(10000)
steps_done = 0

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def train():
    num_episodes = 50
    for i_episode in range(num_episodes):
        # Initialize the environment and state
        env.reset()
        last_screen = env.get_screen()
        current_screen = env.get_screen()
        state = current_screen - last_screen
        while not env.done:
            # action = select_action(state)
            reward, done = env.step()
            reward = torch.tensor([reward], device=device)

            # Observe new state
            last_screen = env.get_screen()
            current_screen = env.get_screen()
            if not done:
                next_state = current_screen - last_screen
            else:
                next_state = None

            # Store the transition in memory
            memory.push(state, action, next_state, reward)

            # Move to the next state
            state = next_state

            # Perform one step of the optimization (on the target network)
            optimize_model()
            if done:
                # graph something
                break
        # Update the target network, copying all weights and biases in DQN
        if i_episode % TARGET_UPDATE == 0:
            target_net.load_state_dict(policy_net.state_dict())


if __name__ == '__main__':
    active_keys = env.console.controller.get_active_keys()
    train()
