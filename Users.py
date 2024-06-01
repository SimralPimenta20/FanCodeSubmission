import requests
import json

class Geo:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
    
class Address:
    def __init__(self, street, suite, city, zipcode, geo):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        if type(geo) == Geo:
            self.geo = geo

class Company:
    def __init__(self, name, catchPhrase, bs):
        self.name = name
        self.catchPhrase = catchPhrase
        self.bs = bs

class User:
    def __init__(self, id, name, username, email, address, phone, website, company):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        if type(address) == Address:
            self.address = address
        self.phone = phone
        self.website = website
        if type(company) == Company:
            self.company = company
    
    @staticmethod
    def ListOfUsers(url):
        response = None
        try:
            response = requests.get(url)
        except:
            print("Could not access Users URL!")
            return []
        
        data = None
        try:
            data = json.loads(response.text)
        except:
            print("Could not access data in Users URL!")

        UserItems = []
        for item in data:
            geo = Geo(
                lat = item["address"]["geo"]["lat"],
                lng = item["address"]["geo"]["lng"]
            )
            address = Address(
                street = item["address"]["street"],
                suite = item["address"]["suite"],
                city = item["address"]["city"],
                zipcode = item["address"]["zipcode"],
                geo = geo                
            )
            company = Company(
                name = item["company"]["name"],
                catchPhrase = item["company"]["catchPhrase"],
                bs = item["company"]["bs"]
            )

            user = User(
                id = item["id"],
                name = item["name"],
                username = item["username"],
                email = item["email"],
                address = address,
                phone = item["phone"],
                website = item["website"],
                company = company
            )
            UserItems.append(user)
        return UserItems

    @staticmethod
    def ListofFancodeUsers(UserItems):
        FancodeUsers = {}
        for item in UserItems:
            lat = float(item.address.geo.lat)
            lng = float(item.address.geo.lng)
            if((float(lat) > -40.00 and float(lat) < 5.00) and (float(lng) > 5.00 and float(lng) < 100.00)):
                FancodeUsers[item.id] = item.name
        return FancodeUsers
