def add_item(item_list) :
    print("Adding item... ")
    productName = input("Enter product Name : ")
    if productName in item_list :
        print("Item is already in the list")
    else :
        item_list.append(productName)
    
def change_item(item_list) :
    print("Changing item... ")
    productName = input("Enter product Name : ")
    if productName not in item_list :
        print("Item is not in the list")
    else :
        newName = input('Enter new name: ')
        item_list[item_list.index(productName)] = newName
        print("Item has been changed")
    
def insert_item(item_list) :
    print("Inserting item... ")
    productName = input("Enter product Name: ")
    index = input("Enter index to insert into list: ")
    item_list.insert(int(index),productName)
    # item_list.insert(productName,int(index))
    print("Item has been inserted")

def remove_item(item_list) :
    print("Removing item... ")
    productName = input("Enter product Name: ")
    if productName in item_list :
        item_list.remove(productName)
        print("Item has been removed")
    else :
        print("This item is not in the list")

def show_item(item_list) :
    print("Showing item... ")
    if len(item_list) == 0 :
        print("The list is currently empty")
    else :
        for item in item_list :
            print(item)
    
print("What would you like to do?")
print("1: add item")
print("2: change item")
print("3: insert item")
print("4: remove item")
print("5: show items")
print("6: exit")

x = []
choose = input('Enter a number : ')
while choose != "6" :
    if choose == "1" :
        add_item(x)
    elif choose == "2" :
        change_item(x)
    elif choose == "3" :
        insert_item(x)
    elif choose == "4" :
        remove_item(x)
    elif choose == "5" :
        show_item(x)
    print()
    choose = input("Enter a number : ")