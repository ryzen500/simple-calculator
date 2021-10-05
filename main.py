#Program simple calculator

#this function add two numbers 
def add(x,y):
  return x+y

#this function substract two numbers
def substract(x,y):
  return x-y


#this function multiply two numbers 
def multiply(x,y):
  return x*y


#this function divides two numbers 
def divide(x,y):
  return x/y

print("Select operation")
print("1.Add")
print("2.Substract")
print("3.multiply")
print("4.divide")

while True:
  #take input from User 
  choice = input("Enter Choice(1/2/3/4): ")

  #check if choice is one of the four options 
  if choice in ('1','2','3','4'):
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter second Number: "))

    if choice  == '1':
      print(num1, "+",num2, "=", add(num1,num2))
    
    elif choice =='2':
      print(num1,"-",num2,"=",substract(num1,num2))
    
    elif choice =='3':
      print(num1,"-",num2,"=",multiply(num1,num2))


    elif choice =='4':
      print(num1,"/",num2,"=",divide(num1,num2))

      #check if user wants another calculation
      #break the  while loops if answers is no
      next_calculation = input("Let's do calculation again ? (yes/no): ")
      if next_calculation =="no":
        break
  else:
    print("invalid Input")   
   