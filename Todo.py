import requests
import json

class Todo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

    @staticmethod
    def ListOfTodoItems(url):
        
        response = None
        try:
            response = requests.get(url)
        except:
            print("Could not access the Todo URL!")
            return []
        
        data = None
        try:
            data = json.loads(response.text)
        except:
            print("COuld not access the data in Todo URL!")
            return []
        
        TodoItems = []

        for item in data:
            TodoObject = Todo(
                userId = item["userId"],#Json data is accessed using brackets not "." notation
                id = item["id"],
                title = item["title"],
                completed = item["completed"]
            )
            TodoItems.append(TodoObject)
         
        return TodoItems #we return the list
    
    @staticmethod
    def GetUsersWithMoreThan50Completion(TodoItems):

        data = {}

        for item in TodoItems:
            if not type(item) == Todo:
                break
         #   When you are changing the values in a dictionary go about like this use curly braces and attribute name inside it
         #   On the other hand hen you  are accessing the value in the  dictionary you can use the method similar to accessing a 2D Array
            if item.userId in data.keys():
                data[item.userId] = { 
                    "total": data[item.userId]["total"] + 1,
                    "completed": data[item.userId]["completed"] + (1 if item.completed == True else 0)
                    }
            else:
                data[item.userId] = { 
                    "total": 1,
                    "completed": (1 if item.completed == True else 0)
                    }
                
        MoreThan50PercentCompletedUsers = []

        for user in data.keys():
            if data[user]["completed"]/data[user]["total"] > 0.5:
                MoreThan50PercentCompletedUsers.append(user)
        
        return MoreThan50PercentCompletedUsers

