#The else keyword in a for loop specifies a block of code to be executed when the loop is finished

"""for x in range (6):
    print(x)
else:
    print ("finally finished")"""

#this prints all the no form 0 to 5 and prints a message when the loop ends
 

#break

#break when the loop is 3 and see what happens to the else block
 
"""for x in range (6):
    if x == 3: break
    print(x)
else:
    print ("finally finished")"""

#If the loop breaks, the else block is not executed.


#NESTED LOOPS
 
 #a loop inside a looop
 #inner will be executed first for each iteration of the "outer loop"

adj = ["red","big","tasty"]
fruits = [ "apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)


#PASS STATEMENT
#to avoid error when for loop is empty when u have a reason to put is empty


for x in [0,1,2]:
    pass


# having an empty for loop like this, would raise an error without the pass statement