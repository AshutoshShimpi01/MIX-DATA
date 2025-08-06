
FUNCTIONS
----------


Fantastic question! Many people struggle with **when and how to use functions**, how **parameters** work, and how to **call** them. Let’s break it down in the simplest way possible.

---

## ✅ PART 1: Why and When Should You Use a Function?

Think of a **function** as a **reusable tool**.

### Ask yourself:

| Situation                   | Ask Yourself                                          | Should You Use a Function? |
| --------------------------- | ----------------------------------------------------- | -------------------------- |
| You repeat the same logic   | "Will I do this again?"                               | ✅ YES                      |
| You want to organize code   | "Is this logic separate?"                             | ✅ YES                      |
| You want inputs and outputs | "Do I want to pass values in and get something back?" | ✅ YES                      |

---

### 💡 Examples:

#### ❌ Bad:

```python
a = 5
b = 7
sum = a + b
print(sum)

x = 10
y = 15
sum2 = x + y
print(sum2)
```

#### ✅ Better (with function):

```python
def add(a, b):         # define function
    return a + b        # logic

print(add(5, 7))        # call it
print(add(10, 15))      # reuse it
```

---

## ✅ PART 2: Understanding Parameters, Arguments, and Function Calls

| Term          | Meaning                              | Example            |
| ------------- | ------------------------------------ | ------------------ |
| **Function**  | Block of reusable code               | `def greet():`     |
| **Parameter** | Placeholder variable inside function | `def greet(name):` |
| **Argument**  | Actual value you pass in             | `greet("Ashu")`    |

---

### 🔧 Example: Function With Parameter

```python
def greet(name):             # 'name' is the parameter
    print("Hello", name)

greet("Ashu")                # "Ashu" is the argument
greet("Shubhendra")
```

---

## ✅ PART 3: How to Think About Using Functions (Step-by-Step)

Let’s take an example: **Check if a number is even.**

---

### 🧠 Think:

1. Will I check this for many numbers? → Yes
2. Do I want to give a number and get True/False? → Yes
3. That means: **input → logic → output** → Use a function ✅

---

### 🛠️ Code:

```python
def is_even(num):          # input
    return num % 2 == 0    # logic + output

# calling
print(is_even(10))         # Output: True
print(is_even(7))          # Output: False
```

---

## ✅ PART 4: Types of Functions You’ll Write

| Type                    | Description                 | Example                              |
| ----------------------- | --------------------------- | ------------------------------------ |
| No input, no output     | Just runs some code         | `def greet(): print("Hello")`        |
| Input, no output        | Takes input, just prints    | `def greet(name): print("Hi", name)` |
| Input + Output          | Takes input, returns result | `def add(a, b): return a + b`        |
| No input, returns value | Used for fetching data      | `def get_name(): return "Ashu"`      |

---

## ✅ PART 5: Calling a Function Correctly

Always remember:

```python
# Define first
def function_name(parameters):
    # logic
    return result

# Then call it later
function_name(arguments)
```

If you **call before defining**, Python gives an error.

---

## ✍️ Try This — Practice Time

Can you write a function that:

1. Takes a number and returns its square
2. Takes a list and returns only even numbers
3. Takes a string and returns it in uppercase

Let me know which one you want to try, and I’ll help you build it step by step!
