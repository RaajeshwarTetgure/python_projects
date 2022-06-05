# import random
# min = 1
# max = 6

# roll_dice="Yes"
# # if roll_dice=="Yes":
# while roll_dice =="yes" or roll_dice=="y":
#     print("Rolling the dices...")
#     print("The values are....")
#     print(random.randint(1,6))
#     print(random.randint(1,6))

#     roll_dice = input("Wann to roll dice again?" )

# print(roll_dice)


import random
roll_dice = input("Write start to dice roll: ")

if roll_dice == "start":
   posiblle_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))