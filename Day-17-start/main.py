###Create a class and object for it
#class User:
#    print("Hello user")

###Create a object from the class
#user_1 = User()

###Creting an attrubute from the class
###Attribute is the varaible associated with the class
#user_1.user_name = "angela"
#user_1.id = "001"
#print(user_1.user_name)

###Constructor and __init__() function
class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.follower =0
        self.following =0

    def follow(self, user):
        user.follower +=1
        user.following +=1

users1 =  User("10","aish")
users2 = User("11","Angela")
users1.follow(users2)
print(f"Follower before {users2.follower}")
print(f"Follower after {users2.following}")


