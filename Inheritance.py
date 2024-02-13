class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number =phone_number
    def send_money(self,amount,recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES Sent to {recipient} successfully")
        else:
            print("insufficient balance")

class Personal_Mpesa(Mpesa):
    def __init__(self,account_balance,phone_number,id_number):
        super().__init__(account_balance,phone_number)
        self.id_number = id_number
    def buyairtime(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES airtime bought successfully")
        else:
            print("insufficient balance")

class Business_Mpesa(Mpesa):
    def __init__(self,account_balance,phone_number,business_name):
        super().__init__(account_balance,phone_number)
        self.business_name = business_name
    def receive_money(self,amount):
            self.account_balance += amount
            print(f"{amount} KES received successfully")
personal=Personal_Mpesa(500,794594539,4253789)
personal. send_money(400,78934643)
personal.buyairtime(25)

business=Business_Mpesa(4566,78999999,"housing")
business.receive_money(2000)
business.send_money(500,794594539)