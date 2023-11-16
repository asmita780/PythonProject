 
import json
a=input("login_or_sig up  ")
if a=="login":

    username=input("enter username  ")

    # if username in userdetails['username'] :

    #     p=input("enter pas sword  ")

    #     if p in userdetails:
    #             print("suss")
                                                             
    #     else:
    #             print("password id wrong")
    # else:
    #     print("email is not exist")

else:
    if a=="singup":
            userdetails={}
            list=[]
            dict1={}
            # dict1={}
            
            dict1["username"]=input("enter username ")
            dict1["passwort"]=input("enter password, passwort must have at least one spacel charecter  ")
            if "@" in dict1["passwort"] or "#" in dict1["passwort"]:
                dict1["passwort2"]=input("enter passwort again  ")
                if dict1["passwort2"] == dict1["passwort"]:
                    list.append(dict1)
                    userdetails['user']+=list
                    print("submit")



                    filename = 'userdetails.json'

                    with open(filename, 'w') as file_object:

                        json.dump(userdetails, file_object)
                    
    
                else:
                    print("both passwort are not same ")
                    print("try again ")
            else:
                print("ERROR: at least passwort shoud contain one spacle character ")
                print("try again ")
        


d = {0: 'Alice', 1: 'Bob'}

dicts = [{**d} for _ in range(3)]
print(dicts)
[{0: 'Alice', 1: 'Bob'}, {0: 'Alice', 1: 'Bob'}, {0: 'Alice', 1: 'Bob'}]


# d=[x for x in range(10)]
# print(d)
