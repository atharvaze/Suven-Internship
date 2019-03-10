import random as r

def coinToss(number):
    recordList, heads, tails = [], 0, 0 # multiple assignment
    for i in range(1,number+1): # do this 'number' amount of times
         flip = r.randint(0, 1)
         if (flip == 0):

              recordList.append("Heads")
         else:

              recordList.append("Tails")
    print(str(recordList))
    print("Number of heads=")
    print(str(recordList.count("Heads")))
    print("Number of tails=")
    print(str(recordList.count("Tails")))

coinToss(int(input("Enter value")))
