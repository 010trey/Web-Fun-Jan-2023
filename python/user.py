#slippin' PMm — Yesterday at 2:31 PM

class User:
    def init(self,name,lastname,email,age):
        self.first_name =name
        self.last_name =lastname
        self.email=email
        self.age = age
        self.rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print("first name",self.first_name)
        print("last name",self.last_name)
        print(" email",self.email)
        print("age",self.age)
        print("rewards member",self.rewards_member)
        print("gold card points",self.gold_card_points)
    def enroll(self):
        self.rewards_member=True
        self.gold_card_points=200
    def spend_points(self, amount) :
        self.gold_card_points= self.gold_card_points - amount

amine=User("amine","hahaha","test@gmail.com",20)
aziz=User("aziz","hhihihi","aaaa@gmm.tn",66)
amine.display_info()
amine.enroll()
amine.display_info()
amine.spend_points(50)
amine.display_info()
aziz.enroll()
aziz.spend_points(80)