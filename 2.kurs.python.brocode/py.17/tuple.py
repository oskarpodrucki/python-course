student = ("oskar",16,"male")

print(student.count("oskar"))
print(student.index("male"))


for x in student:
    print(x)

if "oskar" in student:
    print("oskar is here")