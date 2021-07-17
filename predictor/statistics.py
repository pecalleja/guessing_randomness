import re
from random import choice


def get_statistics(text: str, triads: list[str]) -> dict:
    statistics = {}
    for triad in triads:
        ones = f"(?=({triad}1))"
        zeros = f"(?=({triad}0))"
        total_ones = len(re.findall(ones, text))
        total_zeros = len(re.findall(zeros, text))
        statistics[triad] = [total_zeros, total_ones]
    return statistics


def predict_symbol(statistics: dict, test_triad) -> str:
    zeros, ones = statistics[test_triad]
    if zeros > ones:
        return "0"
    elif ones > zeros:
        return "1"
    else:
        elements = ["1", "0"]
        return choice(elements)
