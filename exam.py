import random
java=[
  {
    "question": "What is the output of the following code?\n\npublic class Example {\n    public static void main(String[] args) {\n        int x = 5;\n        System.out.println(x++);\n        System.out.println(++x);\n    }\n}",
    "options": ["5, 7", "6, 6", "6, 7", "5, 6"],
    "correct_answer": "a"
  },
  {
    "question": "Which keyword is used to explicitly call the superclass constructor in a subclass?",
    "options": ["this", "base", "super", "parent"],
    "correct_answer": "c"
  },
  {
    "question": "What is the correct way to declare a method that doesn't return any value?",
    "options": ["void myMethod()", "int myMethod()", "String myMethod()", "float myMethod()"],
    "correct_answer": "a"
  },
  {
    "question": "Which loop is guaranteed to execute at least once?",
    "options": ["for loop", "while loop", "do-while loop", "if-else loop"],
    "correct_answer": "c"
  },
  {
    "question": "Which data structure stores elements in key-value pairs?",
    "options": ["List", "Set", "Map", "Array"],
    "correct_answer": "c"
  },
  {
    "question": "What does the 'static' keyword mean in Java?",
    "options": ["It makes a method non-static.", "It makes a variable non-static.", "It allows access to private members.", "It indicates the main method."],
    "correct_answer": "b"
  },
  {
    "question": "Which exception is thrown when a class is not found during runtime?",
    "options": ["ClassNotFoundException", "FileNotFoundException", "ClassCastException", "NullPointerException"],
    "correct_answer": "a"
  },
  {
    "question": "What is the purpose of the 'finally' block in a try-catch-finally statement?",
    "options": ["To catch exceptions", "To execute code after try block", "To prevent exceptions", "To handle finally-related exceptions"],
    "correct_answer": "b"
  },
  {
    "question": "Which operator is used to concatenate strings in Java?",
    "options": ["&", "+", "*", "%"],
    "correct_answer": "b"
  },
  {
    "question": "What is the output of the following code?\n\npublic class Example {\n    public static void main(String[] args) {\n        int[] numbers = {1, 2, 3, 4, 5};\n        System.out.println(numbers[3]);\n    }\n}",
    "options": ["1", "2", "3", "4"],
    "correct_answer": "d"
  },
  {
    "question": "Which access modifier provides the widest accessibility?",
    "options": ["private", "protected", "default", "public"],
    "correct_answer": "d"
  },
  {
    "question": "What is the purpose of the 'break' statement in a loop?",
    "options": ["To exit the loop and continue with the next iteration", "To continue with the next iteration of the loop", "To skip a loop iteration", "To terminate the program"],
    "correct_answer": "a"
  },
  {
    "question": "Which class is used to create a thread in Java?",
    "options": ["Thread", "Runnable", "Executor", "Process"],
    "correct_answer": "a"
  },
  {
    "question": "What is the output of the following code?\n\npublic class Example {\n    public static void main(String[] args) {\n        String str = \"Hello, World!\";\n        System.out.println(str.charAt(7));\n    }\n}",
    "options": ["W", "r", "o", "l"],
    "correct_answer": "a"
  },
  {
    "question": "Which method is used to compare two objects for equality in Java?",
    "options": ["equals()", "compare()", "compareTo()", "isEqual()"],
    "correct_answer": "a"
  },
  {
    "question": "Which statement is used to handle exceptions in Java?",
    "options": ["try", "test", "throw", "exception"],
    "correct_answer": "a"
  },
  {
    "question": "What is the correct way to declare a class in Java?",
    "options": ["new class MyClass {}", "public class {MyClass}", "class MyClass {}", "class = MyClass {}"],
    "correct_answer": "c"
  },
  {
    "question": "What does JVM stand for?",
    "options": ["Java Virtual Machine", "Just Virtual Machine", "Java Variable Machine", "Just Variable Machine"],
    "correct_answer": "a"
  },
  {
    "question": "Which data structure uses the 'First In, First Out' (FIFO) principle?",
    "options": ["Queue", "Stack", "Array", "List"],
    "correct_answer": "a"
  },
  {
    "question": "What is the purpose of the 'static' keyword in a Java method?",
    "options": ["It indicates the method is abstract.", "It allows the method to access instance variables.", "It allows the method to be called without creating an instance.", "It makes the method synchronized."],
    "correct_answer": "c"
  }
]
c=[
  {
    "question": "What is the output of the following C code?\n\n#include <stdio.h>\nint main() {\n    int x = 5;\n    printf(\"%d %d\", x++, ++x);\n    return 0;\n}",
    "options": ["5 5", "6 6", "5 6", "6 5"],
    "correct_answer": "b"
  },
  {
    "question": "Which keyword is used to define a constant in C?",
    "options": ["define", "const", "constant", "final"],
    "correct_answer": "b"
  },
  {
    "question": "What is the purpose of the 'break' statement in a switch-case construct?",
    "options": ["To exit the loop", "To continue to the next iteration", "To exit the switch-case construct", "To restart the loop"],
    "correct_answer": "c"
  },
  {
    "question": "Which operator is used to access the value pointed by a pointer?",
    "options": ["*", "&", "->", "<-"],
    "correct_answer": "a"
  },
  {
    "question": "What is the correct way to declare a function that doesn't return any value?",
    "options": ["void myFunction()", "int myFunction()", "float myFunction()", "string myFunction()"],
    "correct_answer": "a"
  },
  {
    "question": "Which data structure uses the 'Last In, First Out' (LIFO) principle?",
    "options": ["Queue", "Stack", "Array", "List"],
    "correct_answer": "b"
  },
  {
    "question": "What is the output of the following C code?\n\n#include <stdio.h>\nint main() {\n    int arr[] = {1, 2, 3, 4, 5};\n    printf(\"%d\", arr[3]);\n    return 0;\n}",
    "options": ["1", "2", "3", "4"],
    "correct_answer": "d"
  },
  {
    "question": "Which header file should be included to use the 'malloc' function?",
    "options": ["<memory>", "<stdlib>", "<malloc>", "<alloc>"],
    "correct_answer": "b"
  },
  {
    "question": "What is the purpose of the 'continue' statement in a loop?",
    "options": ["To exit the loop", "To skip the current iteration", "To terminate the program", "To restart the loop"],
    "correct_answer": "b"
  },
  {
    "question": "What is the correct syntax to declare a pointer to an integer?",
    "options": ["pointer int *p;", "int *p;", "int p;", "ptr int *p;"],
    "correct_answer": "b;"
  },
  {
    "question": "Which keyword is used to indicate the end of a function in C?",
    "options": ["finish", "end", "return", "terminate"],
    "correct_answer": "c"
  },
  {
    "question": "What is the purpose of the 'sizeof' operator in C?",
    "options": ["It returns the size of a variable.", "It returns the address of a variable.", "It returns the value of a variable.", "It returns the type of a variable."],
    "correct_answer": "a"
  },
  {
    "question": "Which type of loop is executed at least once?",
    "options": ["for loop", "while loop", "do-while loop", "if-else loop"],
    "correct_answer": "c"
  },
  {
    "question": "What is the purpose of the 'void' keyword in a function declaration?",
    "options": ["To specify the return type", "To indicate the function is empty", "To declare a pointer", "To define a variable"],
    "correct_answer": "a"
  },
  {
    "question": "Which operator is used to access the memory address of a variable?",
    "options": ["&", "*", "#", "$"],
    "correct_answer": "a"
  },
  {
    "question": "What does 'EOF' stand for in C?",
    "options": ["End of Function", "End of File", "End of Format", "End of Find"],
    "correct_answer": "b"
  },
  {
    "question": "What is the output of the following C code?\n\n#include <stdio.h>\nint main() {\n    int x = 10;\n    if (x > 5) {\n        printf(\"Hello\");\n    }\n    printf(\"World\");\n    return 0;\n}",
    "options": ["Hello", "World", "HelloWorld", "No output"],
    "correct_answer": "c"
  },
  {
    "question": "Which function is used to read a character from the standard input in C?",
    "options": ["getc()", "readchar()", "input()", "scanf()"],
    "correct_answer": "a"
  },
  {
    "question": "What is the correct way to declare an array of integers in C?",
    "options": ["array[10]", "int array[10]", "array = [10]", "int array = [10]"],
    "correct_answer": "b"
  },
  {
    "question": "What is the purpose of the 'sizeof' function in C?",
    "options": ["To calculate the size of a data type", "To calculate the length of a string", "To calculate the number of elements in an array", "To calculate the sum of elements in an array"],
    "correct_answer": "a"
  }
]
sc=[
  {
    "question": "What is the output of the following JavaScript code?\n\nlet x = 5;\nconsole.log(x++);\nconsole.log(x++);",
    "options": ["5 5", "6 7", "5 6", "6 5"],
    "correct_answer": "b"
  },
  {
    "question": "Which keyword is used to declare a constant in JavaScript?",
    "options": ["const", "let", "var", "constant"],
    "correct_answer": "a"
  },
  {
    "question": "What is the purpose of the 'break' statement in a loop?",
    "options": ["To exit the loop", "To continue to the next iteration", "To exit the loop block", "To restart the loop"],
    "correct_answer": "c"
  },
  {
    "question": "What is the correct way to declare a function in JavaScript?",
    "options": ["function myFunction()", "myFunction()", "func myFunction()", "void myFunction()"],
    "correct_answer": "a"
  },
  {
    "question": "Which operator is used to access the value of a property in an object?",
    "options": ["=>", ".", "::", "->"],
    "correct_answer": "b"
  },
  {
    "question": "What is the purpose of the 'typeof' operator in JavaScript?",
    "options": ["To check if a variable is defined", "To check the type of a variable", "To assign a variable", "To compare two variables"],
    "correct_answer": "b"
  },
  {
    "question": "What is the output of the following JavaScript code?\n\nlet arr = [1, 2, 3, 4, 5];\nconsole.log(arr[3]);",
    "options": ["1", "2", "3", "4"],
    "correct_answer": "d"
  },
  {
    "question": "Which method is used to add an element to the end of an array in JavaScript?",
    "options": ["push()", "add()", "insert()", "append()"],
    "correct_answer": "a"
  },
  {
    "question": "What does the 'NaN' value represent in JavaScript?",
    "options": ["Null and None", "Not a Number", "No Assignment", "Negative"],
    "correct_answer": "b"
  },
  {
    "question": "Which data structure stores elements in key-value pairs?",
    "options": ["List", "Set", "Map", "Array"],
    "correct_answer": "c"
  },
  {
    "question": "What is the purpose of the 'this' keyword in JavaScript?",
    "options": ["To create a new variable", "To refer to the current object", "To access a global variable", "To indicate a function"],
    "correct_answer": "b"
  },
  {
    "question": "What is the correct way to declare a variable in JavaScript?",
    "options": ["variable x;", "x = 5;", "let x;", "x = let;"],
    "correct_answer": "c"
  },
  {
    "question": "What is the purpose of the 'null' value in JavaScript?",
    "options": ["To represent an empty value", "To indicate an error", "To represent infinity", "To indicate a function"],
    "correct_answer": "a"
  },
  {
    "question": "Which function is used to round a number to the nearest integer in JavaScript?",
    "options": ["round()", "floor()", "ceil()", "truncate()"],
    "correct_answer": "a"
  },
  {
    "question": "What is the output of the following JavaScript code?\n\nconsole.log(typeof null);",
    "options": ["object", "null", "undefined", "string"],
    "correct_answer": "a"
  },
  {
    "question": "Which operator is used to compare two values for equality in JavaScript?",
    "options": ["==", "===", "!=", "<>"],
    "correct_answer": "b"
  },
  {
    "question": "What is the purpose of the 'async' keyword in JavaScript?",
    "options": ["To declare a variable", "To indicate an asynchronous function", "To create a loop", "To access an external file"],
    "correct_answer": "b"
  },
  {
    "question": "What is the output of the following JavaScript code?\n\nconsole.log(2 + '2');",
    "options": ["4", "22", "2", "Error"],
    "correct_answer": "b"
  },
  {
    "question": "Which function is used to convert a string to lowercase in JavaScript?",
    "options": ["toLower()", "toLowerCase()", "lowercase()", "convertToLower()"],
    "correct_answer": "b"
  },
  {
    "question": "What is the purpose of the 'length' property in JavaScript arrays?",
    "options": ["To get the number of elements in an array", "To access the first element", "To remove the last element", "To check if the array is empty"],
    "correct_answer": "a"
  }
]
a=[
  {
    "question": "What is the output of the following code?\nx = 10\ny = x\nx += 5\nprint(x + y)",
    "options": [
      "15",
      "20",
      "25",
      "10"
    ],
    "answer": "c"
  },
  {
    "question": "Which of the following is true about Python's Global Interpreter Lock (GIL)?",
    "options": [
      "It allows multiple threads to execute in parallel.",
      "It prevents multiple threads from executing Python bytecode at once.",
      "It ensures that Python code runs faster on multi-core processors.",
      "It is only present in the CPython implementation."
    ],
    "answer": "b"
  },
  {
    "question": "What is the result of the expression: `2 ** 3 ** 2`?",
    "options": [
      "64",
      "512",
      "81",
      "9"
    ],
    "answer": "b"
  },
  {
    "question": "In Python, what is the purpose of the `super()` function?",
    "options": [
      "It returns the parent class of an object.",
      "It calls the constructor of the parent class.",
      "It is used to access superclass attributes.",
      "It is a keyword to indicate inheritance."
    ],
    "answer": "b"
  },
  {
    "question": "What will be the value of `x` after the following code?\nx = [1, 2, 3]\nx = x * 2\nx[0] = 10",
    "options": [
      "[10, 2, 3, 10, 2, 3]",
      "[10, 10, 3]",
      "[10, 2, 3, 1, 2, 3]",
      "[1, 2, 3, 10, 10, 3]"
    ],
    "answer": "a"
  },
  {
    "question": "What does the `global` keyword do in Python?",
    "options": [
      "It declares a variable as having a global scope.",
      "It imports global functions from other modules.",
      "It specifies that a function should be accessible globally.",
      "It defines a variable to be used only within a specific scope."
    ],
    "answer": "a"
  },
  {
    "question": "What is the purpose of the `itertools` module in Python?",
    "options": [
      "It provides functions for file I/O operations.",
      "It offers tools for creating GUI applications.",
      "It includes functions for working with iterators and generators.",
      "It is used for handling networking operations."
    ],
    "answer": "c"
  },
  {
    "question": "Which sorting algorithm has the worst-case time complexity of O(n log n) in Python's `sorted()` function?",
    "options": [
      "Quick Sort",
      "Merge Sort",
      "Bubble Sort",
      "Insertion Sort"
    ],
    "answer": "b"
  },
  {
    "question": "What is the output of the following code?\nnum = 2\nresult = num << 2 + num >> 2\nprint(result)",
    "options": [
      "2",
      "8",
      "3",
      "4"
    ],
    "answer": "b"
  },
  {
    "question": "In Python, what is the purpose of the `__slots__` attribute in a class?",
    "options": [
      "It specifies a list of methods that are accessible from outside the class.",
      "It is used to define read-only attributes for instances of the class.",
      "It restricts the attributes that can be added dynamically to instances.",
      "It enables access to private attributes from subclasses."
    ],
    "answer": "c"
  },
  {
    "question": "What is the result of the expression: `sum([i * i for i in range(5)])`?",
    "options": [
      "0",
      "10",
      "30",
      "55"
    ],
    "answer": "c"
  },
  {
    "question": "Which module in Python is used to measure the execution time of code?",
    "options": [
      "timeit",
      "timing",
      "timer",
      "datetime"
    ],
    "answer": "a"
  },
  {
    "question": "What is the output of the following code?\nnumbers = [1, 2, 3, 4]\nresult = [x * 2 for x in numbers if x % 2 == 0]\nprint(result)",
    "options": [
      "[2, 4, 6, 8]",
      "[4, 8]",
      "[2, 6]",
      "[1, 2, 3, 4]"
    ],
    "answer": "2"
  },
  {
    "question": "What is the purpose of the `__exit__()` method in Python context managers?",
    "options": [
      "It is called when entering the context.",
      "It is used to clean up resources when exiting the context.",
      "It is a special method to create context managers.",
      "It is responsible for handling exceptions within the context."
    ],
    "answer": "b"
  },
  {
    "question": "Which statement is true about Python's `asyncio` library?",
    "options": [
      "It is used for parsing JSON data.",
      "It is used for creating graphical user interfaces.",
      "It provides support for asynchronous programming using coroutines.",
      "It is used for unit testing."
    ],
    "answer": "c"
  },
  {
    "question": "What is the output of the following code?\nprint(*map(lambda x: x ** 2, range(5))))",
    "options": [
      "0 1 4 9 16",
      "1 4 9 16 25",
      "0 1 4 9",
      "0 1 2 3 4"
    ],
    "answer": "a"
  },
  {
    "question": "What is the purpose of the `collections.Counter` class in Python?",
    "options": [
      "It is used to define counters for loop iterations.",
      "It is used to count the number of elements in an iterable.",
      "It is used to count the number of instances of a specific class.",
      "It is a decorator to create counters for functions."
    ],
    "answer": "b"
  },
    {
    "question": "What is the output of the following code?\ndef foo(x, y=[]):\n    y.append(x)\n    return y\n\nprint(foo(2))\nprint(foo(3))",
    "options": [
      "[2, 3]",
      "[2]",
      "[3]",
      "[2, 3, 3]"
    ],
    "answer": "a"
  },
  {
    "question": "In Python, what is the purpose of the `__new__()` method in a class?",
    "options": [
      "It is called before the `__init__()` method to create an instance.",
      "It is used to create new objects based on existing ones.",
      "It is used to destroy instances of a class.",
      "It is called after the `__init__()` method to finalize an instance."
    ],
    "answer": "a"
  },
  {
    "question": "What is the result of the expression: `lambda x: x if x > 0 else 0`?",
    "options": [
      "It creates a function that returns `x` if `x` is positive, otherwise returns 0.",
      "It creates a function that returns `x` if `x` is negative, otherwise returns 0.",
      "It creates a function that returns 0 if `x` is positive, otherwise returns `x`.",
      "It creates a function that returns the absolute value of `x`."
    ],
    "answer": "a"
  }
]


sc=random.sample(sc,20)
c=random.sample(c,20)
a=random.sample(a,20)
java=random.sample(java,20)
cques=[]
ckey=[]
javaques=[]
pques=[]
javakey=[]
sckey=[]
scques=[]
pkey=[]
for q in range(len(c)):
  cques.append(c[q]['question'])
  ckey.append(c[q]['correct_answer'])
for q in range(len(java)):
  javaques.append(java[q]['question'])
  javakey.append(java[q]['correct_answer'])
for q in range(len(sc)):
  scques.append(sc[q]['question'])
  sckey.append(sc[q]['correct_answer'])
for q in range(len(a)):
  pques.append(a[q]['question'])
  pkey.append(a[q]['answer'])
points=[0]
def result(option,key):
  if option=='1':
    for i in range(20):
      if key[i]==ckey[i]:
        points[0]=points[0]+1
  elif option=='2':
    for i in range(20):
      if key[i]==sckey[i]:
        points[0]=points[0]+1
  elif option=='3':
    for i in range(20):
      if key[i]==javakey[i]:
        points[0]=points[0]+1
  elif option=='4':
    for i in range(20):
      if key[i]==pkey[i]:
        points[0]=points[0]+1
  return points[0]

