from .statistics import get_statistics
from .statistics import predict_symbol
from random import choice


def main():
    length = 100
    text = ""
    print("Please give AI some data to learn...")
    print("The current data length is 0, 100 symbols left")
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
    print("You have $1000. Every time the system successfully predicts your next press, you lose $1."
          "Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")
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

    statistics = get_statistics(text, triads)

    # for triad, values in result.items():
    #    total_zeros, total_ones = values
    #    print(f"{triad}: {total_zeros},{total_ones}")
    capital = 1000
    while True:
        print("Print a random string containing 0 or 1:")
        test_string = input()
        if test_string == "enough":
            print("Game over!")
            break
        if not all([True if x in ["1", "0"] else False for x in test_string]):
            continue
        # print(test_string)
        print("prediction")
        values = ["1", "0"]
        predicted = "".join([choice(values) for _ in range(3)])
        total = len(test_string) - 3
        right_predicted = 0
        for index in range(3, len(test_string)):
            element = test_string[index]
            prediction = predict_symbol(statistics, test_string[index-3:index])
            predicted += prediction
            if prediction == element:
                right_predicted += 1
        print(predicted)
        print()
        percent = round(100*right_predicted/total, 2)
        print(f"Computer guessed right {right_predicted} out of {total} symbols ({percent} %)")

        capital -= right_predicted
        capital += total - right_predicted
        print(f"Your capital is now ${capital}")
        print()


if __name__ == '__main__':
    main()
