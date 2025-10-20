# JSONLikeDicts.py
# Work with nested dicts resembling JSON.

data = {"user": {"name": "Sam", "roles": ["admin","user"]}, "active": True}

def has_role(d, role):
    return role in d.get("user", {}).get("roles", [])

if __name__ == '__main__':
    print("Is admin?", has_role(data, "admin"))
    print("Is moderator?", has_role(data, "moderator"))