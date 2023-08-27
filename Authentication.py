class User:
    
    admins=["Roger"]
    normalUsers=["John", "Joe", "Toby"]
    beginners=["Aaron"]
    
    def list_user():
        string1 = "admins:\t"
        for user in User.admins:
            string1 += "\t" + user
        print(string1)
        string2 = "normal_users:"
        for user in User.normalUsers:
            string2 += "\t" + user
        print(string2)
        string3 = "beginners:"
        for user in User.beginners:
            string3 += "\t" + user
        print(string3)
        
    def return_users():
        return User.admins, User.normalUsers, User.beginners
    def add1(list1, name):
        list1.append(name)
    def addUser(list_name,name):
        if list_name == "admins":
            User.add1(admins, name)
            print("Updated admins List")
            print(admins)
        elif list_name == "normal_users":
            User.add1(normalUsers, name)
            print("Updated normal user List")
            print(normalUsers)
        elif list_name == "beginners":
            print("Updated beginners List")
            User.add1(beginners, name)
            print(beginners)
        else:
            print("Invalid list name. Please select admins, normal_users, or beginners.")
    def remove1(list1, name):
        try:
            list1.remove(name)
        except:
            print("Name not found.")
    
    def removeUser(list_name,name):
        if list_name == "admins":
            User.remove1(admins, name)
            print("Updated admins List")
            print(admins)
        elif list_name == "normal_users":
            User.remove1(normalUsers, name)
            print("Updated normal user List")
            print(normalUsers)
        elif list_name == "beginners":
            print("Updated beginners List")
            User.remove1(beginners, name)
            print(beginners)
        else:
            print("Invalid list name. Please select admins, normal_users, or beginners.")

a = User.return_users()
admins = a[0]
normalUsers = a[1]
beginners = a[2]

if __name__ == "__main__":
    User.list_user()
    a = User.return_users()
    print(a[2])
    admins = a[0]
    normalUsers = a[1]
    beginners = a[2]
    
    for user in admins:
        print(user)
    User.addUser("beginners","Mihail")
    User.removeUser("beginners","re")
    #User.addUser("normal_users","Toby")

    
