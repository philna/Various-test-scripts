class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """
#Create constructor
    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

    def getBalance(self):
        """Return the balance amount
        """
        return self.balance


#Create customer object names Phil
Phil = Customer("Phil",5000.00)

#Get the current balance
print (Phil.getBalance())

#Deposit money and show new balance
print (Phil.deposit(50.0))

#Get the current balance
print (Phil.getBalance())




