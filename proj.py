""" Mad Libs Generator
----------------------------------------
"""
# Loop back to this point once code finishes
loop = 1
while (loop < 10):
    # # All the questions that the program asks the user
#     noun = input("Choose a noun: ")
#     p_noun = input("Choose a plural noun: ")
#     noun2 = input("Choose a noun: ")
#     place = input("Name a place: ")
#     adjective = input("Choose an adjective (Describing word): ")
#     noun3 = input("Choose a noun: ")
# # Displays the story based on the users input
#     print ("------------------------------------------")
#     print ("Be kind to your",noun,"- footed", p_noun)
#     print ("For a duck may be somebody's", noun2,",")
#     print ("Be kind to your",p_noun,"in",place)
#     print ("Where the weather is always",adjective,".")
#     print ()
#     print ("You may think that is this the",noun3,",")
#     print ("Well it is.")
#     print ("------------------------------------------")

    animals = input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name = input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')

    print('\nsay ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place + ' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' +
          animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

# Loop back to "loop = 1"
    loop = loop + 1
