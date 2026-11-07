print("========[WELCOME TO FILE MANGEMENT APP]===========")
import os
def  create_file(filename):
    try:
        with open(filename,"x") as f:                          #crete a file
            print(f"File name {filename}: created sucessfully")
    except FileExistsError:
        print(f"File name {filename} alredy exists")
    except Exception as E:                           #koi bhi error ahyega
        print("an error is occuried")
    
def view_all_file():
    files = os.listdir()
    if not files:
        print("No files")
    else:
        print("view file sucessfully")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has delted sucessfully!")
    except FileNotFoundError:
        print("file not exist")
    except Exception as E:
        print("An error is occuried")

def read_file(filename):
    try:
        with open(filename,"r") as f:
            content = f.read()
            print(f'content of "{filename}" : \n {content}')
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except Exception as E:
        print("An error is ocuried")
    
def edit_file(filename):
    try:
        with open("sample.txt","a") as f:
            content = input("enter the data to add: ")
            f.write(content + "\n")
            print(f"content added to {filename} sucessfully")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except Exception as E:
        print("An error is occuried")

def main():
    while True:
        print("File management app")
        print("1.Create a file")
        print("2.view all file")
        print("3.Delete a file")
        print("4. Read  a file")
        print("5. edit  a file")
        print("6. Exit  app")

        choice = input("Enter the choice 1-6: ")
        
        if choice =="1":
            filename = input("Enter the file name to create: ")
            create_file(filename)

        elif choice=="2":
            view_all_file()

        elif choice=="3":
            filenamme = input("Enter the file name: ")
            delete_file(filename)
        
        elif choice=="4":
            filename = input("Enter the file name: ")
            read_file(filename)
        
        elif choice=="5":
            filename = input("Enter the file name: ")
            edit_file(filename)

        elif choice=="6":
            print("Closing the app")
            break

        else:
            print("Invalid syntax ")

if __name__ == "__main__":
    main()
    