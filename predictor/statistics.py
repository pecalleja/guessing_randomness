import re


def get_statistics(text: str, triads: list[str]) -> dict:
    statistics = {}
    for triad in triads:
        ones = f"(?=({triad}1))"
        zeros = f"(?=({triad}0))"
        total_ones = len(re.findall(ones, text))
        total_zeros = len(re.findall(zeros, text))
        statistics[triad] = [total_zeros, total_ones]
    return statistics
