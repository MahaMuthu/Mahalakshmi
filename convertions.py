def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

print(convert(100))
while True:
    reply = input("Enter Text: ")
    if reply == 'stop': break
    print(reply)