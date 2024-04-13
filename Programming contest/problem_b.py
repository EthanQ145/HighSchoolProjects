months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
while True:
    date = input().split()
    if date[0] == '0' and date[1] == "#":
        break
    month = date[1]
    day = int(date[0])
    if months.index(month) != 1 or day != 29:
        if months.index(month) < 8:
            print("You have had your birthday.")
        elif months.index(month) > 8:
            print("Your birthday is still to come.")
        elif months.index(month) == 8:
            if day < 11:
                print("You have had your birthday.")
            elif day > 11:
                print("Your birthday is still to come.")
            elif day == 11:
                print("Happy birthday!")
    else:
        print("Sorry, leapling, no birthday this year.")