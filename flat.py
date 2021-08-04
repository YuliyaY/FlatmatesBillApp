class Bill:
    """
    Object containing data about bill: total bill amount and a period of a bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        to_pay = round(bill.amount / (self.days_in_house + flatmate2.days_in_house)
                       * self.days_in_house, 2)
        return to_pay