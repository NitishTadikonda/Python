def is_leap(year):
    leap = False
    # Write your logic here
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("Leap year")
            else:
                return leap
        else:
            return True
    else:
        return leap
year = int(input())
print(is_leap(year))
