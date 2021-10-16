import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)


#1 = 123
#2 = 12
#3 = 23
#4 = 1
#5 =2
#6 = 3
#7 = empty


class model(ACTR):
    goal=Buffer()
    def move_1(goal='action:move pegA:1 pegB:7 pegC:7'):
        print("Disk 3 was moved to peg C")
        print("Peg A has disks [1,2], peg B has disks [], peg C has disks [3]")
        goal.modify(pegA='2',pegC='6')
    def move_2(goal='action:move pegA:2 pegB:7 pegC:6'):
        print("Disk 2 was moved to peg B")
        print("Peg A has disks [1], peg B has disks [2], peg C has disks [3]")
        goal.modify(pegA='4', pegB= '5')
    def move_3(goal='action:move pegA:4 pegB:5 pegC:6'):
        print("Disk 3 was moved to peg B")
        print("Peg A has disks [1], peg B has disks [2,3], peg C has disks []")
        goal.modify(pegB ='3', pegC='7')
    def move_4(goal='action:move pegA:4 pegB:3 pegC:7'):
        print("Disk 1 was moved to peg C")
        print("Peg A has disks [], peg B has disks [2,3], peg C has disks [1]")
        goal.modify(pegA='7', pegC='4')
    def move_5(goal='action:move pegA:7 pegB:3 pegC:4'):
        print("Disk 3 was moved to peg A")
        print("Peg A has disks [3], peg B has disks [2], peg C has disks [1]")
        goal.modify(pegA='6', pegB='5')
    def move_6(goal='action:move pegA:6 pegB:5 pegC:4'):
        print("Disk 2 was moved to peg C")
        print("Peg A has disks [3], peg B has disks [], peg C has disks [1,2]")
        goal.modify(pegB='7', pegC='2')
    def move_7(goal='action:move pegA:6 pegB:7 pegC:2'):
        print("Disk 3 was moved to peg C")
        print("Peg A has disks [], peg B has disks [], peg C has disks [1,2,3]")
        goal.modify(pegA='7', pegC='1')

    def finish(goal='action:move pegC:1'):
        print("Problem solved")
        goal.clear()

model=model()
ccm.log_everything(model)
model.goal.set('action:move pegA:1 pegB:7 pegC:7')
model.run()