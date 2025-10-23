```markdown
# Python Data Structures - Practice Lab (Practice by myself for learning...)

Hands-on practice materials for core Python data structures.  
This folder contains simple, well-commented examples for **Lists, Tuples, Sets, and Dictionaries**, plus a `PythonExamples` area with small scripts that combine ideas.

---

## 📂 Folder Structure

```

PythonDataStructure/
├─ Dictionaries/      # Key–value basics, methods, nested dicts, safe lookups
├─ Lists/             # Indexing, slicing, list methods, list comps
├─ PythonExamples/    # Small end-to-end examples using multiple structures
├─ Sets/              # Unique collections, set algebra, membership tests
├─ Tuples/            # Immutable sequences, packing/unpacking
└─ README.md

````

> Each subfolder contains one or more `*.py` files. Open them to read comments and run them directly.

---

## 🚀 Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/emrancub/Data-Science-and-Machine-Learning.git
   cd Data-Science-and-Machine-Learning/PythonDataStructure
````

2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Run any example**

   ```bash
   # Example: run a script from the Lists folder
   python Lists/your_script_name.py
   ```

> Requirements: Python 3.8+ (no external packages needed).

---

## 📘 What You’ll Learn

* How to choose the right data structure for a task
* Common operations and their behavior
* Idiomatic Python patterns (comprehensions, unpacking, membership checks)

---

## 🧩 Mini Cheat-Sheet

* **List**: ordered, mutable sequence — great for ordered data you need to edit
  Common ops: append, extend, insert, pop, sort, slice

* **Tuple**: ordered, **immutable** sequence — good for fixed records and safe returns
  Common ops: unpacking, indexing, nested tuples

* **Set**: unordered, unique elements — fast membership and set algebra
  Common ops: add, remove/discard, union/intersection/difference

* **Dict**: key–value mapping — fast lookups by key, flexible nesting
  Common ops: get, keys/values/items, dict comprehensions, `setdefault`

---

## 🏗️ Suggested Practice (checklist)

* [ ] Lists: convert CSV-like text to structured rows
* [ ] Tuples: return multiple values from a function safely
* [ ] Sets: remove duplicates from a list and compare two lists
* [ ] Dicts: count word frequencies and sort by count
* [ ] Examples: build a tiny contact book using dicts + sets

---

## 🧪 How to Add Your Own Examples

1. Pick the right folder (e.g., `Sets/`).
2. Create a file like `set_membership_demo.py`.
3. Include a short docstring at the top explaining the goal.
4. Keep examples **small, runnable, and commented**.

```python
"""
Demonstrates fast membership with sets vs lists.
Run: python Sets/set_membership_demo.py
"""
```

---

## 📄 License

See the [`LICENSE`](./LICENSE) file in this folder for terms.

---

## 🤝 Contributing / Notes

* Keep examples beginner-friendly and self-contained.
* Prefer descriptive filenames (e.g., `list_slicing_basics.py`).
* If you spot an issue, open a PR or create an Issue in the main repo.

---

## ✍️ Author

Maintained by **@emrancub** — learning by building, one example at a time.

