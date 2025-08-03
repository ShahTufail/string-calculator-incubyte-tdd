import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        parts = re.split(",|\n", numbers)
        return sum(int(p) for p in parts)