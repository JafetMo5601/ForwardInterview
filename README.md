## 📦 Thoughtful Robot Package Sorter
This project simulates a robotic arm at Thoughtful’s automation factory that classifies packages based on their size and weight. The robot decides how to dispatch each package into one of three stacks: STANDARD, SPECIAL, or REJECTED.

### ✅ Classification Rules
A package is classified based on the following criteria:
* Bulky if: Volume (width × height × length) is ≥ 1,000,000 cm3, or any single dimension is >= 150 cm
* Heavy if: Mass is >= 20 kg

Stack Dispatching Logic:
* Bulky and Heavy	REJECTED
* Bulky or Heavy	SPECIAL
* Neither	STANDARD

### 🚀 How to Run
Clone or copy the file into a Python environment.

Run the script with: ```python run.py```

### 🧪 Included Features
* Built-in assertions to verify correctness.
* A set of sample packages processed by the robot.
* Descriptive console output that simulates robotic arm dispatch behavior.

📝 Example Output
```
Tests successfully finalized.

Packages to sort by Thoughtful’s robot:

Package number 1, with dimension 50x50x50 cm, and weight of 10kg -> Dispatched to -> STANDARD stack.
Package number 2, with dimension 160x40x40 cm, and weight of 15kg -> Dispatched to -> SPECIAL stack.
Package number 3, with dimension 80x90x90 cm, and weight of 25kg -> Dispatched to -> SPECIAL stack.
Package number 4, with dimension 200x200x200 cm, and weight of 30kg -> Dispatched to -> REJECTED stack.
Package number 5, with dimension 100x100x100 cm, and weight of 19kg -> Dispatched to -> SPECIAL stack.

```
