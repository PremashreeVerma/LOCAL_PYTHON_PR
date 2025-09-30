import random

machine=random.choice([1,2,3])
print("Lets start the game")
print("""select any one of them 'Stone','Paper','Scissor' """)
person_selection=input("Enter your choice: ").lower()
person_dict={"stone":1,"paper":2,"scissor":3}
reverse_dict={1:"stone",2:"paper",3:"scissor"}
person=person_dict[person_selection]


print(f"your choice {reverse_dict[person]} \n computer choice {reverse_dict[machine]}")

if machine == person:
    print("Its a draw")

elif machine == 2 and person == 1:
    print("you lose!!!")
elif machine == 1 and person == 2:
    print("you win!!!")
elif machine == 3 and person == 1:
    print("you lose!!!")
elif machine == 1 and person == 3:
    print("you win!!!")
elif machine == 3 and person == 2:
    print("you lose!!!")
elif machine == 2 and person == 3:
    print("you win!!!")
else:
    print("something went wrong")
