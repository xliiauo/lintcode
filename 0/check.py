def date_conversion_robust(date_string):
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    def leap_year(n):
        if n % 4 == 0:
            return False
        elif n % 100 != 0:
            return True
        elif n % 400 != 0:
            return False
        else:
            return True
    if '/' not in date_string:
        print('cNot a valid date.')
        print('None')
        return(None)

    date = date_string.split('/')

    if len(date) != 3:
        print('cNot a valid date.')
        print('None')
        return(None)
    elif int(date[2]) < 0 | (int(date[2]) < 1000) & (int(date[2]) > 99) | int(date[2]) > 9999:
        print('Not a valid date.')
        print('None')
        return(None)
    elif int(date[0]) >= 31:
        print('Not a valid date.')
        print('None')
        return(None)
    elif int(date[1]) >= 12:
        print('Not a valid date.')
        print('None')
        return(None)
    elif (int(date[1]) in [4,6,9,11]) & (int(date[0]) == 31):
        print('Not a valid date.')
        print('None')
        return(None)
    elif (int(date[1]) == 2) & (int(date[0]) > 29) & (leap_year(int(date[2]))):
        print('Not a valid date.')
        print('None')
        return(None)
    elif (int(date[1]) == 2) & (int(date[0]) >= 29) & (not leap_year(int(date[2]))):
        print('Not a valid date.')
        print('None')
        return(None)
    else:
        return 1
