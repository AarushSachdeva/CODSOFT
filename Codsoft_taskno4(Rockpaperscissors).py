import random
import tkinter as tk
window=tk.Tk()
window.geometry("500x360")
window.title("Rock Paper Scissors")
Won=Lose=0
possible_choices=["Rock","Paper","Scissors"]
player=""
system_action=""
def random_computer_choice():
    global possible_choices
    return random.choice(possible_choices)
def result(user_input,computer_input):
    global Won
    global Lose
    if(user_input=="Rock" and computer_input=="Scissors"):
        print("You Won")
        Won=Won+1
    elif user_input=="Paper" and computer_input=="Rock":
        print("You Won")
        Won=Won+1
    elif user_input=="Scissors" and computer_input=="Paper":
        print("You Won")
        Won=Won+1
    elif user_input==computer_input:
        print("Draw")
    else:
        print("You Lost")
        Lose=Lose+1
    text_area=tk.Text(master=window,width=30,height=12,bg="#FFFF99")
    text_area.grid(row=6,column=2)
    answer=f"Your choice:{user_input} \nComputer Choice:{computer_input} \nYour Score:{Won} \nComputer Score:{Lose}"
    text_area.insert(tk.END,answer)
def Rock():
    global system_action
    global player
    player="Rock"
    system_action=random_computer_choice()
    result(player,system_action)
def Paper():
    global system_action
    global player
    player="Paper"
    system_action=random_computer_choice()
    result(player, system_action)
def Scissors():
    global system_action
    global player
    player="Scissors"
    system_action=random_computer_choice()
    result(player, system_action)


button1=tk.Button(text="  Rock  ",width=5,height=4,bg="green",command=Rock)
button1.grid(row=1,column=0,padx=3,pady=3)
button2=tk.Button(text="  Paper  ",width=5,height=4,bg="blue",command=Paper)
button2.grid(row=2,column=0,padx=3,pady=3)
button3=tk.Button(text="  Scissors  ",width=5,height=5,bg="pink",command=Scissors)
button3.grid(row=3,column=0,padx=3,pady=3)
window.mainloop()
