class chair:
    def __init__(self, weight = 2, legs = 4, endurance = 10):
        self.weight = weight
        self.legs = legs
        self.endurance = endurance
    def __str__(self):
        return f"chair(weight = {self.weight}, legs = {self.legs}, endurance = {self.endurance}.)"
    def __repr__(self):
        return f"chair(weight = {self.weight}, legs = {self.legs}, endurance = {self.endurance}.)"
a = chair()
print(a)