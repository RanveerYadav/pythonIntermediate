def doMath():
    return  input("Please enter a number ",)

try:
    number = int(doMath())
    # result = number // 0
    print(number)
except ValueError:
    print('Please enter an interger value')
except ZeroDivisionError:
    print('Division by zero is not allowed')
except Exception as e:
    print(e)
# else always executes only when try is executed properly
else:
    print("Successfully executed the code")
# finally block always executes
finally:
    print("It will always excute")
