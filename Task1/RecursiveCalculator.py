class RecursiveCalculator:

    @staticmethod
    def recursive_sum(numbers):
        if len(numbers) == 1:
            return numbers[0]
        else:
            return numbers[0] + RecursiveCalculator.recursive_sum(numbers[1:])
