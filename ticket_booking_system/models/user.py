class User:
    def __init__(self, user_id, name, is_vip=False):
        self.user_id = user_id
        self.name = name
        self.is_vip = is_vip

    def __repr__(self):
        return f"{self.name} (VIP={self.is_vip})"
