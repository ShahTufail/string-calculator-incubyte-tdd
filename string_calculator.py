import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        # Check for empty string
        if not numbers:
            return 0

        delimiters = [",", "\n"]
        num_section = numbers

        # Handling custom delimiters
        if numbers.startswith("//"):
            delimiter_section, num_section = numbers.split("\n", 1)
            custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_section)
            if custom_delimiters:
                delimiters = [re.escape(d) for d in custom_delimiters]
            else:
                delimiters = [re.escape(delimiter_section[2:])]

        # regex pattern for splitting
        pattern = "|".join(delimiters)
        parts = re.split(pattern, num_section)

        # Converting to integers and filter
        nums = []
        negatives = []
        for p in parts:
            if p:
                n = int(p)
                if n < 0:
                    negatives.append(n)
                elif n <= 1000:
                    nums.append(n)

        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(nums)