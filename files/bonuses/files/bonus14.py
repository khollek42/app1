from files.bonuses.files.converter14 import convert
from files.bonuses.files.parsers14 import parse

feet_inches = input("enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])


print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")


if result < 1.5:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")