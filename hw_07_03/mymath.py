# returns sum of 2 numbers
def calc():
    n1 = int(input('num? '))
    n2 = int(input('num? '))
    return n1 + n2


# prints the multiplication table
def multi_table():
    table = ''
    for i in range(1, 11):
        for j in range(1, 11):
            table += str(i * j) + " "
        table += '\n'
    print(table)
