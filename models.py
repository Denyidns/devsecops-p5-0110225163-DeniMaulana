class UserManager:
    def __init__(self):
        self.users = [
            {"id": 1, "name": "Admin DevSecOps", "role": "admin"},
            {"id": 2, "name": "Developer 1", "role": "user"}
        ]

    def get_all_users(self):
        return {"count": len(self.users), "users": self.users}