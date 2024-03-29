# 0x01-python-if_else_loops_functions

## Resources
`Read or watch`:
+ [How to Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)

`man or help`
+ python3

## Learning Objectives
+ Why Python programming is awesome
+ Why indentation is so important in Python
+ How to use the `if`, `if ... else` statements
+ How to use comments
+ How to affect values to variables
+ How to use the `while` and `for` loops
+ How is Python's `for` different from `C`'s?
+ How to use the `break` and `continue` statements
+ How to use `else` clauses on loops
+ What does the pass the `pass` statement do, and when to use it
+ How to use `range`
+ What is the function and how do you use functions
+ What does return a function that does not use any `return` statement
+ Scope of variables
+ What's a traceback
+ What are the arithmetic operators and how to use them


## Tasks

### 0-positive_or_negative.py
> Complete the following source code in order to print whether the number stored in the variable `number` is positive or negative. The output should be the `number`, followed by `is positive` if the number greater than 0, `is zero` if the number is 0, and `is negative` if the number is less than 0, followed by a new line.
```
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
```

```
gamachu@ubuntu:~$ ./0-positive_or_negative.py 
0 is zero
gamachu@ubuntu:~$ ./0-positive_or_negative.py 
-3 is negative
gamachu@ubuntu:~$ ./0-positive_or_negative.py 
-10 is negative
gamachu@ubuntu:~$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$
```

### 1-last_digit.py
> Complete the following source code in order to print the last digit of the number stored in the variable `number`.
```
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
```
  - The output should be the `number`, followed by
      - `and is greater than 5` if the last digit > 5
      - `and is 0` if the last digit == 0
      - `and is less than 6 and not 0` if the last digit < 6 and !== 0
  - followed by a new line
```
gamachu@ubuntu:~$ ./1-last_digit.py
Last digit of 809 is 9 and is greater than 5
gamachu@ubuntu:~$ ./1-last_digit.py
Last digit of 2035 is 5 and is less than 6 and not 0
gamachu@ubuntu:~$ ./1-last_digit.py
Last digit of -5227 is -7 and is less than 6 and not 0
gamachu@ubuntu:~$ ./1-last_digit.py
Last digit of 3890 is 0 and is 0
gamachu@ubuntu:~$
```

### 2-print_alphabet.py
> Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
  - You can only use one `print` function with string format
  - You can only use one loop in your code
  - You are not allowed to store characters in a variable
  - You are not allowed to import any module
```
gamachu@ubuntu:~$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzgamachu@ubuntu:~$
```

### 3-print_alphabt.py
> Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

  - Print all the letters except q and e
  - You can only use one print function with string format
  - You can only use one loop in your code
  - You are not allowed to store characters in a variable
  - You are not allowed to import any module

```
gamachu@ubuntu:~$ ./2-print_alphabet.py
abcdfghijklmnoprstuvwxyzgamachu@ubuntu:~$
```

### 4-print_hexa.py
> Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

  - You can only use one print function with string format
  - You can only use one loop in your code
  - You are not allowed to store numbers or strings in a variable
  - You are not allowed to import any module
```
gamachu@ubuntu:~$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
...
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
gamachu@ubuntu:~$
```

### 5-print_comb2.py
> Write a program that prints numbers from 0 to 99.

  - Numbers must be separated by ,, followed by a space
  - Numbers should be printed in ascending order, with two digits
  - The last number should be followed by a new line
  - You can only use no more than 2 print functions with string format
  - You can only use one loop in your code
  - You are not allowed to store numbers or strings in a variable
  - You are not allowed to import any module
```
gamachu@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
gamachu@ubuntu:~$ 
```

### 6-print_comb3.py
Write a program that prints all possible different combinations of two digits.

  - Numbers must be separated by `,`, followed by a space
  - The two digits must be different
  - 01 and 10 are considered the same combination of the two digits 0 and 1
  - Print only the smallest combination of two digits
  - Numbers should be printed in ascending order, with two digits
  - The last number should be followed by a new line
  - You can only use no more than 3 print functions with string format
  - You can only use no more than 2 loops in your code
  - You are not allowed to store numbers or strings in a variable
  - You are not allowed to import any module
```
gamachu@ubuntu:~$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
gamachu@ubuntu:~$
```

### 7-islower.py
> Write a function that checks for lowercase character.

  - Prototype: `def islower(c)`:
  - Returns True if c is lowercase
  - Returns False otherwise
  - You are not allowed to import any module
  - You are not allowed to use str.upper() and str.isupper()
  - Tips: ord()
You don’t need to understand `__import__`
```
gamachu@ubuntu:~$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

gamachu@ubuntu:~$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
gamachu@ubuntu:~$
```

### 8-uppercase.py
> Write a function that prints a string in uppercase followed by a new line.

  - Prototype: `def uppercase(str)`:
  - You can only use no more than 2 print functions with string format
  - You can only use one loop in your code
  - You are not allowed to import any module
  - You are not allowed to use str.upper() and str.isupper()
  - Tips: ord()
You don’t need to understand __import__
```
gamachu@ubuntu:~$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")

gamachu@ubuntu:~$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
gamachu@ubuntu:~$ 
```

### 9-print_last_digit.py
> Write a function that prints the last digit of a number.

  - Prototype: `def print_last_digit(number):`
  - Returns the value of the last digit
  - You are not allowed to import any module

```
gamachu@ubuntu:~$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

gamachu@ubuntu:~$ ./9-main.py
8044
gamachu@ubuntu:~$ 
```

### 10-add.py
Write a function that adds two integers and returns the result.

  - Prototype: `def add(a, b):`
  - Returns the value of a + b
  - You are not allowed to import any module

```
gamachu@ubuntu:~$ cat 10-main.py
#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 1))
print(add(-5, 5))

gamachu@ubuntu:~$ ./10-main.py
3
99
0
gamachu@ubuntu:~$
```

### 11-pow.py
> Write a function that computes a to the power of b and return the value.

  - Prototype: def pow(a, b):
  - Returns the value of a ^ b
  - You are not allowed to import any module
You don’t need to understand __import__
```
gamachu@ubuntu:~$ cat 11-main.py
#!/usr/bin/env python3
pow = __import__('11-pow').pow

print(pow(2, 10))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

gamachu@ubuntu:~$ ./11-main.py
1024
1
0.0001
-1024
gamachu@ubuntu:~$ 
```

### 12-fizzbuzz.py
> Write a function that prints the numbers from 1 to 100 separated by a space.

  - For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
  - For numbers which are multiples of both three and five print FizzBuzz.
  - Prototype: `def fizzbuzz():`
  - Each element should be followed by a space
  - You are not allowed to import any module
You don’t need to understand __import__
```
gamachu@ubuntu:~$ cat 12-main.py
#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

gamachu@ubuntu:~$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
gamachu@ubuntu:~$ 
```

### 13-insert_number.c
> Write a function in C that inserts a number into a sorted singly linked list.

  - Prototype: `listint_t *insert_node(listint_t **head, int number)`;
  - Return: the address of the new node, or NULL if it failed

## Advanced tasks (optional)

### 100-print_tebahpla.py
> Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.

  - You can only use one print function with string format
  - You can only use one loop in your code
  - You are not allowed to store characters in a variable
  - You are not allowed to import any module
```
gamachu@ubuntu:~$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbAgamachu@ubuntu:~$
```

### 101-remove_char_at.py
> Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).

  - Prototype: `def remove_char_at(str, n)`:
  - You are not allowed to import any module
```
gamachu@ubuntu:~$ cat 101-main.py
#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))

gamachu@ubuntu:~$ ./101-main.py
Bes School
Chcago
 is fun!
School
Python
gamachu@ubuntu:~$ 
```

### 102-magic_calculation.py
Write the Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
  - **Tip**: [ByteCode](https://docs.python.org/3.4/library/dis.html)

## Just for Fun
```
gamachu@ubuntu:~$ python3
>>> sum(range(101))
5050
>>> print(sum(range(101))
... )
5050
>>> range(101)
range(0, 101)
>>> print(range(101))
range(0, 101)
>>> list(range(4,-1))
[]
>>> list(range(-1, 4))
[-1, 0, 1, 2, 3]
>>> list(range(-6, 0, -1))
[]
>>> list(range(-6, 0, 1))
[-6, -5, -4, -3, -2, -1]
>>> list(range(-6, 0, 2))
[-6, -4, -2]
>>> list(range(2,2))
[]
>>> def f(a, L=[]):
...   L.append(a)
...   return L
...
>>> print(f(1))
[1]
>>> print(f(2))
[1, 2]
>>> print(f(4))
[1, 2, 4]
>>> def g(b, t=()):
...   L = list(t)
...   L.append(b)
...   return tuple(L)
...
>>> print(g(1))
(1,)
>>> print(g(2))
(2,)
>>> print(g(3))
(3,)
>>> "{1}{0}{2}".format("One", "Zero", "Two")
'ZeroOneTwo'
>>> "{}-{}-{}".format("One", "Zero", "Two")
'One-Zero-Two'
>>> "{1}-{0}-{2}".format("One", "Zero", "Two")
'Zero-One-Two'
>>> "{1}-{0}-{2}".format("One", "Zero", 2)
'Zero-One-2'
>>> "{1}-{0}-{2}".format(1, 0, 2)
'0-1-2'
>>> "{1}-{0}-{go}".format(1, 0, go="Fiigi")
'0-1-Fiigi'
>>> "float {0:f}".format(3.14)
'float 3.140000'
>>> "float {0:f}".format(3)
'float 3.000000'
>>> "float {0:d}".format(3)
'float 3'
>>> "float {0:3f}".format(3.14)
'float 3.140000'
>>> "float {0:30f}".format(3.14)
'float                       3.140000'
>>> "float {0:30.3f}".format(3.14)
'float                          3.140'
>>> "float {0:=^30.3f}".format(3.14)
'float ============3.140============='
>>> "float {0:=30.3f}".format(3.14)
'float                          3.140'
>>> "float {0:=>30.3f}".format(3.14)
'float =========================3.140'
>>> "float {0:=<30.3f}".format(3.14)
'float 3.140========================='
>>> "float {0:*>10.0f}".format(3.14)
'float *********3'
>>> "float {0:*>10.1f}".format(3.14)
'float *******3.1'
>>> "float {0:>5.1f}".format(3.14)
'float >>3.1'
>>> "float {0:<>5.1f}".format(3.14)
'float <<3.1'
>>> "float {0:<5.1f}".format(3.14)
'float 3.1  '
>>> "float {0:5.1f}".format(3.14)
'float   3.1'
>>> "float {0:>5.1f}".format(3.14)
'float   3.1'
>>> "float {0:^5.1f}".format(3.14)
'float  3.1 '
>>> for i in range(1, 10):
...   print("{:*>5d} {:*>5d} {:*>5d}".format(i, i*i,
i*i
...
...
... ))
...
****1 ****1 ****1
****2 ****4 ****4
****3 ****9 ****9
****4 ***16 ***16
****5 ***25 ***25
****6 ***36 ***36
****7 ***49 ***49
****8 ***64 ***64
****9 ***81 ***81
>>> for i in range(1, 10):
...   print("{:_>5d} {:_>5d} {:_>5d}".format(i, i*i, i*i*i))
...
____1 ____1 ____1
____2 ____4 ____8
____3 ____9 ___27
____4 ___16 ___64
____5 ___25 __125
____6 ___36 __216
____7 ___49 __343
____8 ___64 __512
____9 ___81 __729
>>> 12 == 48/4
True
>>> 12 == 12.00
True
>>> 12 == 12.002
False
>>> 12.002 == 12.002
True
>>> 3/2 == 3/2
True
>>> 12 is 12
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True
>>> i = 12
>>> j = 12
>>> i is j
True
>>> k = j
>>> k is j
True
>>> m = 12.00
>>> k is m
False
>>> m == k
True
>>> -24 % 10
6
>>> 0 % 10
0
>>> 5 % 10
5
>>> -24 % -10
-4
>>> -24 % 10 - 10
-4
>>> 24 % -10
-6
>>> chr(112)
'p'
>>> chr(97)
'a'
>>> chr(122)
'z'
>>> type(chr(122))
<class 'str'>
>>> print(f"10", end=" ")
10 >>>
>>> n = print("HI")
HI
>>> print(n)
None
>>> print(f"10", end="?? ")
10?? >>> print(f"{10:*>5.2f}")
10.00
>>> print(f"{10:*>11.2f}")
******10.00
>>> ord('z')
122
>>> type(ord('0'))
<class 'int'>
>>> ord('0')
48
>>> "i" not in "in"
False
>>> "I" in "INPUT"
True
>>> print(f"{10:x}")
a
>>> print(f"{11:X}")
B
>>> print(f"{'Hi'}" + " {}".format(22), end="*")
Hi 22*>>>
>>> 5 < 6 < 8
True
>>> 5 < 6 < 3
False
>>> 'Z' < 'z'
True
>>> chr(ord('A') + 26)
'['
>>> chr(ord('A') + 32)
'a'
>>> chr(ord('a') - 32)
'A'
>>> print("Hello"[-1])
o
>>> for i in range(ord('z'), ord('a')-1, -1):
...   print("{}".format(chr(i - 32) if i % 2 else chr(i)))
...
z
Y
x
W
v
U
t
S
r
Q
p
O
n
M
l
K
j
I
h
G
f
E
d
C
b
A
>>> for i in range(ord('z'), ord('a')-1, -1):
...   print("{}".format(chr(i - 32) if i % 2 else chr(i)), end='')
...
zYxWvUtSrQpOnMlKjIhGfEdCbA>>>
>>> def magic(a, b, c):
...
...   if a < b:
...     return c
...   elif c > b:
...     return a + b
...   else:
...     return a * b - c
...
>>> import dis
>>> dis.dis(magic)
  3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 COMPARE_OP               0 (<)
              6 POP_JUMP_IF_FALSE       12

  4           8 LOAD_FAST                2 (c)
             10 RETURN_VALUE

  5     >>   12 LOAD_FAST                2 (c)
             14 LOAD_FAST                1 (b)
             16 COMPARE_OP               4 (>)
             18 POP_JUMP_IF_FALSE       28

  6          20 LOAD_FAST                0 (a)
             22 LOAD_FAST                1 (b)
             24 BINARY_ADD
             26 RETURN_VALUE

  8     >>   28 LOAD_FAST                0 (a)
             30 LOAD_FAST                1 (b)
             32 BINARY_MULTIPLY
             34 LOAD_FAST                2 (c)
             36 BINARY_SUBTRACT
             38 RETURN_VALUE
             40 LOAD_CONST               0 (None)
             42 RETURN_VALUE
>>> def magic_calculation(a, b, c):
...   if a < b:
...     return c
...   elif c > b:
...     return a + b
...   return a * b - c
...
>>> dis.dis(magic_calculation)
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 COMPARE_OP               0 (<)
              6 POP_JUMP_IF_FALSE       12

  3           8 LOAD_FAST                2 (c)
             10 RETURN_VALUE

  4     >>   12 LOAD_FAST                2 (c)
             14 LOAD_FAST                1 (b)
             16 COMPARE_OP               4 (>)
             18 POP_JUMP_IF_FALSE       28

  5          20 LOAD_FAST                0 (a)
             22 LOAD_FAST                1 (b)
             24 BINARY_ADD
             26 RETURN_VALUE

  6     >>   28 LOAD_FAST                0 (a)
             30 LOAD_FAST                1 (b)
             32 BINARY_MULTIPLY
             34 LOAD_FAST                2 (c)
             36 BINARY_SUBTRACT
             38 RETURN_VALUE
>>> def magic_calculation(a, b, c):
...
...   if a < b:
...     return c
...   elif c > b:
...     return a + b
...   return a * b - c
...
>>> dis.dis(magic_calculation)
  3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 COMPARE_OP               0 (<)
              6 POP_JUMP_IF_FALSE       12

  4           8 LOAD_FAST                2 (c)
             10 RETURN_VALUE

  5     >>   12 LOAD_FAST                2 (c)
             14 LOAD_FAST                1 (b)
             16 COMPARE_OP               4 (>)
             18 POP_JUMP_IF_FALSE       28

  6          20 LOAD_FAST                0 (a)
             22 LOAD_FAST                1 (b)
             24 BINARY_ADD
             26 RETURN_VALUE

  7     >>   28 LOAD_FAST                0 (a)
             30 LOAD_FAST                1 (b)
             32 BINARY_MULTIPLY
             34 LOAD_FAST                2 (c)
             36 BINARY_SUBTRACT
             38 RETURN_VALUE
>>> # now all is good, let's exit
>>> quit()
gamachu@ubuntu:~$
```
---
Author: gAmAchU
