def is_vovel(ch):
    return ch.lower() in "aeiou"

ch=input("Enter a string")

if is_vovel(ch):
    print("true")
else:
    print("false")

