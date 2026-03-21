'''Build command line task manager
- Add tasks
-Marks tasks as completed
-categorise tasks
-set priorities
-save/load tasks from file

oops concepts:
1.classes,objects
2.encapsulation
3.inheritance
4.polymorphism
5.file handling with objects

Design:
1.Build base class -task
2.point out inheritance specialised tasks - takes inputs from base class
3.Manager class -coree task in this class
'''


class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.completed = False
    def mark_done(self):
        self.completed = True
    def display(self):
        status = "yes" if self.completed else "No"
        return f"{self.title} [{self.priority}] {status}"


class WorkTask(Task):
    def __init__(self,title,priority,deadline):
        super().__init__(title,priority)
        self.deadline = deadline
    def display(self):
        return super().display() + f' (Deadline : {self.deadline})'
    
class PersonalTask(Task):
    def __init__(self,title,priority,category):
        super().__init__(title,priority)
        self.category = category
    
class TaskManager:
    def __init__(self):
        self.tasks =[]
    def add_tasks(self,task):
        self.tasks.append(task)
    def show_tasks(self):
        for i,task in enumerate(self.tasks):
            print(i,task.display())
    def complete_task(self, index):
        self.tasks[index].mark_done()

def main():
    manager =TaskManager()
    while True:
        print("\n1.Add Task\n2. Show Tasks\n3. complete Task\n4.exit")
        choice = input()
        if choice =='1':
            title = input("title:")
            priority = input("priority:")
            task = Task(title,priority)
            manager.add_tasks(task)
        elif choice == '2':
            manager.show_tasks()
        elif choice == '3':
            index = int(input("Enter the task index: "))
            manager.complete_task(index)
        elif choice == '4':
            break

if __name__ == "__main__":
    main()