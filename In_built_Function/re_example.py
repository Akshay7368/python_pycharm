import re
#
# txt = " Hello welcome to my world"
# Ans = re.findall("m", txt)
# print(Ans)
'''
txt1 = "Hi this is Akshay, from Chennai and my age is 23"
Ans1 = re.findall("[arn]", txt1)
Ans2 = re.findall("[^arn]", txt1)
Ans3 = re.findall("[1234]", txt1)
Ans4 = re.findall("[0-9]", txt1)
Ans5 = re.findall("[a-zA-Z]", txt1)


print(Ans1)
print(Ans2)
print(Ans3)
print(Ans4)
print(Ans5)

txt2 = "Hello Akshay how are you"
a = re.findall("^Hello", txt2)
print(a)
a = re.findall("Akshay$", txt2)
print(a)
a = re.findall("^H", txt2)
print(a)
a = re.findall("^The", txt2)
print(a)
a = re.findall("He.o", txt2)
print(a)
a = re.findall("^He..o", txt2)
print(a)
a = re.findall("^He.*o", txt2)
print(a)


phno = input("Enter the phone number:")
if len(phno) < 10:
    print("Invalid Phone Number")
elif re.findall("[6-9][0-9]{9}", phno):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")



txt = "9080147368"
print("length:", len(txt))
if len(re.findall("[a-zA-Z]", str(txt))) == 0:
    if len(txt) == len(re.findall("[0-9]", txt)):
        print("It contains only numbers")
    else:
        print("It contains some special characters")


tx = "Hello welcome to my world everyone"
b = re.split("\\s", tx)
print(b)

b = re.split("my", tx)
print(b)

# b = re.split("\\s", tx, 3)
# print(b)

b = re.sub("\\s","9",tx)   # re.sub will replace
print(b)
'''

x = "hello bro welcome"
c = re.search("welcome", x)
print(c)
print(c.span())
print(c.group())
c1 = re.search("a", x)
print(c1)