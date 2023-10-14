import os


class FileSaver:
    def saveToFile(self, object):
        with open('newContact.txt', 'a') as f:
            fr = f.write(object + '\n')




class FileReader:
    def readFromFile(self):
        with open('newContact.txt', 'r') as f:
            f.seek(0)
            fr = f.read().split('\n')
            l = []
            for i in fr:
                try:
                    data = eval(i)
                    l.append(data)
                except SyntaxError:
                    pass
        return l


class Contact:
    def __init__(self):
        self.info = {}

    def AddContact(self,id, name, address, email, phone):
        self.info = {id:[name, phone, email, address]}
        try:
            self.save_to_file()
        except Exception as e:
            print(e)
        else:
            print("Successfully Added")



    def save_to_file(self):
        fs = FileSaver()
        fs.saveToFile(str(self.info))

    def ViewContact(self):
        fr = FileReader()
        frList = fr.readFromFile()
        for dic in frList:
            for key, List in dic.items():
                print(f"id:{key}   NAME:{List[0]}  PHONENUMBER:{List[1]}  EMAIL:{List[2]}  ADDRESS:{List[3]}")

    def searchContactViaName(self, name):
        fr = FileReader()
        frList = fr.readFromFile()
        l = []
        for dic in frList:
            for key, List in dic.items():
                if List[0] == name:
                    l.append(dic)

        if l != []:
            for dic in l:
                for key, List in dic.items():
                    print(f"id{key}  NAME:{List[0]}  PHONENUMBER:{List[1]}  EMAIL:{List[2]}  ADDRESS:{List[3]}")
        else:
            print("Not Found")

    def searchContactViaPhoneNumber(self, phone):
        fr = FileReader()
        frList = fr.readFromFile()
        l = []
        for dic in frList:
            for key, List in dic.items():
                if phone == List[1]:
                    print('yes')
                    l.append(dic)
        if l != []:
            for dic in l:
                for key, List in dic.items():
                    print(f"id{key}  NAME:{List[0]}  PHONENUMBER:{List[1]}  EMAIL:{List[2]}  ADDRESS:{List[3]}")
        else:
            print("Not Found")

    def UpdateContact(self, id):
        fr = FileReader()
        frList = fr.readFromFile()
        option = input("1. Name\n2. PhoneNumber\n3. Email\n4. Address\n\nCHOOSE:  ")
        if int(option) == 1:
            newName = input("Enter New Name: ")
            for dic in frList:
                for key, List in dic.items():
                    if key == id:
                        List[0] = newName
        elif int(option) == 2:
            newPhoneNumber = input("Enter New Phone Number: ")
            for dic in frList:
                for key, List in dic.items():
                    if key == id:
                        List[1] = newPhoneNumber
        elif int(option) == 3:
            newEmail = input("Enter New Email: ")
            for dic in frList:
                for key, List in dic.items():
                    if key == id:
                        List[2] = newEmail
        elif int(option) == 4:
            Address = input("Enter New Address: ")
            for dic in frList:
                for key, List in dic.items():
                    if key == id:
                        List[3] = Address
        try:
            with open('newContact.txt', 'w') as f:
                for dic in frList:
                    f.write(str(dic) + '\n')
        except Exception as e:
            print(e)
        else:
            print("Successfully Updated a Phone Number At Id",id)

    def DeleteContact(self, id):
        fr = FileReader()
        frList = fr.readFromFile()
        try:
            for dic in frList:
                for key, List in dic.items():
                    if id == key:
                        frList.remove(dic)

            with open('newContact.txt', 'w') as f:
                for dic in frList:
                    f.write(str(dic) + '\n')
            print("Successfully Deleted")
        except Exception as e:
            print(e)
def AddtoContact(obj):
    os.system('cls')
    while True:
        try:

            name = input("Enter Name: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            with open('idtrack.txt', 'r') as f:
                id = eval(f.read())
                id += 1
                obj.AddContact(id, name, address, email, phone)
            with open('idTrack.txt', "w") as f1:
                f1.write(str(id))
                input()
            break
        except IndexError as e:
            print("Please Enter Complete Information\n\n")
            input()

def Update(obj):
    os.system('cls')
    obj.ViewContact()
    print()
    contact = int(input("Choose Phone Number By Its Id: "))
    obj.UpdateContact(contact)
    input()

def Delete(obj):
    os.system('cls')
    obj.ViewContact()
    print()
    contact = int(input("Choose Phone Number To delete: "))
    obj.DeleteContact(contact)
    input()

def Search(obj):

    while True:
        os.system(('cls'))
        print("1. Search Via Name")
        print("2. Search Via Phone Number")
        print("3. Back")
        choice = int(input("Enter: "))
        if choice == 1:
            name = input("Enter Name: ")
            obj.searchContactViaName(name)
            input()
        elif choice == 2:
            number = input("Enter Number: ")
            obj.searchContactViaPhoneNumber(number)
            input()
        elif choice == 3:
            break
        else:
            print("Invalid Input")
            input()

def View(obj):
    os.system('cls')
    obj.ViewContact()
    input()
if __name__ == "__main__":

    obj = Contact()



    while True:
        os.system('cls')
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. View Contact")
        print("6. Quit")
        choice = int(input("Enter: "))
        if choice == 1:
            AddtoContact(obj)
        elif choice == 2:
            Update(obj)
        elif choice == 3:
            Delete(obj)
        elif choice == 4:
            Search(obj)
        elif choice == 5:
            View(obj)
        elif choice == 6:
            break
        else:
            print("Invalid Input")




