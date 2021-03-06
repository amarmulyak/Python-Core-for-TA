"""
Provide full program code of parse_number(num) function which returns the dict with following structure:
{odd: number of odd digits in input value, even: number of even digits of input value} or false when wrong input value.
num - input number.
NOTE: Assume that the "zero" digit also belongs to even numbers
EXAMPLE OF Inputs/Ouputs when using this function:
```
print parse_number(34567)
{'odd': 3, 'even': 2}
print parse_number(100)
{'odd': 1, 'even': 2}
print parse_number("word")
False
```
"""
num = input("Provide number: ")
dict = {'odd': 0, 'even': 0}


def parse_number(n):
    if n.isdigit():
        for i in n:
            i = int(i)
            if i % 2 == 0:
                dict['even'] += 1
            else:
                dict['odd'] += 1
        print(dict)
    else:
        print("Please enter a valid number.")


parse_number(num)
