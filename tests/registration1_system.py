class Registration1System:
    def __init__(self):
        self.users = {}

    def register(self, param):
        pass


def register(self, fname, lname, email):
    if email in self.users:
        return "Error: The email address you have entered is being used."

    self.users[email] = {'name': fname, 'name': lname, 'email': email}
    return "User successfully registered"


system = Registration1System()
print(system.register("Tj", "Gold", "cinnamo04@gmail.com"))