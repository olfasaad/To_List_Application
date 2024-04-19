# 1 - add tasks to a list 
#2-mark task as complete 
#3- view tasks 
#4-Quit 
tasks=[{"task":"Quran","completed":True},
       {"task":"study","completed":False},
       {"task":"qym","completed":True},
       {"task":"play","completed":False}]

message ="""
 1 - add tasks to a list 
 2-mark task as complete 
 3- view tasks 
 4-Quit """

def add_task():
   #get task from user 
   task=input ("enter ur task: ")
   note =input ("enter ur note related to this task ")
   #define task status 
   task_info={"task":task,"completed":False, "note":note}
   #add task to the list of tasks
   tasks.append(task_info)
   print(f"tasks of list {tasks}")
   
def mark_task():
   #get list of incomplete 
   #we can use this method
   #incomplete_task=[task for task in tasks if task["completed"]==False]
   
   incomplete_task=[]
   #or this 
   for i in tasks:
      if i["completed"]==False:
        incomplete_task.append(i)
   print(incomplete_task)
   #show the incomplete task 
   if incomplete_task:
      for i in tasks:
         if i["completed"]==False:
            stat="progress"
         else:
            stat="complete"
            print(f"{i}-{i['task']} the status in : {stat} /n")
      for i,task in enumerate(incomplete_task):
         print(f"{i+1}-{task['task']}")
    #get number of task from user
      try:
         number=int (input("choose the task to complete "))
         if number<1 or number > len(incomplete_task):
            print("Invalid Task number")
            return
    #Mark task as completed 
         incomplete_task [number - 1]["completed"]=True
     # incomplete_task[0]["completed"]=True
         print(incomplete_task[number-1])
         print (tasks)
      except ValueError:
         print("invalid input please enter a number ")
      except IndexError:
         print("Please choose from the available tasks ")
def view_tasks(tasks):
   if not tasks:
      print("no taks to view")
      return
   for i,j in enumerate(tasks):
      #if j["completed"]==False:
      #   status="🚩"
          
      #   print(f"{i+1}.{j['task']} is incompleted {status}")
      
      #else:
       #  status="✔" 
      status="✔" if j['completed'] else "🚩"
      print(f"{i+1}.{j['task']}  {status}")

def main ():
   

   while True :
    print (message)
    choice=input("enter ur choice ")
    if choice=="1":
       add_task()
    elif choice=="2":
       mark_task()
    elif choice=="3":
      view_tasks(tasks)
    elif choice=="4":
      break
    else:
      print("Invalid choice ,please enter e nuber entre 1 & 4")

if __name__=="__main__":
   main()
   