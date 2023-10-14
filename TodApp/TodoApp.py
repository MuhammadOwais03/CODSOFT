import time
import os
""" from TodoApp import * """
class FileSaver:
    def saveToFile(self, obj):
        with open('todo.txt', 'a') as f:
            f.write(obj+'\n')

class FileReader:
    def readFromFile(self):
        List = []
        try:
            with open('todo.txt', 'r') as f:
                readList = f.read().split('\n')

            for dic in readList:
                List.append(eval(dic))
            return List
        except SyntaxError:
            return List

class Todo:
    def __init__(self):
        self.filesaver = FileSaver()
        self.fileReader = FileReader()

    def AddTodo(self, todo, id):
        obj = {id:[todo, "Pending"]}
        self.filesaver.saveToFile(str(obj))
    
    def readTodo(self):

        List = self.fileReader.readFromFile()
        if List != []:
            return List
        else:
            return  "NO"
    def Delete(self, id):
        List = self.readTodo()
        if List != "NO":
            for dic in List:
                for key, todo in dic.items():
                    if str(key) == str(id):
                        List.remove(dic)
            with open('todo.txt', 'w') as f:
                for dic in List:
                    f.write(str(dic)+'\n')
        else:
            print("NO ITEMS")
    
    def MarkAsCompleted(self, id):
        List = self.fileReader.readFromFile()
        if List !=[]:
            for dic in List:
                for id_, items in dic.items():
                    if str(id_)== str(id):
                        items[1] = "Completed"
            with open('todo.txt', 'w') as f:
                for dic in List:
                    f.write(str(dic) + '\n')

    def CompletedList(self):
        List = self.fileReader.readFromFile()
        completedList = []
        if List != []:
            for dic in List:
                for id, items in dic.items():
                    if items[1] == "Completed":
                        completedList.append(dic)
            return completedList
    def PendingList(self):
        List = self.fileReader.readFromFile()
        pendingList = []
        if List != []:
            for dic in List:
                for id, items in dic.items():
                    if items[1] == "Pending":
                        pendingList.append(dic)
            return pendingList
    
def showTodo(obj):
    List = obj.readTodo()
    try:
        for dic in List:
            for id, items in dic.items():
                print(f"ID: {id}  ||{items[0]}||  STATUS: {items[1]}")
    except AttributeError as e:
        print("NO ITEM YET...")

def add(obj):
    topic = input("Enter: ")
    with open('idTrackForTodo', 'r') as f:
        id = f.read()
        id = int(id)+1
    with open('idTrackForTodo', 'w') as f:
        f.write(str(id))
    try:
        obj.AddTodo(topic, id)
        print("Added Successfully")
        input()
    except:
        print("Some Error Occurs")
        input()

def Completed(obj):
    List = obj.CompletedList()

    if List==[]:
        print("NO TASK IS COMPLETED YET")
    else:
        for dic in List:
            for id, items in dic.items():
                print(f"ID: {id}  ||{items[0]}||  STATUS: {items[1]}")
    input()


def Pending(obj):
    List = obj.PendingList()

    if List == []:
        print("NO TASK IS PENDING")
    else:
        for dic in List:
            for id, items in dic.items():
                print(f"ID: {id}  ||{items[0]}||  STATUS: {items[1]}")
    input()

def delete(obj):
    showTodo(obj)
    while True:
        id = input("Enter According To The Id: ")
        if id != "":
            break
        else:
            print("Invalid Input")
    try:
        obj.Delete(id)
        print("Successfully Deleted!")
    except:
        print("Some Error Occurs! ")
    input()

def mark(obj):
    showTodo(obj)

    id = input("Enter According To The Id: ")
    try:
        obj.MarkAsCompleted(id)
        print("Successfully Marked!")
    except:
        print("Some Error Occurs! ")
    input()



if __name__ == "__main__":
    obj = Todo()
    while True:
        os.system('cls')
        print("1. Add Todo")
        print("2. Show Todo")
        print("3. Completed Todo")
        print("4. Pending Todo")
        print("5. Delete Todo")
        print("6. Mark As Completed")
        print("7. Quit")

        option = int(input("Enter: "))

        if option == 1:
            os.system('cls')
            add(obj)
        elif option == 2:
            os.system('cls')
            showTodo(obj)
            input()
        elif option == 3:
            os.system('cls')
            Completed(obj)
        elif option == 4:
            os.system('cls')
            Pending(obj)
        elif option == 5:
            os.system('cls')
            delete(obj)
        elif option == 6:
            os.system('cls')
            mark(obj)
        elif option == 7:
            os.system('cls')
            print("Closing....")
            time.sleep(2)
            break
