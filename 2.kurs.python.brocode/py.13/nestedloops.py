rows = int(input("how many rows: "))
columns = int(input("how many columns: "))
symbols = input("enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbols, end="")
    print()