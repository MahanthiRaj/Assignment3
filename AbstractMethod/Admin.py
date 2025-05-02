from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def login(self):
        pass

    def logout(self):
        return "User logged out"

class AdminUser(User):
    def login(self):
        return "Admin logged in"

admin = AdminUser()
print(admin.login())
print(admin.logout())
