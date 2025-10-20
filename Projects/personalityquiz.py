Gryffindor_points = 0
Hufflepuff_points = 0
Ravenclaw_points  = 0
Slytherin_points  = 0

answer = input ("You would be most hurt if someone called you A weak, B ignorant, C Unkind or D Boring")
if answer == "A":
   Gryffindor_points += 1
elif answer == "B":
   Ravenclaw_points  += 1
elif answer == "C": 
   Hufflepuff_points += 1
elif answer == "D":
   Slytherin_points  += 1

answer = input ("Which of these most accurately  describe  your relationships with your closest friend A i am love surrounding myself with new people, B I have a few very close friends that i would trust with my life, C I dont often make new friends and i tend to be wary when making then, or D i find myself becoming freinds with people who can make me more successful") 
if answer == "A":
    Hufflepuff_points += 1
elif answer == "B":
    Ravenclaw_points += 1
elif answer == "C": 
    Slytherin_points += 1
elif answer == "D":
    Gryffindor_points += 1

answer = input ("Wich of the following do you find most difficult to deal with A Loneliness, B Feeling stupid, C lack of control, or D Boredom")
if answer == input == "A":
    Hufflepuff_points += 1
elif answer == "B":
    Ravenclaw_points += 1
elif answer == "C": 
    Slytherin_points += 1
elif answer == "D":
    Gryffindor_points += 1

    answer = input (" What is your favorite animal A dog, B lama, C mouse, or a mountain lion ")
if answer == input == "A": 
    Hufflepuff_points += 1
elif answer == "B":
    Ravenclaw_points += 1
elif answer == "C": 
    Slytherin_points += 1
elif answer == "D":
    Gryffindor_points += 1

    answer == input ("if you could play any posion in Quiditch what would you chose A seeker, B chaser, C beater or D youll be in the crowd makign sure supporter moral is high")
if answer == input == "A": 
    Gryffindor_points += 1
elif answer == "B":
    Ravenclaw_points += 1
elif answer == "C": 
    Slytherin_points += 1
elif answer == "D":
    Hufflepuff_points += 1

if Gryffindor_points > Hufflepuff_points and Gryffindor_points > Ravenclaw_points and Gryffindor_points > Slytherin_points:
    print ("You are in the gryffindor house!")
elif Hufflepuff_points > Gryffindor_points and Hufflepuff_points > Ravenclaw_points and Hufflepuff_points > Slytherin_points:
    print ("You are in the Hufflepuff house!")
elif Ravenclaw_points> Gryffindor_points and Ravenclaw_points > Hufflepuff_points and Ravenclaw_points > Slytherin_points:
    print ("You are in the Ravenclaw house!")
elif Slytherin_points > Hufflepuff_points and Slytherin_points > Ravenclaw_points and Slytherin_points > Gryffindor_points:
    print ("You are in the Slytherin house!)")