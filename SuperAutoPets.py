import random
import time
#import pandas as pd

class Die:
    def __init__(self,max_val):
        self.frozen=False
        self.max_val=max_val
        self.value=random.randint(1,max_val)

    def roll_die(self):
        if not self.frozen:
            #print("rerolling")
            self.value=random.randint(1,self.max_val)
            #print(self.value)
        #else:
            #print("dice is frozen, not rerolling")
            #print(self.value)
        return self.value

    def freeze_die(self):
        self.frozen=True

    def unfreeze_die(self):
        self.frozen=False

class Dice:
    def __init__(self,num_dice,max_val):
        self.dice = [Die(max_val) for _ in range(num_dice)]
    def roll_dice(self):
        for die in self.dice:
            die.roll_die()
        return self.dice
    def freeze_die_index(self,index):
       self.dice[index].freeze_die()
    def unfreeze_die_index(self,index):
       self.dice[index].unfreeze_die()
    def get_die_value(self,index):
        return self.dice[index].value
    def get_die_status(self,index):
        return self.dice[index].frozen
    def get_number_frozen(self):
        count=0
        for die in self.dice:
            if die.frozen:
                count=count+1
        return count
    def print_dice_list(self):
        n=0
        for die in self.dice:
            print(f"die {n}: {die.value}")
            n=n+1

def get_freeze_fish(my_dice,index,gold,fish_count):
    #print(f"---Checking die {index} ----")
    #print(f"gold is {gold}")
    #print(f"dice value was {my_dice.get_die_value(index)}")
    if my_dice.get_die_value(index)==1 and gold>=3:
        fish_count=fish_count+1
        gold=gold-3
        #print("buying fish")
        my_dice.unfreeze_die_index(index)
        #print("unfreezing die")
    elif my_dice.get_die_value(index)==1:
        my_dice.freeze_die_index(index)
        #print("freezing fish")
    #print(f"gold is now {gold}")
    #print(f"fish_count is now {fish_count}")
    return [gold,fish_count]

startTime=time.time()
fish_list=[]
frozen_list=[]
for m_index in range(1000001):
    #print("==== START OF SIM ======")
    gold=10
    round=1
    fish_count=0
    round1_fish=0
    round1_frozen=0
    num_dice=3
    my_dice=Dice(num_dice,10)
    while gold>=0:
        #print("====== NEW ROLL ========")
        my_dice.roll_dice()
        #my_dice.print_dice_list()
        for index in range(num_dice):
            new_vals=get_freeze_fish(my_dice,index,gold,fish_count)
            gold=new_vals[0]
            fish_count=new_vals[1]
        #print(f"gold val {gold}")
        #print(f"fish count {fish_count}")
        #print(f"num frozen {my_dice.get_number_frozen()}")
        gold=gold-1

        if gold<0 and round==1:
            round=2
            gold=10
            round1_fish=fish_count
            round1_frozen=my_dice.get_number_frozen()
            #print("+++++++++++ Next Round +++++++++++")

    round2_fish=round1_fish
    round2_frozen=my_dice.get_number_frozen()
    final_fish=fish_count
    final_frozen=my_dice.get_number_frozen()
    #print(f"Number of first round fish {round1_fish}")
    #print(f"Number of first round frozen {round1_frozen}")
    #print(f"Number of second round fish {round2_fish}")
    #print(f"Number of second round frozen {round2_frozen}")
    #print(f"Number of final fish {final_fish}")
    #print(f"Number of final frozen {final_frozen}")
    fish_list.append(final_fish)
    frozen_list.append(final_frozen)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))


# my_die=Die(10)
# print(my_die)
# val2=my_die.value
# print(val2)
# val=my_die.roll_die()
# print(val)
# print(my_die.value)
# val=my_die.roll_die()
# print(val)
# print(my_die.value)
#
#
# my_dice=Dice(3,10)
# print(type(my_dice))
# print("dice")
# for val in my_dice.dice:
#     print(val.value)
# print("die 2")
# print(my_dice.roll_dice()[1].value)
#
# print("new vals")
# print(my_dice.get_die_value(1))
# print(my_dice.get_die_status(1))
# my_dice.freeze_die_index(1)
# print(my_dice.get_die_status(1))
# print("before")
# for val in my_dice.dice:
#     print(val.value)
# print("after")
# my_dice.roll_dice()
# for val in my_dice.dice:
#     print(val.value)
# #print(my_dice.get_die_value(1))
# my_dice.roll_dice()
# print("after 2")
# for val in my_dice.dice:
#     print(val.value)
# my_dice.freeze_die_index(2)
# print(my_dice.get_number_frozen())