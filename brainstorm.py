
import numpy as np
import random
from anytree import Node, RenderTree

def spin():
    spin = np.random.rand(4)
    fail = False
    for row in spin:
        if row > 0.2:
            fail = True

    return not fail

# NUM_USERS = 10
# DEFAULT_SPINS = 0

ROOT = Node("ROOT_USER")

class User(object):
    def __init__(self, invitee=None):
        if not invitee == None:
            self.node = Node(self, parent=ROOT)
        else:
            self.node = Node(self, parent=invitee)

            

def calculate_cost(player, spins):
    ...

def buy_spins(player_index, spins):
    ...

def invite_new_user(inviter_index):
    ...

if __name__ == "__main__":
    ...

