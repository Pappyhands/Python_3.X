def userInt(prompt):
    print(prompt)
    num = int(input())

    return num

def userFloat(prompt):
    print(prompt)
    f = float(input())

    return f

def userString(prompt):
    print(prompt)
    s= input()
    return s

def userList(prompt):
    print(prompt)
    l = input().split(",")
    return l

def kmToMi(km):
    return 0.62 * km
