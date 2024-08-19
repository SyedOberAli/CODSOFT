# num=int(input("enter num:"))

# if(num%2==10):
#     print("num is even")

# else:
#     print("num is odd") 

# x = int(input("enter first num:"))
# y = int(input("enter second num:"))
# z = int(input("enter third num:"))

# if(x>=y and x>=z):
#     print("first num is greatest:",x)
# elif(y>=z):
#     print("second num is greatest:",y)
# else:
#     print("third num is greatest:",z)      

# a = int(input("enter first num:"))
# b = int(input("enter second num:"))
# c = int(input("enter third num:"))
# d = int(input("enter fourth num:"))

# if(a>=b and a>=c and a>=d):
#     print("first num is greatest:",a)
# elif(b>=c and b>=d):
#     print("second num is greatest:",b)
# elif(c>=d):
#     print("third num is greatest:",c) 
# else:
#     print("third num is greatest:",d)

# i = 1
# while i<=100000:
#     print("syed ober ali",i)
#     i+=1

# i=5
# while i<=6:
#     print(i)
#     i-=1
# print("program ended")

# list = [1,4,9,16,25,36,49,64,81,100]

# x=36
# i = 0
# while i<len(list):
#     if list[i]==x:
#         print("number found",x,"at idx",i)
#     i+=1 


# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# n = int(input("enter number:"))

# i=1
# while (i<=10):
#     print(n*i)
#     i+=1

# count = 0
# while (count < 3): 
#     count = count + 1
#     print("Hello Geek")



# age = 28
  
# # the test condition is always True 
# while age > 19: 
#     print('Infinite Loop')
    

# def check_num():

#     num = int(input("enter number:"))    
#     if num%2 == 0:
#         print(num," is even")
#     else: 
#         print(num,"is odd")

# check_num()


# i = 6
# while i>0:
#     i-=1
#     print(i)

# def show(n):
#     if n==0:
#         rerturn
#     print(n)

#     show(n-1)

# show(5)    

# def calc_sum(n):
#     if n==0:
#         return 0
#     return calc_sum(n-1)+n

# sum = calc_sum(6)
# print(sum)    

# movies = ["pk","3 idiots","dangal","jawaan","bajrangibhaijaan"] 
# def print_list(list,idx=0):
#     if idx ==len(list):
#         return
#     print(list[idx])
#     print_list(list,idx+1)   

# print_list(movies)    

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\nusing JAVA.\nI like programming in JAVA")

# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)

#     new_data = data.replace("JAVA","python")
#     print(new_data)
 
# with open("practice.txt","w") as f:
#     f.write(new_data)

# count = 0
# with open("practice.txt","r") as f:
#      data = f.read()
     
#      nums = data.split(",")

#      for val in nums:
#           if int(val)%2 == 0:
#                count+=1

# print(count)

# class Account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def Debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount,"was debited")
#         print("Total balance =",self.balance )

#     def Credit(self,amount):
#         self.balance+=amount
#         print("Rs.",amount,"was credited")
#         print("Total balance:",self.balance )

#     def get_bal(self):
#         return self.balance       

# acc1 = Account(10000,1234)--

# acc1.Debit(5000) 
# acc1.Credit(30000)  
# acc1.Debit(20000) 



# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return ((22/7)*self.radius**2)

#     def perimeter(self):
#         return 2*(22/7)*self.radius
      
# C1 = Circle(30) 
# print(C1.area()) 

# print(C1.perimeter())

# class employee:
#     def __init__(self,dept,role,salary):
#         self.dept = dept
#         self.role = role
#         self.salary = salary

#     def showdetails(self):
#         print("dept:",self.dept)
#         print("role :",self.role)
#         print("salary :",self.salary)

# class Engineer(employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Quality Control","Mechanical Engineer","100000")

# Engg1 = Engineer("Syed Ober Ali","27")
# Engg1.showdetails()
# print("Name :",Engg1.name)
# print("Age :",Engg1.age)

 
n = 1
while n<=5:
    square = n**2
    n=+1
    print(f"{n} - {square}")



