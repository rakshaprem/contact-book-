#Menu funtion
def display_menu():
    print("1.) Add the contact")
    print("2.) view the contact")
    print("3.) Search the contact")
    print("4.) Delete the contact")
    print("5.) Exit the application,bye:)")


#add contacts function
def add_contacts(contacts):
    name = input("enter the name of the contact to be added:")
    phone = input("enter the mobile number:")
    contacts[name] = phone
    print("the contact",name," is added")

#view contacts function
def view_contacts(contacts):
    name = input("enter a contact name")
    if name not in contacts:
        print("your contact is not found:(")
    else:
        for name,phone in contacts.items():
            print("name:",name," ","phone:",phone)

#search contacts function            
def search_contacts(contacts):
    name = input("enter the contact to be searched")
    if name in contacts:
        for name,phone in contacts.items():
            print("name:",name,"phone:",phone)
    else:
        print("your contact is not found:(")

#delete contact function
def delete_contacts(contacts):
    name = input("enter a contact to be deleted")
    if name in contacts:
        del contacts[name]
        print("your contact is deleted ")
    else:
        print("your contact is not found")

#function that contains all the funtion calling statements

def contact_book():
    contacts = {}

    while True:
        display_menu()
        choice = input("enter your choice")
        if(choice=='1'):
            add_contacts(contacts)
        elif(choice=='2'):
            view_contacts(contacts)
        elif(choice=='3'):
            search_contacts(contacts)
        elif(choice=='4'):
            delete_contacts(contacts)
        elif(choice=='5'):
            print(" you preffered to exit the application, thank you!")
            
        else:
            print("invalid choice ")
            break
#main function
contact_book()            
            




        
