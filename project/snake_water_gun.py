import random

computer=random.choice([1,-1,0])
print("Lets start the game")
print("""select any one of them 'Snake','Water','Gun' """)
youstr = input("Enter your choice: ").lower()
youdict={"snake":1,"water":-1,"gun":0}
reverse_dict={1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]

print(f"your choice {reverse_dict[you]} \n computer choice {reverse_dict[computer]}")

if computer==you:
    print("Its a draw")
    
elif computer==1 and you==-1:
    print("you lose!!!")
    
elif computer==-1 and you==1:
    print("you win!!!")
elif computer==-1 and you==0:
    print("you lose!!!")
elif computer==0 and you==-1:
    print("you win!!!")
elif computer==1 and you==0:
    print("you lose!!!")
elif computer==0 and you==1:
    print("you win!!!")
else:
    print("something went wrong")