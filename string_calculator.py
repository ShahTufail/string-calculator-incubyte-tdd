import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ",|\n"
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            delimiter = re.escape(header[2:])

        parts = re.split(delimiter, numbers)
        nums = [int(p) for p in parts if p]

        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(nums)