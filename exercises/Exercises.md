# Exercises

* [Strings and user input](#strings-and-user-input)
* [Defining functions](#defining-functions)
* [Control structures](#control-structures)
* [Importing and creating modules](#importing-and-creating-modules)
* [Exception handling](#exception-handling)
* [Debugging](#debugging)
* [Testing](#testing)
* [Tuple and Sequence operations](#tuple-and-sequence-operations)
* [List](#list)
* [Mutability](#mutability)
* [Dict](#dict)
* [Set](#set)
* [Text processing](#text-processing)
* [Comprehensions and Generator expressions](#comprehensions-and-generator-expressions)
* [Dealing with files](#dealing-with-files)
* [Executing external commands](#executing-external-commands)
* [Command line arguments](#command-line-arguments)
* [More exercises](#more-exercises)

<br>

# Strings and user input

* Read about **Bytes** literals from [docs.python: String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#strings). See also [stackoverflow: What is the difference between a string and a byte string?](https://stackoverflow.com/q/6224052/4082052)
* If you check out [docs.python: int() function](https://docs.python.org/3/library/functions.html#int), you'll see that the `int()` function accepts an optional argument. As an example, write a program that asks the user for hexadecimal number as input. Then, use `int()` function to convert the input string to an integer (you'll need the second argument for this). Add `5` and display the result in hexadecimal format.
* Write a program to accept two input values. First can be either a number or a string value. Second is an integer value, which should be used to display the first value in centered alignment. You can use any character you prefer to surround the value, other than the default space character.
* What happens if you use a combination of `r`, `f` and other such valid prefix characters while declaring a string literal? What happens if you use raw strings syntax and provide only a single `\` character? Does the documentation describe these cases?
* Try out at least two format specifiers not discussed in this chapter.
* Given `a = 5`, get `'{5}'` as the output using **f-strings**.

<br>

# Defining functions

* Call the function before declaration and see what happens for this program:

    ```ruby
    def greeting():
        print('-----------------------------')
        print('         Hello World         ')
        print('-----------------------------')

    greeting()
    ```

* For the program shown below, try these experiments:
    * add print statements for `ip`, `op_length` and `styled_line` variables at the end of the program (after the function calls)
    * pass a numeric value to the `greeting()` function
    * don't pass any argument while calling the `greeting()` function

    ```ruby
    def greeting(ip):
        op_length = 10 + len(ip)
        styled_line = '-' * op_length
        print(styled_line)
        print(f'{ip:^{op_length}}')
        print(styled_line)

    greeting('hi')
    weather = 'Today would be a nice, sunny day'
    greeting(weather)
    ```

* Modify the script shown below as per these requirements:
    * what do you think will happen if you call the function as `greeting(spacing=5, ip='Oh!')`
    * make the spacing work for multicharacter `style` argument
    * accept another argument with a default value of single space character that determines the character to be used around the centered `ip` value

    ```ruby
    def greeting(ip, style='-', spacing=10):
        op_length = spacing + len(ip)
        styled_line = style * op_length
        print(styled_line)
        print(f'{ip:^{op_length}}')
        print(styled_line)

    greeting('hi')
    greeting('bye', spacing=5)
    greeting('hello', style='=')
    greeting('good day', ':', 2)
    ```

<br>

# Control structures

* What would happen if you use `<` or `<=` or `>` or `>=` operators between numeric and string values?
* Simplify the function shown below (you wouldn't need any form of ternary operator):

    ```ruby
    def isodd(n):
        if n % 2:
            return True
        else:
            return False
    ```

* Create this arithmetic progression `-2, 1, 4, 7, 10, 13` using the `range()` function.
* Use appropriate `range()` logic so that the `if` statement is no longer needed for the snippet shown below.

    ```ruby
    for num in range(10):
        if num % 3:
            continue
        print(f'{num} * 2 = {num * 2}')
    ```

* If you don't already know about **FizzBuzz**, read [Using FizzBuzz to Find Developers who Grok Coding](https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/) and implement it in Python. See also [Why Can't Programmers.. Program?](https://blog.codinghorror.com/why-cant-programmers-program/)
* Print all numbers from `1` to `1000` (inclusive) which reads the same in reversed form in both binary and decimal format. For example, `33` in decimal is `100001` in binary and both of these are palindromic. You can either implement your own logic or search online for palindrome testing in Python.
* Write a function that returns the maximum nested depth of curly braces for a given string input. For example, `'{{a+2}*{{b+{c*d}}+e*d}}'` should give `4`. Unbalanced or wrongly ordered braces like `'{a}*b{'` and `'}a+b{'` should return `-1`.

<br>

# Importing and creating modules

* For the program shown below:
    * add docstrings and check the output of `help()` function using `num_funcs`, `num_funcs.fact`, etc as arguments.
    * check what would be the output of `num_funcs.fact()` for negative integers and floating-point numbers. Then import the `math` built-in module and repeat the process with `math.factorial()`.

    ```ruby
    def sqr(n):
        return n * n

    def fact(n):
        total = 1
        for i in range(2, n+1):
            total *= i
        return total

    num = 5
    print(f'square of {num} is {sqr(num)}')
    print(f'factorial of {num} is {fact(num)}')
    ```

<br>

# Exception handling

* Identify the syntax errors in the following code snippets. Try to spot them manually.

    ```ruby
    # snippet 1:
    def greeting()
        print('hello')

    # snippet 2:
    num = 5
    if num = 4:
        print('what is going on?!')

    # snippet 3:
    greeting = “hi”
    ```

* For the function shown below, add exception handling to gracefully process negative integers and floating-point numbers.

    ```ruby
    def fact(n):
        total = 1
        for i in range(2, n+1):
            total *= i
        return total
    ```

* Write a function `num(ip)` that accepts a single argument and returns the corresponding integer or floating-point number contained in the argument. Only `int`, `float` and `str` should be accepted as valid input data type. Provide custom error message if the input cannot be converted to a valid number. Examples are shown below:

    ```ruby
    # int example
    >>> num(0x1f)
    31
    # float example
    >>> num(3.32)
    3.32
    # str examples
    >>> num(' \t 52 \t')
    52
    >>> num('3.982e5')
    398200.0

    # wrong data type
    >>> num(['1', '2.3'])
    TypeError: not a valid input data type
    
    # string input that cannot be converted to a valid int/float number
    >>> num('foo')
    ValueError: could not convert string to int or float
    ```

<br>

# Debugging

* Create an empty file named as `math.py`. In the same directory, create another program file that imports the `math` module and then uses some feature, `print(math.pi)` for example. What happens if you execute this program?

<br>

# Testing

* Randomly change the logic of `max_nested_braces` function shown below and see if any of the tests fail.

    ```ruby
    def max_nested_braces(expr):
        max_count = count = 0
        for char in expr:
            if char == '{':
                count += 1
                if count > max_count:
                    max_count = count
            elif char == '}':
                if count == 0:
                    return -1
                count -= 1

        if count != 0:
            return -1
        return max_count

    def test_cases():
        assert max_nested_braces('a*b') == 0
        assert max_nested_braces('a*b+{}') == 1
        assert max_nested_braces('a*{b+c}') == 1
        assert max_nested_braces('{a+2}*{b+c}') == 1
        assert max_nested_braces('a*{b+c*{e*3.14}}') == 2
        assert max_nested_braces('{{a+2}*{b+c}+e}') == 2
        assert max_nested_braces('{{a+2}*{b+{c*d}}+e}') == 3
        assert max_nested_braces('{{a+2}*{{b+{c*d}}+e*d}}') == 4
        assert max_nested_braces('a*b{') == -1
        assert max_nested_braces('a*{b+c}}') == -1
        assert max_nested_braces('}a+b{') == -1
        assert max_nested_braces('a*{b+c*{e*3.14}}}') == -1
        assert max_nested_braces('{{a+2}*{{b}+{c*d}}+e*d}}') == -1

    if __name__ == '__main__':
        test_cases()
        print('all tests passed')
    ```

<br>

# Tuple and Sequence operations

* Given `chars = tuple('hello')`, see what's the output of the expression `chars[0]` and the statement `chars[0] = 'H'`.
* Given `primes = (2, 3, 5, 7, 11)`:
    * what happens if you use `primes[5]` or `primes[-6]`?
    * what happens if you use `primes[:5]` or `primes[-6:]`?
    * is it possible to get the same output as `primes[::-1]` by using an explicit number for `stop` value? If not, why not?
* What do you think will happen for these cases, given `nums = (1, 2)`:
    * `a, b, c = nums`
    * `a, *b, c = nums`
    * `*a, *b = nums`
* Instead of the function shown below, write a custom logic that iterates only once over the input sequence and returns both minimum/maximum values.

    ```ruby
    def min_max(iterable):
        return min(iterable), max(iterable)
    ```

* Change the below snippet to start the index from `1` instead of `0`.

    ```ruby
    nums = (42, 3.14, -2)
    for idx, val in enumerate(nums):
        print(f'{idx}: {val:>5}')
    ```

* For the program shown below:
    * add a default valued argument `initial` which should be used to initialize `total` instead of `0` in the `sum_nums()` function. For example, `sum_nums(3, -8)` should give `-5` and `sum_nums(1, 2, 3, 4, 5, initial=5)` should give `20`.
    * what would happen if you call this modified function as `sum_nums(initial=5, 2)`?
    * what would happen if you have `nums = (1, 2)` and call this function as `sum_nums(*nums, initial=3)`?
    * in what ways does this function differ from the [sum()](https://docs.python.org/3/library/functions.html#sum) built-in function?

    ```ruby
    def sum_nums(*args):
        total = 0
        for n in args:
            total += n
        return total
    ```

* Write a function `inner_product(seq1, seq2)` that returns the sum of product of corresponding elements of the two sequences. For example, the result should be `44` for `(1, 3, 5)` and `(2, 4, 6)` passed as arguments to this function.

<br>

# List

* What happens if you pass an iterable to the `append()` method and a non-iterable value to the `extend()` method on a `list` object? Also, what happens if you pass multiple values to both these methods?
* Check what happens if you pass a `list` value to the `insert()` method. Also, what happens if you pass more than one value?
* Read [docs.python HOWTOs: Sorting](https://docs.python.org/3/howto/sorting.html) and implement the below examples using `operator` module instead of `lambda` expressions.

    ```ruby
    # based on second element of each item
    >>> items = [('bus', 10), ('car', 20), ('jeep', 3), ('cycle', 5)]
    >>> sorted(items, key=lambda e: e[1], reverse=True)
    [('car', 20), ('bus', 10), ('cycle', 5), ('jeep', 3)]

    # based on number of words, assuming space as the word separator
    >>> dishes = ('Poha', 'Aloo tikki', 'Baati', 'Khichdi', 'Makki roti')
    >>> sorted(dishes, key=lambda s: s.count(' '), reverse=True)
    ['Aloo tikki', 'Makki roti', 'Poha', 'Baati', 'Khichdi']
    ```

* Given `nums = [1, 4, 5, 2, 51, 3, 6, 22]`, determine and implement the sorting condition based on the required output shown below:
    * `[4, 2, 6, 22, 1, 5, 51, 3]`
    * `[2, 4, 6, 22, 1, 3, 5, 51]`
    * `[22, 6, 4, 2, 51, 5, 3, 1]`
* For `random.sample()` method, see what happens if you pass a slice size greater than the number of elements present in the input sequence.
* Write a function that returns the product of a sequence of numbers. Empty sequence or sequence containing non-numerical values should raise `TypeError`.
    * `product([-4, 2.3e12, 77.23, 982, 0b101])` should give `-3.48863356e+18`
    * `product(range(2, 6))` should give `120`
    * `product(())` and `product(['a', 'b'])` should raise `TypeError`
* Write a function that removes dunder names from `dir()` output.

    ```ruby
    >>> remove_dunder(list)
    ['append', 'clear', 'copy', 'count', 'extend', 'index',
     'insert', 'pop', 'remove', 'reverse', 'sort']
    >>> remove_dunder(tuple)
    ['count', 'index']
    ```

<br>

# Mutability

* Use `id()` function to verify that the identity of last two elements of `nums_2d` variable in the below example is the same as the identity of both the elements of `last_two` variable.

    ```ruby
    nums_2d = ([1, 3, 2, 10], [1.2, -0.2, 0, 2], [100, 200])
    last_two = nums_2d[-2:]
    ```
* Create a deepcopy of only the first two elements of `nums_2d` object shown below.

    ```ruby
    nums_2d = [[1, 3, 2, 10], [1.2, -0.2, 0, 2], [100, 200]]
    ```

<br>

# Dict

* Given `fruits = dict(banana=12, papaya=5, mango=10, fig=100)`, what do you think will happen when you use `a, *b, c = fruits`?
* Given `nums = [1, 4, 6, 22, 3, 5, 4, 3, 6, 2, 1, 51, 3, 1]`, keep only first occurrences of a value from this list without changing the order of elements. The output should be `[1, 4, 6, 22, 3, 5, 2, 51]`.

<br>

# Set

* Write a function that checks whether an iterable has duplicate values or not.

    ```ruby
    >>> has_duplicates('pip')
    True
    >>> has_duplicates((3, 2))
    False
    ```

* What does your function return for `has_duplicates([3, 2, 3.0])`?

<br>

# Text processing

* Check what happens if you pass multiple string values separated by comma to the `join()` string method instead of an iterable.
* Read the documentation for:
    * `str` methods `translate()` and `maketrans()`
    * built-in function `ord()`
    * [string module](https://docs.python.org/3/library/string.html)
* From `str` documentation, go through all the methods that start with **is**.
* Write a function that checks if two strings are anagrams irrespective of case (assume input is made up of alphabets only).

    ```ruby
    >>> anagram('god', 'Dog')
    True
    >>> anagram('beat', 'table')
    False
    >>> anagram('Beat', 'abet')
    True
    ```

* Read the documentation and implement these formatting examples with equivalent `str` methods.

    ```ruby
    >>> fruit = 'apple'

    >>> f'{fruit:=>10}'
    '=====apple'
    >>> f'{fruit:=<10}'
    'apple====='
    >>> f'{fruit:=^10}'
    '==apple==='

    >>> f'{fruit:^10}'
    '  apple   '
    ```

* Write a function that returns a `list` of words present in the input string.

    ```ruby
    >>> words('"Hi", there! How *are* you? All fine here.')
    ['Hi', 'there', 'How', 'are', 'you', 'All', 'fine', 'here']
    >>> words('This-Is-A:Colon:Separated,Phrase')
    ['This', 'Is', 'A', 'Colon', 'Separated', 'Phrase']
    ```

<br>

# Comprehensions and Generator expressions

* Write a function that returns a dictionary sorted by values in ascending order.

    ```ruby
    >>> marks = dict(Rahul=86, Ravi=92, Rohit=75, Rajan=79, Ram=92)
    >>> sort_by_value(marks)
    {'Rohit': 75, 'Rajan': 79, 'Rahul': 86, 'Ravi': 92, 'Ram': 92}
    ```

* Write a function that returns a `list` of string slices as per the following rules:
    * return the input string as the only element if its length is less than 3 characters
    * otherwise, return all slices that have 2 or more characters

    ```ruby
    >>> word_slices('i')
    ['i']
    >>> word_slices('to')
    ['to']
    >>> word_slices('table')
    ['ta', 'tab', 'tabl', 'table', 'ab', 'abl', 'able', 'bl', 'ble', 'le']
    ```

* Square even numbers and cube odd numbers. For example, `[321, 1, -4, 0, 5, 2]` should give you `[33076161, 1, 16, 0, 125, 4]` as the output.
* Calculate sum of squares of the numbers, only if the square value is less than `50`. Output for `(7.1, 1, -4, 8, 5.1, 12)` should be `43.01`.

<br>

# Dealing with files

* Write a program that reads a known filename `f1.txt` which contains a single column of numbers in Python syntax. Your task is to display the sum of these numbers, which is `10485.14` for the given example.

    ```bash
    $ cat f1.txt 
    8
    53
    3.14
    84
    73e2
    100
    2937
    ```

* Read the documentation for `glob.glob()` and write a program to list all files ending with `.txt` in the current directory as well as sub-directories, recursively.

<br>

# Executing external commands

* Read [subprocess.run documentation](https://docs.python.org/3/library/subprocess.html#subprocess.run) and modify the below `ls` example to:
    * redirect the `stderr` stream to `/dev/null`
    * automatically raise an exception when the exit status is non-zero

    ```ruby
    >>> import subprocess

    >>> process = subprocess.run(('ls', 'xyz.txt'))
    ls: cannot access 'xyz.txt': No such file or directory
    >>> process.returncode
    2
    ```

<br>

# Command line arguments

* Modify the `sum_two_nums.py` program to handle `TypeError` exceptions as well. Instead of the output shown below, inform the user about the error using `sys.exit()` method. 

    ```ruby
    # sum_two_nums.py
    import ast
    import sys

    try:
        num1, num2 = sys.argv[1:]
        total = ast.literal_eval(num1) + ast.literal_eval(num2)
    except ValueError:
        sys.exit('Error: Please provide exactly two numbers as arguments')
    else:
        print(f'{num1} + {num2} = {total}')
    ```

    ```bash
    $ python3.9 sum_two_nums.py 2 [1]
    Traceback (most recent call last):
      File "/home/learnbyexample/Python/programs/sum_two_nums.py", line 6, in <module>
        total = ast.literal_eval(num1) + ast.literal_eval(num2)
    TypeError: unsupported operand type(s) for +: 'int' and 'list'
    ```

* Write a program to accept one or more numbers as cli arguments. Calculate and display the following details about the input — sum, product and average.
* Add `-o, --output` optional argument to store the output in a file for the program shown below.

    ```ruby
    import argparse, sys

    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?',
                        type=argparse.FileType('r'), default=sys.stdin,
                        help="input file to be sorted")
    parser.add_argument('-u', '--unique', action='store_true',
                        help="sort uniquely")
    args = parser.parse_args()

    ip_lines = args.file.readlines()
    if args.unique:
        ip_lines = set(ip_lines)

    op_lines = sorted(ip_lines, key=lambda s: (s.rsplit('.', 1)[-1], s))
    for line in op_lines:
        print(line, end='')
    ```

<br>

# More exercises

If you'd like even more exercises to test your understanding, check out these excellent resources:

* [Exercism](https://exercism.io/tracks/python/exercises), [Practicepython](https://www.practicepython.org/) — beginner friendly, difficulty levels of problems are labeled
* [Codewars](https://www.codewars.com/), [Adventofcode](https://adventofcode.com/), [Projecteuler](https://projecteuler.net/) — more challenging
* [Checkio](https://py.checkio.org/), [Codingame](https://www.codingame.com/start), [Codecombat](https://codecombat.com/) — gaming based challenges
* [/r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer) — not active currently, but there are plenty of past challenges, along with discussions

