
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

        cost = self.calculate_spin_cost(User) * number_spins
        assert User.balance > cost
        User.balance -= cost
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

    # for sub_human in lisbon.node.descendants:
    #     print(sub_human)

    lisbon.balance = 300 # im rich
    environment.buy_spins(lisbon, 10)
    
    while True:
        input('roll')
        result = environment.spin(lisbon)
        if result:
            print('GAINZZZZZZ@@@!!!!!')
        else:
            print('loser, try again')
        print(f'ur cash {lisbon.balance} ur spins {lisbon.rolls_available}')
        if (environment.calculate_spin_cost(lisbon) > lisbon.balance):
            # can't afford
            print('ur out of cash buddy, sux 2 be u')
            break
        if (lisbon.rolls_available == 0):
            # out of rolls
            buymore = input('BUY mORE SPINS??!! (y/n)')
            if buymore == 'y':
                
                hm = int(input('how many?'))
                
                if (environment.calculate_spin_cost(lisbon) * hm > lisbon.balance):
                    # can't afford
                    print('ur out of cash buddy, sux 2 be u')
                    break
                else:
                    environment.buy_spins(lisbon, hm)
                    print('purchase complete')
            else:
                print('okay, bye')
                break

        