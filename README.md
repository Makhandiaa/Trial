# Float Converter

A Python class that converts floats to integers and generates random matrices using NumPy.

## Features

- Convert lists of floats to integers and calculate their sum
- Generate random matrices with customizable dimensions and value ranges
- Track cumulative sum values

## Requirements

- Python 3.x
- NumPy

## Installation

```bash
pip install numpy
```

## Usage

```python
from float_converter import FloatConverter

# Create an instance
converter = FloatConverter()

# Convert floats to integers and sum them
floats = [3.7, 5.2, 8.9, 1.3, 4.6]
total = converter.convert_and_sum(floats)
print(f"Sum: {total}")  # Output: Sum: 22

# Generate a random matrix
matrix = converter.generate_random_matrix(rows=3, cols=4, min_val=0, max_val=100)
print(matrix)
```

## Running the Example

```bash
python float_converter.py
```

This will run a demonstration showing matrix generation, float conversion, and summation.
