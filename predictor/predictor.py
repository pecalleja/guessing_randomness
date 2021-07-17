from .statistics import get_statistics


def main():
    length = 100
    text = ""
    while True:
        print("Print a random string containing 0 or 1:")
        print()
        user_input = [x for x in input() if x in ["1", "0"]]
        text += "".join(user_input)
        if len(text) >= 100:
            break
        print(f"Current data length is {len(text)}, {length - len(text)} symbols left")

    print()
    print("Final data string:")
    print(text)
    print()

    triads = [
        "000",
        "001",
        "010",
        "011",
        "100",
        "101",
        "110",
        "111",
    ]

    result = get_statistics(text, triads)

    for triad, values in result.items():
        total_zeros, total_ones = values
        print(f"{triad}: {total_zeros},{total_ones}")
