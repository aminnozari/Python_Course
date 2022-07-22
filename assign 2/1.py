temp_numbers = 0
while True:
    a = input("Enter Number")
    if a == "exit":
        break
    else:
        temp_numbers += int(a)
    print(temp_numbers)