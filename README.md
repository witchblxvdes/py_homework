# Dynamic Object Analyzer

A Python application designed to dynamically inspect and analyze Python objects using introspection and reflection.

This project was developed as part of a Python programming course.

## Features

The `ObjectAnalyzer` class provides the following functionality:

| Method | Description |
|---|---|
| `get_type(obj)` | Returns the name of the object's type. |
| `get_attributes(obj)` | Returns a list of non-callable attributes, excluding special attributes. |
| `get_methods(obj)` | Returns callable attributes and their method signatures. |
| `get_inheritance(obj)` | Returns the class inheritance hierarchy using MRO. |
| `get_documentation(obj)` | Retrieves the object's documentation using `inspect.getdoc()`. |
| `get_attribute(obj, name)` | Dynamically retrieves an attribute's value. |
| `set_attribute(obj, name, value)` | Creates or updates an object's attribute. |
| `analyze(obj)` | Generates a structured report containing the analysis results. |

## Technologies

- Python 3.10+
- `inspect` — Python standard library
- Pylint — static code analysis
- `assert` — basic functionality checks

No third-party runtime dependencies are required.

## Project Structure

```text
python-homework-13/
├── object_analyzer.py
├── test_object_analyzer.py
└── README.md
```

## Usage

Import the `ObjectAnalyzer` class into your Python script:

```python
from object_analyzer import ObjectAnalyzer


class Player:
    """Represents a game player."""

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def level_up(self):
        self.level += 1


player = Player("Alex", 10)
analyzer = ObjectAnalyzer()

report = analyzer.analyze(player)

print(report)
```

Expected output:

```python
{
    'type': 'Player',
    'attributes': ['level', 'name'],
    'methods': {'level_up': '()'},
    'inheritance': ['Player', 'object'],
    'documentation': 'Represents a game player.'
}
```

## Testing

The project includes basic checks using Python's built-in `assert` statement.

Run the tests:

```bash
python test_object_analyzer.py
```

If all checks pass, the program displays:

```text
All checks passed!
```

## Code Quality

The project has been checked using Pylint.

Install Pylint:

```bash
pip install pylint
```

Run the analysis:

```bash
python -m pylint object_analyzer.py test_object_analyzer.py
```

**Pylint score: 10.00/10**

## Learning Objectives

This project demonstrates the practical use of:

- Python introspection and reflection
- Dynamic attribute access and modification
- Method signatures with `inspect`
- Method Resolution Order (MRO)
- Docstrings and type annotations
- Exception handling
- Basic testing and static code analysis
