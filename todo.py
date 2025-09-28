import json
import os
from datetime import datetime

time1=datetime.now()
time=time1.strftime("%H:%M")
print("\n \tHello and welcome to the Task Handler of mr Alish\n")

Tasks = []
Status = []

def File_save(location):
     location=f"{location}.json"
     locations=f"C:/Users/USER/OneDrive/Desktop/Python1/Todolist/Data/{location}"
     with open(locations, "w") as Rec:
        json.dump({"Task": Tasks, "Status": Status}, Rec, indent=4)
      
def File_load(location):
     global Tasks, Status
  
     location=f"{location}.json"
     locations=f"C:/Users/USER/OneDrive/Desktop/Python1/Todolist/Data/{location}"
     with open(locations, "r") as rec:
        temp = json.load(rec)
        Tasks, Status = temp["Task"], temp["Status"]

class Tsk_Handler:
    
    def day():  
        while True:
         temp=input("Which Day Is the todolist of(Sunday(S),Monday(M),Tuesday(TU),Wednesday(W),Thrusday(Th),Friday(F),Saturday(SA))").strip()
         if temp=="S":
            return "Sunday"
         if temp=="M":
            return "Monday"
         if temp=="TU":
            return "Tuesday"
         if temp=="W":
            return "Wednesday"
         if temp=="TH":
            return "Thrusday"
         if temp=="F":
            return "Friday"
         if temp=="SA":
            return "Saturday"
         else:
            print("One of the days pleae")
                
    def Commands():
        print("What Task Do You Want To Do")
        print("1)Add A Task \t 2)Remove A Task \t")
        return input("3)List of tasks \t 4)Change the status of a task\t\t5)Exit\n").strip()

    def Task_Add():
        tsk = input("Enter The Task You Have to do").strip()
        sts = input("Enter the status you have the task in").strip()
        Tasks.append(tsk)
        Status.append(sts)
        File_save(Day)

    def Task_list():
        i=0
        print(f"Tsk Number\t||   Tasks\t\t\t||   Status")
        print("----------------||------------------------------||----------------------------------------")
        for ls in Tasks:
            C=i+1
            print(f"{C}\t\t||\t\t{Tasks[i]}\t\t||\t\t{Status[i]}")
            i=i+1
        print("\n")

    def Task_rmv():
     while True:
        R = input("Enter the task number you want to remove ('All' to remove all the tasks): ").strip()
        if R.lower() == 'all':
            Tasks.clear()
            Status.clear()
            File_save(Day)
            break
        elif R.isdigit():
            R = int(R) - 1
            if R >= len(Tasks) or R < 0:
                print("The task doesn't exist")
            else:
                Tasks.pop(R)
                Status.pop(R)
                File_save(Day)
            break
        else:
            print("Enter a number please")

    def ch_sts():
        while True:
            C = input("Enter the task number you want to change the status of").strip()
            if C.isdigit():
                C=int(C)
                C=C-1
                if C >= len(Status) or C < 0:
                    print("The Status doesnt exist")
                else:
                    N_S = input(f"Enter the New status of task number {C+1} you want it to change to").strip()
                    Status[C] = N_S
                    File_save(Day)
                    break
            else:
                print("Enter a number please")

Day=Tsk_Handler.day()
def prgm():
    print(f"\n\n\tIt's currently {time} of {Day}\n")
    Tsk_Handler.Task_list()
    
    while True:
        Orders = Tsk_Handler.Commands()

        if (Orders == '1'):
            Tsk_Handler.Task_Add()
            print("\n Succecfully Added Task! \n")

        elif (Orders == '2'):
            Tsk_Handler.Task_rmv()
            print("\n The Task has successfully been removed \n")
             

        elif (Orders == '3'):
            print("\nHere Is The List of tasks!\n")
            Tsk_Handler.Task_list()

        elif (Orders == '4'):
            Tsk_Handler.ch_sts()
            print("\nsuccessfully changed the status of the task\n")
         
        elif(Orders=='5'):
          
            break
        else:
            print("\nChose a correct option please\n")

try:
    File_load(Day)
except (FileNotFoundError, json.JSONDecodeError):
    File_save(Day)

prgm()





