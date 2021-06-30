length = 100

text = ""
while True:
    print("Print a random string containing 0 or 1:")
    print()
    user_input = [x for x in input() if x in ["1", "0"]]
    text += "".join(user_input)
    if len(text) >= 100:
        break
    print(f"Current data length is {length}, {length - len(text)} symbols left")

print()
print("Final data string:")
print(text)
