#Bank project

class user():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def showdetails(self):
        print("Personal details:")
        print(f"Name: {self.name.title()}")  # Correctly applying title() to the name
        print(f"Age: {self.age}")  # No need for title() for age since it's an integer
        print(f"Gender: {self.gender.title()}")  # Correctly applying title() to the gender

class bank(user):
    __balance=0
    __usercount=0
    
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        bank.__usercount+=1
        self.__accountno=f"bankaccount0005bank.__usercount"
    def deposite(self,amount):
        self.amount=amount
        self.__balance+=self.amount
        print(f"account balance has been updated. RS{self.__balance}")
        
    def withdraw(self,amount):
        self.amount=amount
        if(self.amount>self.__balance):
            print(f"insufficient balance available Rs.{self.__balance}")
        elif(100<=self.amount<=self.__balance):
            print(f"Thank you for visit")
            self.__balance-=self.amount
            print(f"current balance is :- Rs {self.__balance}")
        else:
            print(f"you cannot withdraw less then Rs 1000")
    
    def viewbalance(self):
        self.showdetails()
        print(f"account no :-{self.__accountno}")
        print(f"current balance is Rs{self.__balance}")
    
    def transfer(self,username,amount):
        
        self.amount=amount
        if(self.amount>self.__balance):
            print(f"insufficient amount available of Rs{self.__balance}")
        elif(1<=self.amount<=self.__balance):
            username.__balance+=self.amount
            self.__balance-=self.amount
            print("amount transfer succesfully")
            print(f"current balance is :- Rs{self.__balance}")
        else:
            print("you can not transfer less the amt.rs 1")


