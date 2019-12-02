
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

class Gambling_System(object):
    def __init__(self):
        ...

    def calculate_spin_cost(self, User):
        ...

    def buy_spins(self, User, money):
        ...

class User(object):
    
    def __init__(self, invitee=None):
        if invitee == None:
            self.node = Node(self, parent=ROOT)
        else:
            self.node = Node(self, parent=invitee.node)

        self.rolls_available = 0
        

if __name__ == "__main__":
    # create some users, and hypothetically invite a few of them (form the pyramid)
    lisbon = User()
    voncrub = User(invitee=lisbon)
    volksewagen = User(invitee=lisbon)
    cpt_locke = User(invitee=voncrub)
    plebian = User(invitee=cpt_locke)

    for sub_human in lisbon.node.descendants:
        print(sub_human)

    