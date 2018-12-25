import random
 
def numguess():
    random_val=random.randint(1,100)
    for i in range(10):
        input_val=input_answer()
        if(input_val==random_val):
            flag = False
            print("Your Collect")
            break
        elif(input_val>random_val):
            print("Your input is bigger than Number")
        else:
            print("Yout inpur is smaller than Number")

def input_answer():
    try :
        return int(input("Input Your Value (0~100)"))
    except:
        numguess()

numguess()
