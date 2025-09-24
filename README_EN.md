# PyTest_001_Calculator_App
Calculator: Test of basic math operations including exception handling

A simple calculator project in Python with functions `add`, `subtract`, `multiply`, and `divide`.  
The project includes a set of unit tests written with **pytest** and also runs within **GitHub Actions** CI/CD.

---

## Installation

Clone the repository and install the package in editable mode:

```bash
git clone https://github.com/your-username/calculator.git
cd calculator
pip install -e .
```

---

## Usage

```python
from calculator.calculator import add, subtract, multiply, divide

print(add(2, 3))       # 5
print(subtract(10, 4)) # 6
print(multiply(3, 7))  # 21
print(divide(8, 2))    # 4.0
```

---

## Testing

Tests are written with **pytest**.

Run all tests:

```bash
pytest
```

Run only a specific test:

```bash
pytest tests/test_calculator.py::test_add
```

---

## 📂 Project Structure

```
calculator/                  # root directory
│
├─ README.md                 # project documentation in CZ
├─ README_EN.md              # project documentation in EN
├─ pytest.ini                # pytest marks, testpaths = tests
├─ pyproject.toml            # build system (setuptools)
├─ setup.cfg                 # package configuration
├─ .gitignore                # version control filter
│
├─ src/
│   └─ calculator/
│       ├─ __init__.py       # imports functions from calculator.py
│       └─ calculator.py     # source file with add, subtract, multiply, divide functions
│
├─ tests/
│   ├─ __init__.py           # empty file
│   ├─ conftest.py           # defines pytest fixtures
│   ├─ test_calculator.py    # simple tests of basic operations
│   ├─ test_param.py         # parameterized tests of basic operations
│   ├─ test_fixtures.py      # tests with simple and parameterized fixtures
│   ├─ test_divide_zero.py   # tests for ZeroDivideError exception (with/without messages, non-parameterized)
│   └─ test_param_exc_divide.py # parameterized tests for DivideZeroError exception
│
└─ .github/
    └─ workflows/
        └─ ci.yml            # GitHub Actions workflow for pytest
```

---

## ⚙️ CI/CD

The project uses **GitHub Actions**.  
The workflow in `.github/workflows/ci.yml` runs pytest for Python 3.9, 3.10, and 3.11 on every push and pull request.

---

## 📝 License

MIT License – see the [LICENSE](LICENSE) file (if included).
