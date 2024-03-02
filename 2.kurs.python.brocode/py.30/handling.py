try: 
    num = int(input("enter a numer to divide: "))
    den = int(input("enter a number to divide by: "))
    result = num / den
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero")
except ValueError as e:
    print(e)
    print("enter only numbers")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("ok")