import random
import matplotlib.pyplot as plt
class cursor:

    probabdict = {1:1/2, 2:1/3, 3:1, 4:1, 5: 1/2} #probabilities according to gates in image
    validjump={
        1:[2,4],
        2:[1,3,5],
        3:[2],
        4:[1],
        5:[2,6],
    }#valid jumping positions given an initial position
    def __init__(self,pos=1):
        self.position = pos
        self.stepstoreach6=[0] #stores steps to reach 6 in every try
        self.steps=0 #temp variable to get appended in above later

    def updatepos(self): #checks if position=6 otherwise makes the cursor jump
        if self.position == 6:
            self.position=1
            self.stepstoreach6.append(self.steps)
            self.steps=0
        self.position = random.choices(self.validjump[self.position],[self.probabdict[self.position] for x in self.validjump[self.position]])[0]
        self.steps+=1
        return 0

abc = cursor(1) #intialize the blue bot thing
i=0
avlist = [] #list to store averages
for i in range(1,1000000):
    abc.updatepos()
    if i%100 == 0:
        avlist.append(sum(abc.stepstoreach6)/len(abc.stepstoreach6)) #append avg to the list
print('average steps is {}'.format(avlist[-1]))
#PLOT BELOW
plt.ylabel('average steps')
plt.xlabel('# iterations x 100')
plt.plot(avlist)
plt.show()