class PaymentMethod:
    def __init__(self, amount):
        self.amount = amount 
    def pay(self):
        print(f"Paying {self.amount} using a generic payment method.")
class Creditcard(PaymentMethod):
    def pay(self,amount):
        super().__init__(amount)
        print(f"Paying {self.amount} via Credit Card, adding 2% processing fee")
class Cash(PaymentMethod):
    pass 

p1=[Creditcard(1000), Cash(2000)]
for PaymentMethod in p1:
    p1.pay()


        