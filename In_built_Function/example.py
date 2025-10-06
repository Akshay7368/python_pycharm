'''
#capitalise
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

#casefold
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#center
txt = "banana"
x = txt.center(50)
print(x)

#count

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#encode
txt = "My name is Ståle"
x = txt.encode()
print(x)

#endswith

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

#expandtabs
txt = "H\te\tl\tlo"
x =  txt.expandtabs(2)
print(x)

#find
#where it starts
txt = "Hello,welcome to my world."
x = txt.find("x")
print(x)

#format
txt = "For only {price:.5f} dollars!"
print(txt.format(price = 49))

#index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#isalnum It should contains only numbers and alphabets.(No spaces)
txt = "Company12"
x = txt.isalnum()
print(x)

#isalpha - It should contains only alphabets
txt = "Company0x"
x = txt.isalpha()
print(x)


print("------")
#isascii
txt = "company"#"Companåy:"
x = txt.isascii()
print(x)

#isdecimal
txt = "1234"#"1/2"
x = txt.isdecimal()
print(x)

#isdigit
txt = "5080A0" #"50800.3"
x = txt.isdigit()
print(x)

#isidnetifier - It should always starts with an alphabet
txt = "Demo"#"1dem" "dem 0"
x = txt.isidentifier()
print(x)

#islower
txt = "hello world!"
x = txt.islower()
print(x)
'''
#isnumeric
txt = "56554"#"56554a"
x = txt.isnumeric()
print(x)

#isprintable
txt = "Hello! Are you #1?" #"Hello! Are you #1\t?"
x = txt.isprintable()
print(x)

#isspace
txt = "  "#"  a  "
x = txt.isspace()
print(x)

#istitle
txt = "Hello, And Welcome To My World!"#"Hello, and Welcome To My World!"
x = txt.istitle()
print(x)

#isupper
txt = "THIS IS NOW!"#"THIS IS NoW!"
x = txt.isupper()
print(x)

#join
myTuple = ("John", "Peter", "Vicky")
x = " * ".join(myTuple)
print(x)

#!just
txt = "banana"
x = txt.ljust(10)
print(x, "is my favorite fruit.")

#lower
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#lstrip
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#trans casesensitive
txt = "Hello SamS!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

#partition takes first
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

#replace
txt = "I like bananas"
x = txt.replace("banana", "app")
print(x)

#rfind #space
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

#rindex #space
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

#rjust
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

#rpartition
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

#rsplit
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

#rstrip
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

#split
txt = "welcome to the jungle"
x = txt.split()
print(x)

#splitlines
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
