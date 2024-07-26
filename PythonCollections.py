#Lists

testingList_String = ["Lukas", "Adam", "Radim", "Michal", "Marek"]

#Get last list item
print(testingList_String[-1])


#Check if "name" is present in the list:
def check_list():
    name = input("Enter name to check if it's in list: ")
    if name in testingList_String:
        print("Yes, {} is in the list".format(name))
    else:
        print("No, {} is not in the list".format(name))


#Add to list
testingList_String.append("Martin")
print(testingList_String)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
#Clear the list
thislist.clear()
print(thislist)


def myfunc(n):
    return abs(n - 50)


newList = [100, 50, 65, 82, 23]
newList.sort(key=myfunc)
print(newList)
