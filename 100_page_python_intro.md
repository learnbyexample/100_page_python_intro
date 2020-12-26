# Preface

This book is a short, introductory guide for the Python programming language.

## Prerequisites

You should be already familiar with basic programming concepts. If you are new to programming, I'd highly recommended these resources to get started:

* [Think Python](https://greenteapress.com/wp/think-python-2e/) — gives you a solid foundation to programming, teaches debugging right the beginning, includes case studies, exercises, etc
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/) — teaches you programming concepts and then shows how to automate everyday problems

Or, if you prefer certification courses:

* [Harvard CS50: Introduction to Computer Science](https://www.edx.org/course/cs50s-introduction-to-computer-science) — self paced course on edx. Languages include C, Python, SQL, and JavaScript plus CSS and HTML
* [MIT: Introduction to Computer Science and Programming Using Python](https://www.edx.org/course/introduction-to-computer-science-and-programming-7) — self paced course on edx

See my curated list [py_resources](https://learnbyexample.github.io/py_resources/) for many more learning resources on various Python topics.

## Conventions

* The examples presented here have been tested with **Python version 3.9.0** and includes features that are not available in earlier versions.
* Code snippets that are copy pasted from the Python REPL shell have been modified for presentation purposes. For example, comments to provide context and explanations, blank lines and shortened error messages to improve readability and so on.
* A comment with filename will be shown as the first line for program files.
* External links are provided for further exploration throughout the book. They have been chosen with care to provide resources with more detailed discussion on those topics.

## Acknowledgements

* [Offical Python website](https://docs.python.org/3/) — documentation and examples
* [stackoverflow](https://stackoverflow.com/) and [unix.stackexchange](https://unix.stackexchange.com/) — for getting answers to pertinent questions on Python, Shell and programming in general
* [/r/learnpython](https://www.reddit.com/r/learnpython) — helpful forum for beginners
* [/r/Python/](https://www.reddit.com/r/Python/) — general Python discussion
* [tex.stackexchange](https://tex.stackexchange.com/) — for help on `pandoc` and `tex` related questions
* [LibreOffice Draw](https://www.libreoffice.org/discover/draw/) — cover image
* [pngquant](https://pngquant.org/) and [svgcleaner](https://github.com/RazrFalcon/svgcleaner) for optimizing images
* [Warning](https://commons.wikimedia.org/wiki/File:Warning_icon.svg) and [Info](https://commons.wikimedia.org/wiki/File:Info_icon_002.svg) icons by [Amada44](https://commons.wikimedia.org/wiki/User:Amada44) under public domain

## Feedback and Errata

I would highly appreciate if you'd let me know how you felt about this book, it would help to improve this book as well as my future attempts. Also, please do let me know if you spot any error or typo.

Issue Manager: [https://github.com/learnbyexample/100_page_python_intro/issues](https://github.com/learnbyexample/100_page_python_intro/issues)

E-mail: learnbyexample.net@gmail.com

Twitter: https://twitter.com/learn_byexample

## Author info

Sundeep Agarwal is a freelance trainer, author and mentor. His previous experience includes working as a Design Engineer at Analog Devices for more than 5 years. You can find his other works, primarily focused on Linux command line, text processing, scripting languages and curated lists, at [https://github.com/learnbyexample](https://github.com/learnbyexample). He has also been a technical reviewer for [Command Line Fundamentals](https://www.packtpub.com/application-development/command-line-fundamentals) book and video course published by Packt.

**List of books:** https://learnbyexample.github.io/books/

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Code snippets are available under [MIT License](https://github.com/learnbyexample/100_page_python_intro/blob/main/LICENSE)

Images mentioned in Acknowledgements section above are available under original licenses.

## Book version

1.0

# Introduction

[Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language)) does a great job of describing about Python in a few words. So, I'll just copy-paste relevant information here:

>Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
>
>Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.
>
>As of December 2020 Python ranked third in TIOBE’s index of most popular programming languages, behind `C` and `Java`.

>![info](./images/info.svg) See also [docs.python: General Python FAQ](https://docs.python.org/3/faq/general.html) for answers to questions like "What is Python?", "What is Python good for?", "Why is it called Python?", etc.

## Installation

On modern Linux distributions, you are likely to find Python already installed. It may be a few versions behind, but should work just fine for most of the topics covered in this book. To get the exact version used here, visit [Python downloads page](https://www.python.org/downloads/) and install using the appropriate source for your operating system. Should you face any issues in installing, search online for a solution. Yes, that is something I expect you should be able to do as a prerequisite for this book, i.e. you should have prior experience with basic programming and computer usage.

>![info](./images/info.svg) See [docs.python: What's New](https://docs.python.org/3/whatsnew/index.html) to track changes across versions. As mentioned in the Preface chapter, **3.9.0** is the version used in this book.

## Online tools

In case you are facing installation issues, or do not want to install Python on your computer for some reason, there are plenty of options to execute Python programs using online tools. Some of the popular ones are listed below:

* [Repl.it](https://repl.it/languages/python3) — Interactive playground. Code, collaborate, compile, run, share, and deploy Python and more online from your browser
* [Pythontutor](http://www.pythontutor.com/visualize.html#mode=edit) — Visualize code execution, also has example codes and ability to share sessions
* [PythonAnywhere](https://www.pythonanywhere.com/) — Host, run, and code Python in the cloud

The [offical Python website](https://www.python.org/) also has a *Launch Interactive Shell* option ([https://www.python.org/shell/](https://www.python.org/shell/)), which gives access to a REPL session.

## First program

It is customary to start learning a new programming language by printing a simple phrase. Create a new directory, say `Python/programs` for this book. Then, create a plain text file named `hello.py` with your favorite text editor and type the following piece of code.

```ruby
# hello.py
print('*************')
print('Hello there!')
print('*************')
```

If you are familiar with using command line on a Unix-like system, run the script as shown below. Other options to execute a Python program will be discussed in the next section.

```bash
$ python3.9 hello.py
*************
Hello there!
*************
```

A few things to note here. The first line is a comment, used here to indicate the name of the Python program. `print()` is a built-in function, which can be used without having to load some library. A single string argument has been used for each of the three invocations. `print()` automatically appends a newline character by default. The program ran without a compilation step. As quoted earlier, Python is an *interpreted* language. More details will be discussed in later chapters.

>![info](./images/info.svg) All the Python programs discussed in this book, along with related text files, can be accessed from my GitHub repo [learnbyexample: 100_page_python_intro](https://github.com/learnbyexample/100_page_python_intro). However, I highly recommend typing the programs manually by yourself.

## IDE and text editors

An **integrated development environment** (IDE) might suit you better if you are not comfortable with the command line. IDE provides features likes debugging, syntax highlighting, autocompletion, code refactoring and so on. They also help in setting up **virtual environment** to manage different versions of Python and modules (more on that later).

If you install Python on Windows, it will automatically include **IDLE**, an IDE built using Python's `tkinter` module. On Linux, see if you already have the program `idle3.9`. Otherwise you may have to install it separately, for example, `sudo apt install idle-python3.9` on Ubuntu.

When you open IDLE, you'll get a Python shell (discussed in the next section). For now, click the **New File** option under **File** menu to open a text editor. Type the short program `hello.py` discussed in the previous section. After saving the code, press **F5** to run it. You'll see the results in the shell window.

Screenshots from the text editor and the Python shell are shown below.

![hello.py program on IDLE editor](./images/hello.png)

![Python shell example with output from an executed program](./images/Python_shell_run.png)

Popular alternatives to IDLE are listed below:

* [Thonny](https://thonny.org/) — Python IDE for beginners, lots of handy features like viewing variables, debugger, step through, highlight syntax errors, name completion, etc
* [Pycharm](https://www.jetbrains.com/pycharm/) — smart code completion, code inspections, on-the-fly error highlighting and quick-fixes, automated code refactorings, rich navigation capabilities, support for frameworks, etc
* [Spyder](https://www.spyder-ide.org/) — typically used for scientific computing
* [Jupyter](https://jupyter.org/) — web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text
* [VSCodium](https://vscodium.com/) — community-driven, freely-licensed binary distribution of VSCode
* [Vim](https://github.com/vim/vim), [Emacs](https://www.gnu.org/software/emacs/), [Geany](https://www.geany.org/), [Gedit](https://wiki.gnome.org/Apps/Gedit) — text editors with support for syntax highlighting and more

## REPL

One of the best features of Python is the interactive shell. Such shells are also referred to as REPL, which is an abbreviation for **R**ead **E**valuate **P**rint **L**oop. The Python REPL makes it easy for beginners to try out code snippets for learning purposes. Beyond learning, it is also useful for developing a program in small steps, debugging a large program by trying out few lines of code at a time and so on. REPL will be used frequently in this book to show code snippets.

When you launch Python from the command line, or open IDLE, you get a shell that is ready for user input after the `>>>` prompt.

```bash
$ python3.9
Python 3.9.0 (default, Dec  2 2020, 10:42:13) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Try the below instructions. The first one displays a greeting using the `print()` function. Then, a user defined variable is used to store a string value. To display the value, you can either use `print()` again or just type the variable name. Expression results are immediately displayed in the shell. Name of a variable by itself is a valid expression. This behavior is unique to the REPL and an expression by itself won't display anything when used inside a script.

```ruby
>>> print('have a nice day')
have a nice day

>>> username = 'learnbyexample'
>>> print(username)
learnbyexample

# use # to start a single line comment
# note that string representation is shown instead of actual value
# details will be discussed later
>>> username
'learnbyexample'

# use exit() to close the shell, can also use Ctrl+D shortcut
>>> exit()
```

I'll stress again the importance of following along the code snippets by manually typing them on your computer. Programming requires hands-on experience too, reading alone isn't enough. As an analogy, can you learn to drive a car by just reading about it? Since one of the prerequisite is that you should already be familiar with programming basics, I'll extend the analogy to learning to drive a different car model. Or, perhaps a different vehicle such as a truck or a bus might be more appropriate here.

>![info](./images/info.svg) Depending on the command line shell you are using, you might have the `readline` library that makes it easier to use the REPL. For example, `up` and `down` arrow keys to browse code history, re-execute them (after editing if necessary), search history, autocomplete based on first few characters and so on. See [wikipedia: GNU readline](https://en.wikipedia.org/wiki/GNU_Readline) and [wiki.archlinux: readline](https://wiki.archlinux.org/index.php/readline) for more information.

## Documentation and getting help

The offical Python website has an extensive documentation located at [https://docs.python.org/3/](https://docs.python.org/3/). This includes a tutorial, which is much more comprehensive than the contents presented in this book, several guides for specific modules like `re` and `argparse` and various other information.

Here's a couple of annotated screenshots:

![Python documentation: part 1](./images/py_docs_1.png)

![Python documentation: part 2](./images/py_docs_2.png)

Python provides a `help()` function, which is quite handy to use from the REPL. If you type `help(print)` and press the Enter key, you'll get a screen as shown below. If you are using IDLE, the output would be displayed on the same screen. Otherwise, the content might be shown on a different screen depending on your `pager` settings. Typically, pressing the `q` key will quit the `pager` and get you back to the shell.

![help print](./images/help_print.png)

If you get stuck with a problem, there are several ways to get it resolved. For example:

1. read/search for that particular topic from documentation/books/tutorials/etc 
2. reduce the code as much as possible so that you are left with minimal code necessary to reproduce the issue
3. talk about the problem with a friend/colleague/inanimate-objects/etc (see [Rubber duck debugging](https://rubberduckdebugging.com/))
4. search about the problem online

You can also ask for help on forums. Make sure to read the instructions provided by the respective forums before asking a question. See also [how to ask smart-questions](http://catb.org/~esr/faqs/smart-questions.html#before). Here's some forums you can use:

* [/r/learnpython](https://www.reddit.com/r/learnpython) and [/r/learnprogramming/](https://www.reddit.com/r/learnprogramming/) — beginner friendly
* [python-forum](https://python-forum.io/) — dedicated Python forum, encourages back and forth discussions based on the topic of the thread
* [/r/Python/](https://www.reddit.com/r/Python/) — general Python discussion
* [stackoverflow: python tag](https://stackoverflow.com/tags/python)

>![info](./images/info.svg) The [Debugging](#debugging) chapter will discuss more on this topic.

# Numeric data types

Python is a dynamically typed language. The interpreter infers the data type of a value based on pre-determined rules. In the previous chapter, **string** values were coded using single quotes around a sequence of characters. Similarly, there are rules by which you can declare different numeric data types.

## int

Integer numbers are made up of digits `0` to `9` and can be prefixed with **unary** operators like `+` or `-`. There is no restriction to the size of numbers that can be used, only limited by the memory available on your system. Here's some examples:

```ruby
>>> 42
42
>>> 0
0
>>> +100
100
>>> -5
-5
```

For readability purposes, you can use underscores in between the digits.

```ruby
>>> 1_000_000_000
1000000000
```

>![warning](./images/warning.svg) Underscore cannot be used as the first or last character, and cannot be used consecutively.

## float

Here's some examples for floating-point numbers.

```ruby
>>> 3.14
3.14
>>> -1.12
-1.12
```

Python also supports the exponential notation. See [wikipedia: E scientific notation](https://en.wikipedia.org/wiki/Scientific_notation#E_notation) for details about this form of expressing numbers.

```ruby
>>> 543.15e20
5.4315e+22
>>> 1.5e-5
1.5e-05
```

Unlike integers, floating-point numbers have a limited precision. Python will automatically convert very small or very large floating-point numbers to the exponential notation.

```ruby
>>> 0.0000000001234567890123456789
1.2345678901234568e-10
>>> 31415926535897935809629384623048923.649234324234
3.1415926535897936e+34
```

>![info](./images/info.svg) You might also get seemingly strange results as shown below. See [docs.python: Floating Point Arithmetic Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html) and [stackoverflow: Is floating point math broken?](https://stackoverflow.com/questions/588004/is-floating-point-math-broken) for details and workarounds.

```ruby
>>> 3.14 + 2
5.140000000000001
```

## Arithmetic operators

All arithmetic operators you'd typically expect are available. If any operand is a floating-point number, result will be of `float` data type. Use `+` for addition, `-` for subtraction, `*` for multiplication and `**` for exponentiation. As mentioned before, REPL is quite useful for learning purposes. It makes for a good calculator for number crunching as well. You can also use `_` to refer to the result of the previous expression (this is applicable only in the REPL, not in Python scripts).

```ruby
>>> 25 + 17
42
>>> 10 - 8
2
>>> 25 * 3.3
82.5
>>> 32 ** 42
1645504557321206042154969182557350504982735865633579863348609024

>>> 5 + 2
7
>>> _ * 3
21
```

There are two operators for division. Use `/` if you want a floating-point result. Using `//` between two integers will give only the integer portion of the result (no rounding).

```ruby
>>> 4.5 / 1.5
3.0
>>> 5 / 3
1.6666666666666667
>>> 5 // 3
1
```

Use modulo operator `%` to get the remainder. Sign of the result is same as the sign of the second operand.

```ruby
>>> 5 % 3
2

>>> -5 % 3
1
>>> 5 % -3
-1
>>> 6.5 % -3
-2.5
```

>![info](./images/info.svg) See [docs.python: Binary arithmetic operations](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) and [stackoverflow: modulo operation on negative numbers](https://stackoverflow.com/questions/3883004/the-modulo-operation-on-negative-numbers-in-python) for more details.

Arithmetic operator precedence follows the familiar **PEMDAS** or **BODMAS** abbreviations. Precedence, higher to lower is listed below:

* Expression inside parentheses
* exponentiation
* multiplication, division, modulo
* addition, subtraction

Expression is evaluated left-to-right when operators have the same precedence. Unary operator precedence is between exponentiation and multiplication/division operators. See [docs.python: Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence) for complete details.

## Integer formats

The integer examples so far have been coded using base 10, i.e. **decimal** format. Python has provision for representing **binary**, **octal** and **hexadecimal** formats as well. To distinguish between these different formats, a prefix is used.

* `0b` or `0B` for binary
* `0o` or `0O` for octal
* `0x` or `0X` for hexadecimal

All four formats fall under the `int` data type. Underscores can be used for readability for any of these formats.

```ruby
>>> 0b1000_1111
143
>>> 0o10
8
>>> 0x10
16

>>> 5 + 0xa
15
```

As a consequence, decimal format numbers cannot be prefixed by `0`, other than `0` itself.

```ruby
>>> 00000
0

>>> 09
  File "<stdin>", line 1
    09
     ^
SyntaxError: leading zeros in decimal integer literals are not permitted;
             use an 0o prefix for octal integers
```

If code execution hits a snag, you'll get an error message along with the code snippet that the interpreter thinks caused the issue. In Python parlance, an **exception** has occurred. The exception has a name (`SyntaxError` in the above example) followed by the error message. See [Exception handling](#exception-handling) chapter for more details.

## Other numeric types

Python's standard data type also includes complex type (imaginary part is suffixed with the character `j`). Others like `decimal` and `fractions` are provided as modules.

* [docs.python: complex](https://docs.python.org/3/library/stdtypes.html#typesnumeric)
* [docs.python: decimal](https://docs.python.org/3/library/decimal.html)
* [docs.python: fractions](https://docs.python.org/3/library/fractions.html)

>![warning](./images/warning.svg) Some of the numeric types can have alphabets like `e`, `b`, `j`, etc in their values. As Python is a dynamically typed language, you cannot use variable names beginning with a number. Otherwise, it would be impossible to evaluate an expression like `result = initial_value + 0x12 - 2j`.

>![info](./images/info.svg) There are many third-party libraries that are useful for number crunching in mathematical context, engineering applications, etc. See my list [py_resources: Scientific computing](https://learnbyexample.github.io/py_resources/domain.html#scientific-computing) for curated resources.

# Strings and user input

This chapter will discuss various ways to specify string literals. After that, you'll see how to get input data from the user and handle type conversions.

## Single and double quoted strings

The most common way to declare string literals is by enclosing a sequence of characters within single or double quotes. Unlike other scripting languages like **Bash**, **Perl** and **Ruby**, there is no feature difference between these forms. Idiomatically, single quotes are preferred and other variations are used when needed.

REPL will again be used predominantly in this chapter. One important detail to note is that the result of an expression is displayed using the syntax of that particular data type. Use `print()` function when you want to see how a string literal looks visually.

```ruby
>>> 'hello'
'hello'

>>> print("world")
world
```

If the string literal itself contains single or double quote characters, the other form can be used.

```ruby
>>> print('"Will you come?" he asked.')
"Will you come?" he asked.

>>> print("it's a fine sunny day")
it's a fine sunny day
```

What to do if a string literal has both single and double quotes? You can use the `\` character to escape the quote characters. In the below examples, `\'` and `\"` will evaluate to `'` and `"` characters respectively, instead of prematurely terminating the string definition. Use `\\` if a literal backslash character is needed.

```ruby
>>> print('"It\'s so pretty!" can I get one?')
"It's so pretty!" can I get one?

>>> print("\"It's so pretty!\" can I get one?")
"It's so pretty!" can I get one?
```

In general, the backslash character is used to construct escape sequences. For example, `\n` represents the newline character, `\t` is for tab character and so on. You can use `\ooo` and `\xhh` to represent 256 characters in octal and hexadecimal formats respectively. For Unicode characters, you can use `\N{name}`, `\uxxxx` and `\Uxxxxxxxx` formats. See [docs.python: String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#strings) for full list of escape sequences and details about undefined ones.

```ruby
>>> greeting = 'hi there.\nhow are you?'
>>> greeting
'hi there.\nhow are you?'
>>> print(greeting)
hi there.
how are you?

>>> print('item\tquantity')
item    quantity

>>> print('\u03b1\u03bb\u03b5\N{LATIN SMALL LETTER TURNED DELTA}')
αλεƍ
```

## Triple quoted strings

You can also declare multiline strings by enclosing the value with three single/double quote characters. If backslash is the last character of a line, then a newline won't be inserted at that position. Here's a Python program named `triple_quotes.py` to illustrate this concept.

```ruby
# triple_quotes.py
print('''hi there.
how are you?''')

student = '''\
Name:\tlearnbyexample
Age:\t25
Dept:\tCSE'''

print(student)
```

Here's the output of the above script:

```bash
$ python3.9 triple_quotes.py
hi there.
how are you?
Name:   learnbyexample
Age:    25
Dept:   CSE
```

>![info](./images/info.svg) See [Docstrings](#docstrings) section for another use of triple quoted strings.

## Raw strings

For certain cases, escape sequences would be too much of a hindrance to workaround. For example, filepaths in Windows use `\` as the delimiter. Another would be regular expressions, where the backslash character has yet another special meaning. Python provides a **raw** string syntax, where all the characters are treated literally. This form, also known as **r-strings** for short, requires a `r` or `R` character prefix to quoted strings. Forms like triple quoted strings and raw strings are for user convenience. Internally, there's just a single representation for string literals. 

```ruby
>>> print(r'item\tquantity')
item\tquantity

>>> r'item\tquantity'
'item\\tquantity'
>>> r'C:\Documents\blog\monsoon_trip.txt'
'C:\\Documents\\blog\\monsoon_trip.txt'
```

Here's an example with `re` built-in module. The `import` statement used below will be discussed in [Modules](#modules) chapter. See my book [Python re(gex)?](https://github.com/learnbyexample/py_regular_expressions) for details on regular expressions.

```ruby
>>> import re

# numbers >= 100 with optional leading zeros
>>> re.findall(r'\b0*[1-9]\d{2,}\b', '0501 035 154 12 26 98234')
['0501', '154', '98234']

# without raw strings
>>> re.findall('\\b0*[1-9]\d{2,}\\b', '0501 035 154 12 26 98234')
['0501', '154', '98234']
```

## String operators

Python provides a wide variety of features to work with strings. This chapter introduces some of them, like the `+` and `*` operators in this section. Here's some examples to concatenate strings using the `+` operator. The operands can be any expression that results in a string value and you can use any of the different ways to specify a string literal.

```ruby
>>> str1 = 'hello'
>>> str2 = ' world'
>>> str3 = str1 + str2
>>> print(str3)
hello world

>>> str3 + r'. 1\n2'
'hello world. 1\\n2'
```

Another way to concatenate is to simply place any kind of string literal next to each other. You can use zero or more whitespaces between the two literals. But you cannot mix an expression and a string literal. If the strings are inside parentheses, you can also use newline to separate the literals and optionally use comments.

```ruby
>>> 'hello' r' 1\n2\\3'
'hello 1\\n2\\\\3'

# note that ... is REPL's indication for multiline statements, blocks, etc
>>> print('hi '
... 'there')
hi there
```

You can repeat a string by using the `*` operator between a string and an integer.

```ruby
>>> style_char = '-'
>>> print(style_char * 50)
--------------------------------------------------
>>> word = 'buffalo '
>>> print(8 * word)
buffalo buffalo buffalo buffalo buffalo buffalo buffalo buffalo 
```

## String formatting

As per [PEP 20: The Zen of Python](https://www.python.org/dev/peps/pep-0020/),

>There should be one-- and preferably only one --obvious way to do it.

However, there are several approaches for formatting strings. This section will primarily discuss **formatted** string literals (**f-strings** for short). And then show alternate approaches.

f-strings allow you to embed an expression within `{}` characters as part of the string literal. Like raw strings, you need to use a prefix, which is `f` or `F` in this case. Python will substitute the embeds with the result of the expression, converting it to string if necessary (such as numeric results). See [docs.python: Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings) and [docs.python: Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals) for documentation and more examples.

```ruby
>>> str1 = 'hello'
>>> str2 = ' world'
>>> f'{str1}{str2}'
'hello world'

>>> f'{str1}({str2 * 3})'
'hello( world world world)'
```

A recent feature allows you to add `=` after an expression to get both the expression and the result in the output.

```ruby
>>> num1 = 42
>>> num2 = 7

>>> f'{num1 + num2 = }'
'num1 + num2 = 49'
>>> f'{num1 + (num2 * 10) = }'
'num1 + (num2 * 10) = 112'
```

Optionally, you can provide a format specifier along with the expression after a `:` character. These specifiers are similar to the ones provided by `printf()` function in **C** language, `printf` built-in command in **Bash** and so on. Here's some examples for numeric formatting.

```ruby
>>> appx_pi = 22 / 7

# restricting number of digits after the decimal point
>>> f'Approx pi: {appx_pi:.5f}'
'Approx pi: 3.14286'

# rounding is applied
>>> f'{appx_pi:.3f}'
'3.143'

# exponential notation 
>>> f'{32 ** appx_pi:.2e}'
'5.38e+04'
```

Here's some alignment examples:

```ruby
>>> fruit = 'apple'

>>> f'{fruit:=>10}'
'=====apple'
>>> f'{fruit:=<10}'
'apple====='
>>> f'{fruit:=^10}'
'==apple==='

# default is space character
>>> f'{fruit:^10}'
'  apple   '
```

You can use `b`, `o` and `x` to display integer values in binary, octal and hexadecimal formats respectively. Using `#` before these characters will result in appropriate prefix for these formats.

```ruby
>>> num = 42

>>> f'{num:b}'
'101010'
>>> f'{num:o}'
'52'
>>> f'{num:x}'
'2a'

>>> f'{num:#x}'
'0x2a'
```

`str.format()` method, `format()` function and `%` operator are alternate approaches for string formatting.

```ruby
>>> num1 = 22
>>> num2 = 7

>>> 'Output: {} / {} = {:.2f}'.format(num1, num2, num1 / num2)
'Output: 22 / 7 = 3.14'

>>> format(num1 / num2, '.2f')
'3.14'

>>> 'Approx pi: %.2f' % (num1 / num2)
'Approx pi: 3.14'
```

>![info](./images/info.svg) See [docs.python: The String format() Method](https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method) and the sections that follow for more details about the above features. The [String methods](#string-methods) chapter will discuss more about the string processing methods.

>![info](./images/info.svg) In case you don't know what a *method* is, see [stackoverflow: What's the difference between a method and a function?](https://stackoverflow.com/questions/155609/whats-the-difference-between-a-method-and-a-function)

## User input

The `input` built-in function can be used to get data from the user. It also allows an optional string to make it an interactive process. It always returns a string data type, you can convert to another type as discussed in the next section.

```ruby
# Python will wait until you type your data and press the Enter key
# the blinking cursor is represented by a rectangular block shown below
>>> name = input('what is your name? ')
what is your name? █
```

Here's the rest of the above example.

```ruby
>>> name = input('what is your name? ')
what is your name? learnbyexample

# note that newline isn't part of the value saved in the 'name' variable
>>> print(f'pleased to meet you {name}.')
pleased to meet you learnbyexample.
```

## Type conversion

The `type()` built-in function can be used to know what data type you are dealing with. You can pass any expression as an argument.

```ruby
>>> type(42)
<class 'int'>

>>> num = 3.14
>>> type(num)
<class 'float'>

>>> type('Hi there')
<class 'str'>
```

The built-in functions `int()`, `float()` and `str()` can be used to convert from one data type to another. These function names are the same as their data type class names seen above.

```ruby
>>> num = 3.14
>>> int(num)
3
# you can also use f'{num}'
>>> str(num)
'3.14'

>>> usr_ip = input('enter a float value ')
enter a float value 45.24e22
>>> type(usr_ip)
<class 'str'>
>>> float(usr_ip)
4.524e+23
```

>![info](./images/info.svg) See [docs.python: Built-in Functions](https://docs.python.org/3/library/functions.html) for documentation on all of the built-in functions. You can also use `help()` function from the REPL as discussed in the [Documentation and getting help](#documentation-and-getting-help) section.

## Exercises

* Read about **Bytes** literals from [docs.python: String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#strings). See also [stackoverflow: What is the difference between a string and a byte string?](https://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string)
* If you check out [docs.python: int() function](https://docs.python.org/3/library/functions.html#int), you'll see that the `int()` function accepts an optional argument. As an example, write a program that asks the user for hexadecimal number as input. Then, use `int()` function to convert the input string to an integer (you'll need the second argument for this). Add `5` and display the result in hexadecimal format.
* Write a program to accept two input values. First can be either a number or a string value. Second is an integer value, which should be used to display the first value in centered alignment. You can use any character you prefer to surround the value, other than the default space character.
* What happens if you use a combination of `r`, `f` and other such valid prefix characters while declaring a string literal? What happens if you use raw strings syntax and provide only a single `\` character? Does the documentation describe these cases?
* Try out at least two format specifiers not discussed in this chapter.

# Defining functions

This chapter will discuss how to define your own functions, pass arguments to them and get back results. You'll also learn more about the `print()` built-in function.

## def keyword

Use `def` keyword to define a function. The function name is specified after the keyword, followed by arguments inside parentheses and finally a `:` character to end the definition. It is a common mistake for beginners to miss the `:` character. Arguments are optional, as shown in the below program.

```ruby
# no_args.py
def greeting():
    print('-----------------------------')
    print('         Hello World         ')
    print('-----------------------------')

greeting()
```

The above code defines a function named `greeting` and contains three statements. Unlike many other programming languages, whitespaces are significant in Python. Instead of a pair of curly braces, indentation is used to distinguish the body of the function and statements outside of that function. Typically, 4 spaces is used, as shown above. The function call `greeting()` has the same indentation level as the function definition, so it is not part of the function. For readability, an empty line is used to separate the function definition and subsequent statements.

```bash
$ python3.9 no_args.py
-----------------------------
         Hello World         
-----------------------------
```

>![info](./images/info.svg) Functions have to be declared before they can be called. As an exercise, call the function before declaration and see what happens for the above program.

>![info](./images/info.svg) As per [PEP 8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/), it is recommended to use two blank lines around top level functions. However, I prefer to use a single blank line. For large projects, specialized tools like [pylint](https://pypi.org/project/pylint/) and [black](https://pypi.org/project/black/) are used to analyze and enforce coding styles/guidelines.

>![info](./images/info.svg) To create a placeholder function, you can use the `pass` statement to indicate no operation. See [docs.python: pass statement](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement) for details.

## Accepting arguments

Functions can accept one or more arguments, specified as comma separated variable names.

```ruby
# with_args.py
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

In this script, the function from the previous example has been modified to accept an input string as the sole argument. The `len()` built-in function is used here to get the length of a string value. The code also showcases the usefulness of variables, string operators and string formatting.

```bash
$ python3.9 with_args.py
------------
     hi     
------------
------------------------------------------
     Today would be a nice, sunny day     
------------------------------------------
```

As an exercise, modify the above program as suggested below and observe the results you get.

* add print statements for `ip`, `op_length` and `styled_line` variables after the function calls
* pass a numeric value to the `greeting()` function
* don't pass any argument while calling the `greeting()` function

>![info](./images/info.svg) The argument variables, and those that are defined within the body, are local to the function and would result in an exception if used outside the function. See also [docs.python: Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example) and [docs.python: global statement](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement).

>![info](./images/info.svg) Python being a dynamically typed language, it is up to you to sanitize input for correctness. See also [docs.python: Support for type hints](https://docs.python.org/3/library/typing.html) and [realpython: Python Type Checking Guide](https://realpython.com/python-type-checking/).


## Default valued arguments

A default value can be specified during the function definition. Such arguments can be skipped during the function call, in which case they'll use the default value. Here's an example:

```ruby
# default_args.py
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

There are various ways in which you can call functions with default values. If you specify the argument name, they can be passed in any order. But, if you pass values positionally, the order has to be same as the declaration.

```bash
$ python3.9 default_args.py
------------
     hi     
------------
--------
  bye   
--------
===============
     hello     
===============
::::::::::
 good day 
::::::::::
```

As an exercise, modify the above script for the below requirements.

* make the spacing work for multicharacter `style` argument
* accept another argument with a default value of single space character that determines the character to be used around the centered `ip` value

## Return value

The default return value of a function is `None`, which is typically used to indicate the absence of a meaningful value. The `print()` function, for example, has a `None` return value. Functions like `int()`, `len()` and `type()` have specific return values, as seen in prior examples.

```ruby
>>> print('hi')
hi
>>> value = print('hi')
hi

>>> value
>>> print(value)
None
>>> type(value)
<class 'NoneType'>
```

Use the `return` statement to explicitly give back a value to the function caller. You can use this keyword by itself as well, the expression is optional.

```ruby
>>> def num_square(n):
...     return n * n
... 
>>> num_square(5)
25
>>> num_square(3.14)
9.8596

>>> op = num_square(-42)
>>> type(op)
<class 'int'>
```

>![info](./images/info.svg) On encountering a `return` statement, the function will be terminated and further statements, if any, present as part of the function body will not be executed.

>![info](./images/info.svg) A common beginner confusion is mixing up `print()` and `return`. See [stackoverflow: What is the formal difference between “print” and “return”?](https://stackoverflow.com/questions/7664779/what-is-the-formal-difference-between-print-and-return) for examples and explanations.

## A closer look at the print() function

The `help` documentation for the `print()` function is shown below.

![help print](./images/help_print.png)

As you can see, there are four default valued arguments. But, what does `value, ...,` mean? It indicates that the `print()` function can accept arbitrary number of arguments. Here's some examples:

```ruby
# newline character is appended even if no arguments are passed
>>> print()

>>> print('hi')
hi
>>> print('hi', 5)
hi 5

>>> word1 = 'loaf'
>>> word2 = 'egg'
>>> print(word1, word2, 'apple roast nut')
loaf egg apple roast nut
```

If you observe closely, you'll notice that a **space** character is inserted between the arguments. That separator can be changed by using the `sep` argument.

```ruby
>>> print('hi', 5, sep='')
hi5
>>> print('hi', 5, sep=':')
hi:5
>>> print('best', 'years', sep='.\n')
best.
years
```

Similarly, you can change the string that gets appended to something else.

```ruby
>>> print('hi', end='----\n')
hi----
>>> print('hi', 'bye', sep='-', end='\n======\n')
hi-bye
======
```

>![info](./images/info.svg) The `file` and `flush` arguments will be discussed later. Writing your own function to accept arbitrary number of arguments will also be discussed later.

## Docstrings

Triple quoted strings are also used for multiline comments and to document various part of a Python script. This is achieved by adding help content within triple quotes at the start of a function, class, etc. Such literals are known as documentation strings, or **docstrings** for short. The `help()` function reads these docstrings to display the documentation. There are also numerous third-party tools that make use of docstrings.

Here's an example:

```ruby
>>> def num_square(n):
...     """
...     Returns the square of a number.
...     """
...     return n * n
... 
>>> help(num_square)
```

Calling `help(num_square)` will give you the documentation as shown below.

```bash
num_square(n)
    Returns the square of a number.
```

>![info](./images/info.svg) See [docs.python: Documentation Strings](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings) for usage guidelines and other details.

