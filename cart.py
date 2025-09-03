def add_item(item,price):
    li=[item,price]
    cart.append(li)    
    
def bill(li):
    print("items         price")
    total=0
    for i in range(len(li)):
        for j in range(2):
            print(li[i][j],end='')
            
            for k in range(15-len(str(li[i][0]))):
                print(" ",end='')
            if j==1:
                total=total+li[i][1]
        print()
    print("\nYour total Bill is = ",total)
        

def remove_item(li,item):
    for i in range(len(li)):
        if item==li[i][0]:
            ind=i
    li.pop(ind)
    


cart=[]
items=['rice','dal','milk','tamatos','potatos','brinjal','cabbage']
price=[70,80,60,30,25,40,30]
while(True):
    print("\nEnter (1) to add items\nenter (2) to remove item\nEnter (3) to check bill\nenter (4) to checkout or exit\n")
    choice=int(input("\nEnter your choice: "))
    if choice==1:
        ind=0
        print("all are rates for 1 kgs and 1 lit")
        print("\nrice = 70 rs , dal = 80 rs , milk = 60 rs , tamatos = 30 rs \npotatos = 25 rs , brinjal = 40 rs , cabbage = 30 rs\n")
        item=input("enter your item: ")
        quant=int(input("enter quantity: "))
        for i in range(len(items)):
            if items[i]==item:
                ind=i
        if ind!=None:
            amo=price[ind]*quant
            
            add_item(item,amo)
        else:
            print("Your item is not found")
            


    elif choice==2:
        item=input("Enter item to remove: ")
        remove_item(cart,item)


    elif choice==3:
        print("Your bill is: ")
        bill(cart)


    elif choice==4:
        break
