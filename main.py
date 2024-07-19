rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.")
x=int(input())
#paper>rock;scissor>paper;rock>scissor
if x>=2:
    print("\nYou loose because you entered an invalid number.")
else:
 if x==0:
    print(rock)
 elif x==1:
    print(paper)
 elif x==2:
    print(scissors)
 print("\n Computer chooses:")
 y=random.randint(0,2)

 if y==0:
    print(rock)
 elif y==1:
    print(paper)
 elif y==2:
    print(scissors)
 if (x==0 and y==2) or (x==2 and y==1) or (x==1 and y==0):
    print("You win!")
 elif (x==2 and y==0) or (x==1 and y==2) or (x==0 and y==1):
    print("You lose!")
 else :
    print("Draw!")
