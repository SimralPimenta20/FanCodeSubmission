from Todo import Todo
from Users import User

def Main():
    TodoItems = Todo.ListOfTodoItems("https://jsonplaceholder.typicode.com/todos")
    UserItems = User.ListOfUsers("https://jsonplaceholder.typicode.com/users")

    #condition one is greater than 50%
    userIdscondn1 = Todo.GetUsersWithMoreThan50Completion(TodoItems)
    
    #print(userIdscondn1)

    ##userIdscondn1and2 = []
    ##for user in UserItems:
        ##if user.address.geo.LocationFancode():
            ##userIdscondn1and2.append(user.id)
    #return userIdscondn1and2
    ##print(userIdscondn1and2)
    

    #new Code
    userIdscondn2 = User.ListofFancodeUsers(UserItems)

    userIdscondn1and2 = []

    for x in userIdscondn1:
        if x in userIdscondn2:
            userIdscondn1and2.append(x)

    #return userIdscondn1and2
    print(userIdscondn1and2)
Main()


