from Todo import Todo
from Users import User

def Main():
    TodoItems = Todo.ListOfTodoItems("https://jsonplaceholder.typicode.com/todos")
    UserItems = User.ListOfUsers("https://jsonplaceholder.typicode.com/users")

    #condition one is greater than 50%
    userIdscondn1 = Todo.GetUsersWithMoreThan50Completion(TodoItems)
    
    #condition two is - it is a user from FanCode City
    userIdscondn2 = User.ListofFancodeUsers(UserItems)

    #Dictionary of Names and Ids of satisfying users
    userIdscondn1and2 = {}

    for x in userIdscondn1:
        if x in userIdscondn2.keys():
            userIdscondn1and2[x] = userIdscondn2[x]

    #return userIdscondn1and2
    print(userIdscondn1and2)

Main()


