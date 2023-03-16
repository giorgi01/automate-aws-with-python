class ArmstrongNumsGenerator:

    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to

    def generate(self):
        for num in range(self.from_, self.to):
            symbols_count = len(str(num))
            digit_sum = sum(int(digit) ** symbols_count for digit in str(num))
            if num == digit_sum:
                yield num
