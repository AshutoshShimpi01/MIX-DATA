Perfect! Understanding **Collections** (also called **Data Structures** or **DS**) in Python is **essential** — they help you store, organize, and manipulate data effectively.

---

# 📦 PYTHON COLLECTIONS (DATA STRUCTURES) – BASICS GUIDE

We’ll cover:

1. ✅ **Lists**
2. ✅ **Tuples**
3. ✅ **Sets**
4. ✅ **Dictionaries**
5. 🧠 When to use which one
6. ⚙️ Common operations
7. 🧪 Practice problems

---

## ✅ 1. **LIST** – Ordered, changeable, allows duplicates

### Syntax:

```python
fruits = ["apple", "banana", "cherry"]
```

### Key Features:

* Can be updated (mutable)
* Supports indexing/slicing
* Can contain different data types

### Common Methods:

```python
fruits.append("orange")     # add at end
fruits.insert(1, "kiwi")    # add at index
fruits.remove("banana")     # remove by value
fruits.pop()                # remove last item
fruits.sort()               # sort in place
```

---

## ✅ 2. **TUPLE** – Ordered, **unchangeable**, allows duplicates

### Syntax:

```python
colors = ("red", "green", "blue")
```

### Key Features:

* Immutable (cannot change after creation)
* Supports indexing/slicing
* Faster than lists for fixed data

### Example:

```python
print(colors[1])            # Access value
```

---

## ✅ 3. **SET** – **Unordered**, changeable, **no duplicates**

### Syntax:

```python
nums = {1, 2, 3, 3, 2}
print(nums)     # {1, 2, 3}
```

### Key Features:

* No duplicates
* Unordered (no indexing)
* Used for membership checks and unique data

### Common Methods:

```python
nums.add(4)
nums.remove(2)
nums.union({5, 6})
nums.intersection({1, 3})
```

---

## ✅ 4. **DICTIONARY** – Key-value pairs, unordered, mutable

### Syntax:

```python
person = {"name": "Ashu", "age": 25, "city": "Pune"}
```

### Key Features:

* Stores data as key-value
* Fast lookup using keys

### Common Methods:

```python
person["age"] = 26              # Update value
person["gender"] = "Male"       # Add new pair
person.pop("city")              # Remove key
print(person.get("name"))       # Safe access
```

---

## 🧠 5. When to Use What?

| Use Case                           | Best Data Structure |
| ---------------------------------- | ------------------- |
| Ordered data with frequent updates | `list`              |
| Fixed, read-only data              | `tuple`             |
| Unique items, no order             | `set`               |
| Key-value mapping                  | `dict`              |

---

## ⚙️ 6. Common Real-Life Patterns

### 🔹 List of student names

```python
students = ["Ram", "Priya", "Ali"]
```

### 🔹 Student marks as key-value

```python
marks = {"Ram": 85, "Priya": 92}
```

### 🔹 Unique cities visited

```python
cities = {"Pune", "Delhi", "Pune"}  # Set: duplicates removed
```

### 🔹 Coordinates (x, y)

```python
point = (4, 5)  # Tuple: fixed pair
```

---

## 🧪 7. Practice Problems

Try these:

1. Create a list of 5 numbers, sort them, and find the max.
2. Store employee info (name, salary) using a dictionary.
3. Remove duplicates from a list using a set.
4. Check if a city exists in a set of cities.
5. Convert a list of tuples into a dictionary: `[("a", 1), ("b", 2)]`

---

## 🔚 Summary Table

| Type  | Ordered          | Mutable | Duplicates | Indexed | Example      |
| ----- | ---------------- | ------- | ---------- | ------- | ------------ |
| List  | ✅                | ✅       | ✅          | ✅       | `["a", "b"]` |
| Tuple | ✅                | ❌       | ✅          | ✅       | `("a", "b")` |
| Set   | ❌                | ✅       | ❌          | ❌       | `{1, 2, 3}`  |
| Dict  | ❌ (3.7+ ordered) | ✅       | ❌ (keys)   | ❌       | `{"a": 1}`   |

---

Would you like to do practice problems for each of these collections next, or get short quizzes with answers?
