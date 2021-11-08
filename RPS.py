import random
from random import choice
class game :

    def __init__ (self) :
        self.M = 0
        self.A = 0
        C = ["rock", "paper", "scissors"]
        self.d = random.choice(C)

    def takev(self):
        self.m = input()

    def choice(self):
        print("your choice = ", self.m)
        print("machine choice = ", self.d)

    def process(self):
            if self.m == self.d:
                self.M = self.M
            elif self.m == "rock":
                if self.d == "scissors":
                    self.M += 1
                else:
                    self.A += 1
            elif self.m == "scissors":
                self.M = self.M
                if self.d == "paper":
                    self.M += 1
                else:
                    self.A += 1
            elif self.m == "paper":
                self.M = self.M
                if self.d == "rock":
                    self.M += 1
                else:
                    self.A += 1

    def score(self):
        print("Man = ", self.M)
        print("Machine = ", self.A)







p = game()
for x in range(10):
    p.takev()
    p.choice()
    p.process()
    p.score()
