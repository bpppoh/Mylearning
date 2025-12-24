import random 

try :
    choice = ["Rock" , "Paper" , "Scissor"]
    computer_choice = random.randint(0,len(choice)-1)
    print("Choose one of these (type only number 1 - 3)")
    for i in range (0,len(choice)) :
        print(f"{i+1}. {choice[i]}")
        
    user_choice = int(input(">> "))
    if user_choice < 1 or user_choice > 3 :
        raise
    user_choice = user_choice-1
    
    print(f"Computer choice : {choice[computer_choice]}")
    print(f"User Choice : {choice[user_choice]}")
    if user_choice - computer_choice > 1 or computer_choice - user_choice == 1 :
        print("Computer Win !!!")
    elif computer_choice - user_choice > 1 or user_choice - computer_choice == 1 :
        print("User Win !!!")
    else :
        print("Tie !!!")
except:
    print("Error")
    
print("End Programme")