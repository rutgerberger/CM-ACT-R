import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)
import random

## All possible states a peg could take
## Disk 1 is the biggest disk, disk 3 is the smallest and disk 2 is in between
## Disks can only be moved to a peg if the top disk of this peg is larger than the disk to be moved or if this peg has no disks

#1 = 123    i.e. this peg has all disks, the order of how the disks are placed from bottom to top should be read from left to right
#2 = 12     similar to state 1 except no disk 3   
#3 = 23     similar to state 1 except no disk 1
#4 = 1      only disk 1
#5 = 2      only disk 2
#6 = 3      only disk 3
#7 = empty  no disks
#8 = 13     similar to state 1 except no disk 2


class model(ACTR):
    goal=Buffer()
    
    #Above every function, the state is visualized for which that function will be applied
    #123           empty               empty                                      
    def move_1(goal='action:move pegA:1 pegB:7 pegC:7'):
        num = random.randint(0,1)          #initializing a random number between the number of possible moves
        if num == 0:                       #in order to pick a random move
            print("Disk  3 was moved to peg B")
            print("Peg A has disks [1,2], peg B has disks [3], peg C has disks []")
            goal.modify(pegA='2', pegB='6')
        else:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1,2], peg B has disks [], peg C has disks [3]")
            goal.modify(pegA='2', pegC='6')

    #12            empty              3 
    def move_2(goal='action:move pegA:2 pegB:7 pegC:6'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 2 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [2], peg C has disks [3]")
            goal.modify(pegA='4', pegB= '5')
        elif num == 1:
            print("Disk 3 has moved to peg B")
            print("Peg A has disks [1,2], peg B has disks [3], peg C has disks []")
            goal.modify(pegB='6', pegC='7')
        else:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [1,2,3], peg B has disks [], peg C has disks []")
            goal.modify(pegA='1', pegC='7')

    #1              2               3
    def move_3(goal='action:move pegA:4 pegB:5 pegC:6'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [2,3], peg C has disks []")
            goal.modify(pegB ='3', pegC='7')
        elif num == 1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [1,3], peg B has disks [2], peg C has disks []")
            goal.modify(pegA ='8', pegC='7')
        else:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [1,2], peg B has disks [], peg C has disks [3]")
            goal.modify(pegA='2', pegB='7')
        
    #1              23              empty
    def move_4(goal='action:move pegA:4 pegB:3 pegC:7'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 1 was moved to peg C")
            print("Peg A has disks [], peg B has disks [2,3], peg C has disks [1]")
            goal.modify(pegA='7', pegC='4')
        elif num == 1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [1,3], peg B has disks [2], peg C has disks []")
            print("moet nog gedaan worden")
            goal.modify(pegA='8', pegB='5')
        else:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [2], peg C has disks [3]")
            goal.modify(pegB='5', pegC='6')

    #empty              23              1
    def move_5(goal='action:move pegA:7 pegB:3 pegC:4'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [2], peg C has disks [1]")
            goal.modify(pegA='6', pegB='5')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [2], peg C has disks [1,3]")
            goal.modify(pegB='5', pegC='8')
        else:
            print("Disk 1 was moved to peg A")
            print("Peg A has disks [1], peg B has disks [2,3], peg C has disks []")
            goal.modify(pegA='4', pegC='7')
    
    #3              2               1
    def move_6(goal='action:move pegA:6 pegB:5 pegC:4'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [3], peg B has disks [], peg C has disks [1,2]")
            goal.modify(pegB='7', pegC='2')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [2], peg C has disks [1,3]")           
            goal.modify(pegA='7', pegC='8')
        else:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [2,3], peg C has disks [1]")
            goal.modify(pegA='7', pegB='3')


    #3              empty              12
    def move_7(goal='action:move pegA:6 pegB:7 pegC:2'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [], peg C has disks [1,2,3]")
            goal.modify(pegA='7', pegC='1')
        elif num == 1:
            print("Disk 2 was moved to peg B")
            print("Peg A has disks [3], peg B has disks [2], peg C has disks [1]")
            goal.modify(pegB='5', pegC='4')
        else: 
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [3], peg C has disks [1,2]")          
            goal.modify(pegA='7', pegB='6')

    #12             3               empty
    def move_8(goal='action:move pegA:2 pegB:6 pegC:7'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 1 was moved to peg C")
            print("Peg A has disks [1,2], peg B has disks [], peg C has disks [3]")
            goal.modify(pegB='7', pegC='6')
        elif num == 1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [1,2,3], peg B has disks [], peg C has disks []")
            goal.modify(pegA='1', pegB='7')
        else:
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [3], peg C has disks [2]")
            goal.modify(pegA='4', pegC='5')

    #13             2               empty
    def move_9(goal='action:move pegA:8 pegB:5 pegC:7'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [2], peg C has disks [3]")
            goal.modify(pegA='4', pegC='6')
        elif num == 1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [2,3], peg C has disks []")
            goal.modify(pegA='4', pegB='3')
        else: 
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [1,3], peg B has disks [], peg C has disks [2]")
            goal.modify(pegB='7', pegC='5')

    #empty              2               13
    def move_10(goal='action:move pegA:7 pegB:5 pegC:8'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [2], peg B has disks [], peg C has disks [1,3]")
            goal.modify(pegA='5', pegB='7')
        elif num == 1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [2], peg C has disks [1]")
            goal.modify(pegA='4', pegC='6')
        else:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [2,3], peg C has disks [1]")
            goal.modify(pegB='3', pegC='4')

    #empty              3               12
    def move_11(goal='action:move pegA:7 pegB:6 pegC:2'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [], peg C has disks [1,2]")
            goal.modify(pegA='6', pegB='7')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [], peg C has disks [1,2,3]")
            goal.modify(pegB='7', pegC='1')
        else:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [2], peg B has disks [3], peg C has disks [1]")
            goal.modify(pegA='5', pegC='4')

    #1          3           2
    def move_12(goal='action:move pegA:4 pegB:6 pegC:5'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [1,3], peg B has disks [], peg C has disks [2]")
            goal.modify(pegA='8', pegB='7')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [], peg C has disks [2,3]")
            goal.modify(pegB='7', pegC='3')
        else:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [1,2], peg B has disks [3], peg C has disks []")
            goal.modify(pegA='2', pegC='7')

    #13            empty            2
    def move_13(goal='action:move pegA:8 pegB:7 pegC:5'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  2 was moved to peg B")
            print("Peg A has disks [1,3], peg B has disks [2], peg C has disks []")
            goal.modify(pegB='5', pegC='7')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [], peg C has disks [2,3]")
            goal.modify(pegA='4', pegC='3')
        else:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [3], peg C has disks [2]")
            goal.modify(pegA='4', pegB='6')

    #2          empty           13
    def move_14(goal='action:move pegA:5 pegB:7 pegC:8'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  2 was moved to peg B")
            print("Peg A has disks [], peg B has disks [2], peg C has disks [1,3]")
            goal.modify(pegA='7', pegB='5')
        elif num == 1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [2,3], peg B has disks [], peg C has disks [1]")
            goal.modify(pegA='3', pegC='4')
        else:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [2], peg B has disks [3], peg C has disks [1]")
            goal.modify(pegB='6', pegC='4')

    #2          3           1
    def move_15(goal='action:move pegA:5 pegB:6 pegC:4'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [2,3], peg B has disks [], peg C has disks [1]")
            goal.modify(pegA='3', pegB='7')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [2], peg B has disks [], peg C has disks [1,3]")
            goal.modify(pegB='7', pegC='8')
        else:
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [], peg B has disks [3], peg C has disks [1,2]")
            goal.modify(pegA='7', pegC='2')

    #1          empty           23
    def move_16(goal='action:move pegA:4 pegB:7 pegC:3'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [1,3], peg B has disks [], peg C has disks [2]")
            goal.modify(pegA='8', pegC='5')
        elif num == 1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [3], peg C has disks [2]")
            goal.modify(pegB='6', pegC='5')
        else:
            print("Disk 1 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1], peg C has disks [2,3]")
            goal.modify(pegA='7', pegB='4')

    #23         empty           1
    def move_17(goal='action:move pegA:3 pegB:7 pegC:4'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg B")
            print("Peg A has disks [2], peg B has disks [3], peg C has disks [1]")
            goal.modify(pegA='5', pegB='6')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [2], peg B has disks [], peg C has disks [1,3]")
            goal.modify(pegA='5', pegC='8')
        else:
            print("Disk 1 was moved to peg B")
            print("Peg A has disks [2,3], peg B has disks [1], peg C has disks []")
            goal.modify(pegB='4', pegC='7')
    
    #empty          1               23
    def move_18(goal='action:move pegA:7 pegB:4 pegC:3'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  1 was moved to peg A")
            print("Peg A has disks [1], peg B has disks [], peg C has disks [2,3]")
            goal.modify(pegA='4', pegB='7')
        elif num == 1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [1], peg C has disks [2]")
            goal.modify(pegA='6', pegC='5')
        else:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,3], peg C has disks [2]")
            goal.modify(pegB='8', pegC='5')

    #23         1               empty
    def move_19(goal='action:move pegA:3 pegB:4 pegC:7'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg B")
            print("Peg A has disks [2], peg B has disks [1,3], peg C has disks []")
            goal.modify(pegA='5', pegB='8')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [2], peg B has disks [1], peg C has disks [3]")
            goal.modify(pegA='5', pegC='6')
        else:
            print("Disk 1 was moved to peg C")
            print("Peg A has disks [2,3], peg B has disks [], peg C has disks [1]")
            goal.modify(pegB='7', pegC='4')

    #3              1           2
    def move_20(goal='action:move pegA:6 pegB:4 pegC:5'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,3], peg C has disks [2]")
            goal.modify(pegA='7', pegB='8')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [1], peg C has disks [2,3]")
            goal.modify(pegA='7', pegC='3')
        else:
            print("Disk 2 was moved to peg B")
            print("Peg A has disks [3], peg B has disks [1,2], peg C has disks []")
            goal.modify(pegB='2', pegC='7')


    #empty              13              2
    def move_21(goal='action:move pegA:7 pegB:8 pegC:5'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [1], peg C has disks [2]")
            goal.modify(pegA='6', pegB='4')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [1], peg C has disks [2,3]")
            goal.modify(pegB='4', pegC='3')
        else:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [2], peg B has disks [1,3], peg C has disks []")
            goal.modify(pegA='5', pegC='7')

    #2              13              empty
    def move_22(goal='action:move pegA:5 pegB:8 pegC:7'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [2,3], peg B has disks [1], peg C has disks []")
            goal.modify(pegA='3', pegB='4')
        elif num == 1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [2], peg B has disks [1], peg C has disks [3]")
            goal.modify(pegB='4', pegC='6')
        else:
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [], peg B has disks [1,3], peg C has disks []")
            goal.modify(pegA='7', pegC='5')
    
    #2          1           3
    def move_23(goal='action:move pegA:5 pegB:4 pegC:6'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [2,3], peg B has disks [1], peg C has disks []")
            goal.modify(pegA='3', pegC='7')
        elif num == 1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [2], peg B has disks [1,3], peg C has disks []")
            goal.modify(pegB='8', pegC='7')
        else:
            print("Disk 2 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,2], peg C has disks [3]")
            goal.modify(pegA='7', pegB='2')

        #3              12              empty
    def move_24(goal='action:move pegA:6 pegB:2 pegC:7'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [1,2], peg C has disks [3]")
            goal.modify(pegA='7', pegC='6')
        elif num == 1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,2,3], peg C has disks []")
            goal.modify(pegA='7', pegB='1')
        else:
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [3], peg B has disks [1], peg C has disks [2]")
            goal.modify(pegB='4', pegC='5')

    #empty          12              3
    def move_25(goal='action:move pegA:7 pegB:2 pegC:6'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [1,2], peg C has disks []")
            goal.modify(pegA='6', pegC='7')
        elif num == 1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,2,3], peg C has disks []")
            goal.modify(pegB='1', pegC='7')
        else:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [2], peg B has disks [1], peg C has disks [3]")
            goal.modify(pegA='5', pegB='4')

    #empty                  123             empty
    def move_26(goal='action:move pegA:7 pegB:1 pegC:7'):
        num = random.randint(0,1)
        if num == 0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [1,2], peg C has disks []")
            goal.modify(pegA='6', pegB='2')
        else:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [1,2], peg C has disks [3]")
            goal.modify(pegB='2', pegC='6')

    #empty              empty               123
    def finish(goal='action:move pegC:1'):
        print("Problem solved")
        goal.clear()

model=model()
ccm.log_everything(model)
model.goal.set('action:move pegA:1 pegB:7 pegC:7')
model.run()