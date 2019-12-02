
import numpy as np
import random
from anytree import Node, RenderTree


# NUM_USERS = 10
# DEFAULT_SPINS = 0

ROOT = Node("ROOT_USER")

class Gambling_System(object):
    def __init__(self):
        self.BASE_SPIN_COST = 2.0
        self.BASE_SPIN_REWARD = 5.0
    def calculate_spin_cost(self, User):
        # cost could be based on how many people you've invited (maybe discount for people who invite lots)

        #stub
        return self.BASE_SPIN_COST

    def buy_spins(self, User, number_spins):
        # stub
        assert number_spins >= 0
        User.rolls_available += number_spins

    def spin(self, User):
        assert User.rolls_available >= 1
        User.rolls_available -= 1

        spin = random.random()
        if spin > 0.2:
            return False
        else:
            User.balance += self.BASE_SPIN_REWARD
            return True

class User(object):
    
    def __init__(self, invitee=None):
        if invitee == None:
            self.node = Node(self, parent=ROOT)
        else:
            self.node = Node(self, parent=invitee.node)

        self.rolls_available = 0
        self.balance = 0
        

if __name__ == "__main__":
    environment = Gambling_System()
    
    # create some users, and hypothetically invite a few of them (form the pyramid)
    lisbon = User()
    voncrub = User(invitee=lisbon)
    volksewagen = User(invitee=lisbon)
    cpt_locke = User(invitee=voncrub)
    plebian = User(invitee=cpt_locke)

    for sub_human in lisbon.node.descendants:
        print(sub_human)


    environment.buy_spins(lisbon, 10)
    
    
