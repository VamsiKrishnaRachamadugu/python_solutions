"""3.Design and implement a Money class that stores monetary values in dollars and cents.
Special method init should have the following function header, def init(self, dollars, cents)
Include special method repr (str) for displaying values in dollars and cents: $ 0.45, $ 1.00, $ 1.25.
Also include special method add, and three getter methods that each provide the monetary value in another
currency. Choose any three currencies to convert to.

"""


class Money:
    cent = 1
    dollar = cent * 100

    def init(self, dollars, cents):
        self.cent = cents
        self.dollar = dollars

    def __repr__(self):
        print(self.dollar)
        print(self.cent)
