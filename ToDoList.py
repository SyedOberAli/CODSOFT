def task():
    Tasks = []
    print("---Welcome to the Task Mananagement app!---")
    Total_task = int(input("Enter the total number of task : "))
    for i in range(1,Total_task+1):
        task_name = input(f"Enter the task {i} =")
        Tasks.append(task_name)
    print(f"Todays task are\n{Tasks}")

    while True:
        try:
            operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n "))
            if operation == 1:
                Add = input("Enter the task u want to add :")
                Tasks.append(Add)
                print(f"Task '{Add}' been successfully added.")

            elif operation ==2:
                    old_task = input("Enter the task u want to update:")
                    if old_task in Tasks:
                        new_task = input("Enter the task:")
                        ind = Tasks.index(old_task) 
                        Tasks[ind] = new_task
                        print(f"Task has been updated from '{old_task}' to '{new_task}'. ")
                    else:
                         print("Task Not Found.")

            elif operation == 3:
                 del_task = input("Enter the task u want to delete:")
                 if del_task in Tasks:
                      ind = Tasks.index(del_task)
                      del Tasks[ind]
                      print(f"Task '{del_task}'5 has been deleted sucessfully.")
                 else:
                      print("Task not found.")
            
            elif operation == 4:
                 print(f"Total Tasks = {Tasks}")

            elif operation == 5:
                 print(f"You have been exit from the program...")
                 break
            else:
                 print("----Invalid input.Please Enter number between 1 to 5.---- ")

        except ValueError:
             print("Invalid input.Please enter a valid number.")

task()        

