class Theater:
    #Attribute
    theaterName = 'Sader Cronically Unhappy'
 
    
    #constructor
    def __init__(self,title,price) :
        self.title = title
        self.price = price

    #Method
    def hello(self):
        print('hello all clients')

class Customer(Theater):
    #Attribute
    def __init__(self,fullname,age, title, price,seats):
        super().__init__(title, price)
        self.fullname = fullname
        self.age = age
        self.seats = seats
        self.money = 10000
    def buyTicket(self):
        #calculate ticket
        self.total = self.price*self.seats

        #Deduct money from customers
        self.money -= self.total
        
        print(f'clients name : {self.fullname}')
        print(f'age : {self.age}')
        print(f'movie name : {self.title}')
        print(f'buy  : {self.seats} seats total price {self.total}')
        print(f'remaining : {self.money}')
        



# movie01 = Theater('Avengers',150)
# print(movie01.theaterName)
# print(movie01.title)
# print(movie01.price)
# movie01.hello()

# print("============================")

# movie02 = Theater('Justice league',200)
# print(movie02.theaterName)
# print(movie02.title)
# print(movie02.price)
# movie02.hello()
        
custom01 = Customer('metha chankliang',20,'avengers',120,1)
print(custom01.theaterName)
custom01.hello()
custom01.buyTicket()
print('===============================')
custom02 = Customer('chaiwat chompuchan',23,'Justice league',150,2)
print(custom02.theaterName)
custom02.hello()
custom02.buyTicket()
