from flask_restful import Resource

class User(Resource):
    """This is the class that defines all behaviours in a user

    Args:
        Resource ([type]): [description]
    """
    users = {}
    def __init__(self,username,department,email,password):
        """This will define all properties of a user
        """
        self.id = len(User.users)+1
        self.username = username
        self.department = department
        self.email = email
        self.password = password

    def save_user(self):
        """This will add a newly created user to the users array
        """
        new_user = dict(
            id = self.id,
            username = self.username,
            department = self.department,
            email = self.email,
            password = self.password
        )

        self.users.update({
            self.id: new_user
        })
        