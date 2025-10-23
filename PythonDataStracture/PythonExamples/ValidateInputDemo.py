# ValidateInputDemo.py
#Simple validator function for dicts

def validate_person(p):
    return isinstance(p.get("name"), str) and isinstance(p.get("age"), int)

if __name__ == '__main__':
    print(validate_person({"name":"Tom","age":30}))
    print(validate_person({"name":"Tom","age":"30"}))