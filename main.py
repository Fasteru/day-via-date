
# TAKING DATE AND YEAR FROM TH USER
DATE = int(input("enter the date"))
YEAR = int(input("enter the year"))
# TAKING LEAP YEAR INTO ACCOUNT
if YEAR % 4 == 0:
    x1 = YEAR//1000
    a = YEAR-(x1*1000)
    b = a//100
    c = a-(b*100)
    YEAR_CODE = (c+(c//4)) % 7
    if (YEAR >= 1700) and (YEAR <= 1800):
        CENTURY_CODE = 4
    elif (YEAR >= 1800) and (YEAR <= 1900):
        CENTURY_CODE = 2
    elif (YEAR >= 1900) and (YEAR <= 2000):
        CENTURY_CODE = 0
    elif (YEAR >= 2000) and (YEAR <= 2100):
        CENTURY_CODE = 6
    elif (YEAR >= 2100) and (YEAR <= 2200):
        CENTURY_CODE = 4
    elif (YEAR >= 2200) and (YEAR <= 2300):
        CENTURY_CODE = 2
    elif (YEAR >= 2300) and (YEAR <= 2400):
        CENTURY_CODE = 0
    else:
        print("INVALID SYNTAX")
    list1 = ['january', 'februray', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
             'november',
             'december']
    month_code_list = ['0', '3', '3', '6', '1', '4', '6', '2', '5', '0', '3', '5']
    MONTH = input("enter the month")

    if MONTH == list1[0]:
        MONTH_CODE = 0
    elif MONTH == list1[1]:
        MONTH_CODE = 3
    elif MONTH == list1[2]:
        MONTH_CODE = 3
    elif MONTH == list1[3]:
        MONTH_CODE = 6
    elif MONTH == list1[4]:
        MONTH_CODE = 1
    elif MONTH == list1[5]:
        MONTH_CODE = 4
    elif MONTH == list1[6]:
        MONTH_CODE = 6
    elif MONTH == list1[7]:
        MONTH_CODE = 2
    elif MONTH == list1[8]:
        MONTH_CODE = 5
    elif MONTH == list1[9]:
        MONTH_CODE = 0
    elif MONTH == list1[10]:
        MONTH_CODE = 3
    elif MONTH == list1[11]:
        MONTH_CODE = 5

    d = (YEAR_CODE + MONTH_CODE + CENTURY_CODE + DATE) % 7

    if d == 0:
        print("THE DAY IS SUNDAY")
    elif d == 1:
        print("THE DAY IS MONDAY")
    elif d == 2:
        print("THE DAY IS TUESDAY")
    elif d == 3:
        print("THE DAY IS WEDNESDAY")
    elif d == 4:
        print("THE DAY IS THURSDAY")
    elif d == 5:
        print("THE DAY IS FRIDAY")
    else:
        print("THE DAY IS SATURDAY")

else:
    x1 = YEAR // 1000
    a = YEAR - (x1 * 1000)
    b = a // 100
    c = a - (b * 100)
    YEAR_CODE = (c + (c // 4)) % 7
    if (YEAR >= 1700) and (YEAR <= 1800):
        CENTURY_CODE = 4
    elif (YEAR >= 1800) and (YEAR <= 1900):
        CENTURY_CODE = 2
    elif (YEAR >= 1900) and (YEAR <= 2000):
        CENTURY_CODE = 0
    elif (YEAR >= 2000) and (YEAR <= 2100):
        CENTURY_CODE = 6
    elif (YEAR >= 2100) and (YEAR <= 2200):
        CENTURY_CODE = 4
    elif (YEAR >= 2200) and (YEAR <= 2300):
        CENTURY_CODE = 2
    elif (YEAR >= 2300) and (YEAR <= 2400):
        CENTURY_CODE = 0
    else:
        print("INVALID SYNTAX")

    list1 = ['january', 'februray', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
             'november', 'december']
    MONTH = input("enter the month")
    if MONTH == list1[0]:
        MONTH_CODE = 0
    elif MONTH == list1[1]:
        MONTH_CODE = 3
    elif MONTH == list1[2]:
        MONTH_CODE = 3
    elif MONTH == list1[3]:
        MONTH_CODE = 6
    elif MONTH == list1[4]:
        MONTH_CODE = 1
    elif MONTH == list1[5]:
        MONTH_CODE = 4
    elif MONTH == list1[6]:
        MONTH_CODE = 6
    elif MONTH == list1[7]:
        MONTH_CODE = 2
    elif MONTH == list1[8]:
        MONTH_CODE = 5
    elif MONTH == list1[9]:
        MONTH_CODE = 0
    elif MONTH == list1[10]:
        MONTH_CODE = 3
    elif MONTH == list1[11]:
        MONTH_CODE = 5
    day = (YEAR_CODE + MONTH_CODE + CENTURY_CODE + DATE) % 7

    if day == 0:
        print("THE DAY IS SUNDAY")
    elif day == 1:
        print("THE DAY IS MONDAY")
    elif day == 2:
        print("THE DAY IS TUESDAY")
    elif day == 3:
        print("THE DAY IS WEDNESDAY")
    elif day == 4:
        print("THE DAY IS THURSDAY")
    elif day == 5:
        print("THE DAY IS FRIDAY")
    else:
        print("THE DAY IS SATURDAY")




