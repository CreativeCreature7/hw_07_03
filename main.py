# להכריז על list אימפליסיטת, לשים בו מספרים
# לבנות לולאה שמוצאת את המספר הגדול ביותר במערך
lst = [21, 22, 89, 0, 24, 11, 83, 14, 9, 123012, 1]
big = lst[0]
for item in lst:
    if item > big:
        big = item
print(big)

# ממוצע של מערך שמוכרז אקספליסית
lst = list((21, 22, 89, 0, 24, 11, 83, 14, 9, 123012, 1))
avg = 0
for item in lst:
    avg += item
print(avg / len(lst))

# אותו דבר אבל עם while
lst = list((21, 22, 89, 0, 24, 11, 83, 14, 9, 123012, 1))
avg = 0
i = 0
while i < len(lst):
    avg += lst[i]
    i += 1
print(avg / len(lst))

# למיין List
lst = [21, 22, 89, 0, 24, 11, 83, 14, 9, 123012, 1]
lst.sort()  # sorts a list in ascending order
print(lst)

# לחבר 2 lists
# option 1
lst1 = [21, 22, 89, 0, 24, 11, 83, 14, 9, 123012, 1]
lst2 = list(('hello', True, 3, 69, 21, 's', 'e', 'x', 'y'))
lst3 = lst1 + lst2
print(lst3)

# option 2
lst1 = [21, 22, 89, 0, 24, 11, 83, 14, 9, 123012, 1]
lst2 = list(('hello', True, 3, 69, 21, 's', 'e', 'x', 'y'))
lst1.extend(lst2)
print(lst1)

# להגדיר tuple אימפליסית, לרוץ על הtuple עם לולאת for עם אינדקס ולהדפיס אינדקס והערך
# option 1
t = ('my ni**a', 2, 22, 222, 'f')
for i in range(len(t)):
    print(f'index: {i}, value: {t[i]}')

# option 2 (advanced)
for index, value in enumerate(t): print(f'index: {index}, value: {value}')

# למצוא את הפונקציה zip באינטרנט ולהשתמש בה לחבר שני tuples
# https://www.w3schools.com/python/ref_func_zip.asp
t1 = (1, 'Guy', 'ma@ya')
t2 = tuple(('Hello', 'from', 'Mars'))
zipped = zip(t1, t2)
print(tuple(zipped))

# לקלוט מספר מהמשתמש, להדפיס אותו כפול 2
num = float(input('Enter Number: '))
print(num * 2)
# לקלוט מספר מהמשתמש שם פרטי, שם משפחה ואמייל ולהדפיס "אלו הפרטים שלך"
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
email = input('Enter your email name: ')

print(f'Your account information:\nfirst name: {first_name}\nlast name: {last_name}\nemail: {email}')


# לייצר 3 מודולים על נושאים שונים (להתמקד בדברים שפחות הבנו, while for if כל אחד במה שמתקשה)
# לפתוח main שקורא למודולים האלו
def main():
    import osmodule
    import stringmodule as sm
    import mymath

    print(osmodule.cpu_count())
    mymath.multi_table()
    sm.greeting('Guy')


if __name__ == "__main__":
    main()


# לבנות תפריט שמציע 5 פעולות שונות לפחות ואפשרות יציאה מהתוכנית

def menu():
    import stringmodule
    import mymath
    import osmodule
    import os

    menu = """Menu:
    e - exit
    c - calc
    p - cpu count
    g - greeting
    b - get your string back
    o - get the name of your opreating system
    """

    while True:
        print(menu)
        cm = input('enter command')
        os.system('cls')
        if (cm == 'e'): return
        if (cm == 'c'): print(mymath.calc())
        if (cm == 'p'): print(stringmodule.cpu_count())
        if (cm == 'g'): print(stringmodule.greeting(input('your name? ')))
        if (cm == 'b'): print(stringmodule.your_string('write: '))
        if (cm == 'o'): print(stringmodule.op_name())
