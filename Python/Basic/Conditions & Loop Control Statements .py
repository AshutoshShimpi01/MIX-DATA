Conditions & Loop Control Statements 


Great! Let’s now dive into **Conditions & Loop Control Statements** — the building blocks of logic in Python.

---

# 🧠 Mastering Python Conditions & Loop Control Statements

We'll cover:

1. ✅ `if`, `elif`, `else`
2. 🔁 `for` and `while` loops
3. 🛑 `break`, 🔁 `continue`, and 🔁 `pass`
4. 📘 When and how to use each (with examples)
5. 🎯 Practice patterns

---

## ✅ 1. **Conditional Statements** (`if`, `elif`, `else`)

Used to **make decisions** in code.

### Syntax:

```python
if condition:
    # code if true
elif another_condition:
    # code if that is true
else:
    # code if none are true
```

### Example:

```python
age = 20

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

---

## 🔁 2. **Loops** — `for` and `while`

### 🔹 `for` loop → Use when you **know how many times** to repeat

```python
for i in range(5):  # 0 to 4
    print(i)
```

### 🔹 `while` loop → Use when you **don't know how many times**

```python
n = 1
while n <= 5:
    print(n)
    n += 1
```

---

## 🛠️ 3. **Loop Control Statements**

### 🔸 `break` → stop the loop

```python
for i in range(10):
    if i == 5:
        break
    print(i)   # prints 0 to 4
```

### 🔸 `continue` → skip current iteration

```python
for i in range(5):
    if i == 2:
        continue
    print(i)   # prints 0,1,3,4
```

### 🔸 `pass` → do nothing (placeholder)

```python
for i in range(3):
    pass  # use when block is required but you want to do nothing
```

---

## ⚙️ 4. Common Patterns Using Loops + Conditions

### 🔸 Print all even numbers from 1 to 10

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

---

### 🔸 Sum of all numbers from 1 to 100

```python
total = 0
for i in range(1, 101):
    total += i
print(total)
```

---

### 🔸 Count digits in a number

```python
n = 12345
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)
```

---

### 🔸 Find if a number is prime

```python
n = 13
is_prime = True

for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
```

---

## 📌 5. When to Use What?

| Task                         | Use                  |
| ---------------------------- | -------------------- |
| Decision making              | `if`, `elif`, `else` |
| Repeat known times           | `for` loop           |
| Repeat until condition false | `while` loop         |
| Stop loop early              | `break`              |
| Skip current iteration       | `continue`           |
| Placeholder                  | `pass`               |

---

## 🧠 Mini Challenges for You

Try writing code for:

1. Print numbers 1 to 20, skip multiples of 4
2. Find the factorial of a number using a loop
3. Count how many vowels are in a word
4. Print the first 5 odd numbers

Would you like me to walk you through solving any of them now?
