
import random

class CustomRandomGenerator:
    def __init__(self):
        self.generated_numbers = []

    def generate_number(self, start, end):
        number = random.randint(start, end)
        self.generated_numbers.append(number)
        return number

    def show_history(self):
        return self.generated_numbers

generator = CustomRandomGenerator()

print("Random Number:", generator.generate_number(1, 100))
print("History:", generator.show_history())
