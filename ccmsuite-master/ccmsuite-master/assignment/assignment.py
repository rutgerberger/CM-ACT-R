import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)
import random

#1 = 123
#2 = 12
#3 = 23
#4 = 1
#5 =2
#6 = 3
#7 = empty
#8 = 13


class model(ACTR):
    goal=Buffer()
    #123           e               e
    def move_1(goal='action:move pegA:1 pegB:7 pegC:7'):
        num = random.randint(0,1)
        if num ==0:
            print("Disk  3 was moved to peg B")
            print("Peg A has disks [1,2], peg B has disks [3], peg C has disks []")
            goal.modify(pegA='2', pegB='6')
        else:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1,2], peg B has disks [], peg C has disks [3]")
            goal.modify(pegA='2', pegC='6')

    #12            e               3 
    def move_2(goal='action:move pegA:2 pegB:7 pegC:6'):
        num = random.randint(0,2)
        if num == 0:
            print("Disk 2 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [2], peg C has disks [3]")
            goal.modify(pegA='4', pegB= '5')
        elif num ==1:
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
        if num ==0:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [2,3], peg C has disks []")
            goal.modify(pegB ='3', pegC='7')
        elif num ==1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [1,3], peg B has disks [2], peg C has disks []")
            goal.modify(pegA ='8', pegC='7')
        else:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [1,2], peg B has disks [], peg C has disks [3]")
            goal.modify(pegA='2', pegB='7')
        
    #1              23              e
    def move_4(goal='action:move pegA:4 pegB:3 pegC:7'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk 1 was moved to peg C")
            print("Peg A has disks [], peg B has disks [2,3], peg C has disks [1]")
            goal.modify(pegA='7', pegC='4')
        elif num ==1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [1,3], peg B has disks [2], peg C has disks []")
            print("moet nog gedaan worden")
            goal.modify(pegA='8', pegB='5')
        else:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [2], peg C has disks [3]")
            goal.modify(pegB='5', pegC='6')

    #e              23              1
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
        if num ==0:
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


    #3              e              12
    def move_7(goal='action:move pegA:6 pegB:7 pegC:2'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [], peg C has disks [1,2,3]")
            goal.modify(pegA='7', pegC='1')
        elif num ==1:
            print("Disk 2 was moved to peg B")
            print("Peg A has disks [3], peg B has disks [2], peg C has disks [1]")
            goal.modify(pegB='5', pegC='4')
        else: 
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [3], peg C has disks [1,2]")          
            goal.modify(pegA='7', pegB='6')

    #12             3               e
    def move_8(goal='action:move pegA:2 pegB:6 pegC:7'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk 1 was moved to peg C")
            print("Peg A has disks [1,2], peg B has disks [], peg C has disks [3]")
            goal.modify(pegB='7', pegC='6')
        elif num ==1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [1,2,3], peg B has disks [], peg C has disks []")
            goal.modify(pegA='1', pegB='7')
        else:
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [3], peg C has disks [2]")
            goal.modify(pegA='4', pegC='5')

    #13             2               e
    def move_9(goal='action:move pegA:8 pegB:5 pegC:7'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [2], peg C has disks [3]")
            goal.modify(pegA='4', pegC='6')
        elif num ==1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [2,3], peg C has disks []")
            goal.modify(pegA='4', pegB='3')
        else: 
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [1,3], peg B has disks [], peg C has disks [2]")
            goal.modify(pegB='7', pegC='5')

    #e              2               13
    def move_10(goal='action:move pegA:7 pegB:5 pegC:8'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [2], peg B has disks [], peg C has disks [1,3]")
            goal.modify(pegA='5', pegB='7')
        elif num==1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [2], peg C has disks [1]")
            goal.modify(pegA='4', pegC='6')
        else:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [2,3], peg C has disks [1]")
            goal.modify(pegB='3', pegC='4')

    #e              3               12
    def move_11(goal='action:move pegA:7 pegB:6 pegC:2'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [], peg C has disks [1,2]")
            goal.modify(pegA='6', pegB='7')
        elif num==1:
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
        if num ==0:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [1,3], peg B has disks [], peg C has disks [2]")
            goal.modify(pegA='8', pegB='7')
        elif num==1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [], peg C has disks [2,3]")
            goal.modify(pegB='7', pegC='3')
        else:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [1,2], peg B has disks [3], peg C has disks []")
            goal.modify(pegA='2', pegC='7')

    #13            e            2
    def move_13(goal='action:move pegA:8 pegB:7 pegC:5'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  2 was moved to peg B")
            print("Peg A has disks [1,3], peg B has disks [2], peg C has disks []")
            goal.modify(pegB='5', pegC='7')
        elif num==1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [1], peg B has disks [], peg C has disks [2,3]")
            goal.modify(pegA='4', pegC='3')
        else:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [3], peg C has disks [2]")
            goal.modify(pegA='4', pegB='6')

    #2          e           13
    def move_14(goal='action:move pegA:5 pegB:7 pegC:8'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  2 was moved to peg B")
            print("Peg A has disks [], peg B has disks [2], peg C has disks [1,3]")
            goal.modify(pegA='7', pegB='5')
        elif num==1:
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
        if num ==0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [2,3], peg B has disks [], peg C has disks [1]")
            goal.modify(pegA='3', pegB='7')
        elif num==1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [2], peg B has disks [], peg C has disks [1,3]")
            goal.modify(pegB='7', pegC='8')
        else:
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [], peg B has disks [3], peg C has disks [1,2]")
            goal.modify(pegA='7', pegC='2')

    #1          e           23
    def move_16(goal='action:move pegA:4 pegB:7 pegC:3'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [1,3], peg B has disks [], peg C has disks [2]")
            goal.modify(pegA='8', pegC='5')
        elif num==1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [1], peg B has disks [3], peg C has disks [2]")
            goal.modify(pegB='6', pegC='5')
        else:
            print("Disk 1 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1], peg C has disks [2,3]")
            goal.modify(pegA='7', pegB='4')

    #23         e           1
    def move_17(goal='action:move pegA:3 pegB:7 pegC:4'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  3 was moved to peg B")
            print("Peg A has disks [2], peg B has disks [3], peg C has disks [1]")
            goal.modify(pegA='5', pegB='6')
        elif num==1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [2], peg B has disks [], peg C has disks [1,3]")
            goal.modify(pegA='5', pegC='8')
        else:
            print("Disk 1 was moved to peg B")
            print("Peg A has disks [2,3], peg B has disks [1], peg C has disks []")
            goal.modify(pegB='4', pegC='7')
    
    #e          1               23
    def move_18(goal='action:move pegA:7 pegB:4 pegC:3'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  1 was moved to peg A")
            print("Peg A has disks [1], peg B has disks [], peg C has disks [2,3]")
            goal.modify(pegA='4', pegB='7')
        elif num==1:
            print("Disk 3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [1], peg C has disks [2]")
            goal.modify(pegA='6', pegC='5')
        else:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,3], peg C has disks [2]")
            goal.modify(pegB='8', pegC='5')

    #23         1               e
    def move_19(goal='action:move pegA:3 pegB:4 pegC:7'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  3 was moved to peg B")
            print("Peg A has disks [2], peg B has disks [1,3], peg C has disks []")
            goal.modify(pegA='5', pegB='8')
        elif num==1:
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
        if num ==0:
            print("Disk  3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,3], peg C has disks [2]")
            goal.modify(pegA='7', pegB='8')
        elif num==1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [1], peg C has disks [2,3]")
            goal.modify(pegA='7', pegC='3')
        else:
            print("Disk 2 was moved to peg B")
            print("Peg A has disks [3], peg B has disks [1,2], peg C has disks []")
            goal.modify(pegB='2', pegC='7')


    #e              13              2
    def move_21(goal='action:move pegA:7 pegB:8 pegC:5'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [1], peg C has disks [2]")
            goal.modify(pegA='6', pegB='4')
        elif num==1:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [1], peg C has disks [2,3]")
            goal.modify(pegB='4', pegC='3')
        else:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [2], peg B has disks [1,3], peg C has disks []")
            goal.modify(pegA='5', pegC='7')

    #2              13              e
    def move_22(goal='action:move pegA:5 pegB:8 pegC:7'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [2,3], peg B has disks [1], peg C has disks []")
            goal.modify(pegA='3', pegB='4')
        elif num==1:
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
        if num ==0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [2,3], peg B has disks [1], peg C has disks []")
            goal.modify(pegA='3', pegC='7')
        elif num==1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [2], peg B has disks [1,3], peg C has disks []")
            goal.modify(pegB='8', pegC='7')
        else:
            print("Disk 2 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,2], peg C has disks [3]")
            goal.modify(pegA='7', pegB='2')

        #3              12              e
    def move_24(goal='action:move pegA:6 pegB:2 pegC:7'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [1,2], peg C has disks [3]")
            goal.modify(pegA='7', pegC='6')
        elif num==1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,2,3], peg C has disks []")
            goal.modify(pegA='7', pegB='1')
        else:
            print("Disk 2 was moved to peg C")
            print("Peg A has disks [3], peg B has disks [1], peg C has disks [2]")
            goal.modify(pegB='4', pegC='5')

    #e          12              3
    def move_25(goal='action:move pegA:7 pegB:2 pegC:6'):
        num = random.randint(0,2)
        if num ==0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [1,2], peg C has disks []")
            goal.modify(pegA='6', pegC='7')
        elif num==1:
            print("Disk 3 was moved to peg B")
            print("Peg A has disks [], peg B has disks [1,2,3], peg C has disks []")
            goal.modify(pegB='1', pegC='7')
        else:
            print("Disk 2 was moved to peg A")
            print("Peg A has disks [2], peg B has disks [1], peg C has disks [3]")
            goal.modify(pegA='5', pegB='4')

    #e                  123             e
    def move_26(goal='action:move pegA:7 pegB:1 pegC:7'):
        num = random.randint(0,1)
        if num ==0:
            print("Disk  3 was moved to peg A")
            print("Peg A has disks [3], peg B has disks [1,2], peg C has disks []")
            goal.modify(pegA='6', pegB='2')
        else:
            print("Disk 3 was moved to peg C")
            print("Peg A has disks [], peg B has disks [1,2], peg C has disks [3]")
            goal.modify(pegB='2', pegC='6')

    #e              e               123
    def finish(goal='action:move pegC:1'):
        print("Problem solved")
        goal.clear()

model=model()
ccm.log_everything(model)
model.goal.set('action:move pegA:1 pegB:7 pegC:7')
model.run()