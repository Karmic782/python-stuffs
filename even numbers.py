count = 0
print ('This program will count the even numbers in a range')
topnumber = int(input('Enter top number for the range: '))
for number in range(1, topnumber) :
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")