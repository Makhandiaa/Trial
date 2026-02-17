import numpy as np


class FloatConverter:
    """A class that converts floats to integers, sums them, and generates random matrices."""

    def __init__(self):
        """Initialize the FloatConverter."""
        self.sum_value = 0

    def convert_and_sum(self, float_list):
        """
        Convert a list of floats to integers and sum them up.

        Args:
            float_list: List of float numbers

        Returns:
            int: Sum of converted integers
        """
        int_list = [int(f) for f in float_list]
        self.sum_value = sum(int_list)
        return self.sum_value

    def generate_random_matrix(self, rows=2, cols=3, min_val=0, max_val=10):
        """
        Generate a random matrix with specified dimensions.

        Args:
            rows: Number of rows (default: 2)
            cols: Number of columns (default: 3)
            min_val: Minimum value for random numbers (default: 0)
            max_val: Maximum value for random numbers (default: 10)

        Returns:
            numpy.ndarray: Random matrix of shape (rows, cols)
        """
        return np.random.uniform(min_val, max_val, size=(rows, cols))

    def get_sum(self):
        """
        Get the current sum value.

        Returns:
            int: Current sum value
        """
        return self.sum_value


# Executable example
if __name__ == "__main__":
    # Create an instance of FloatConverter
    converter = FloatConverter()

    print("=== Float Converter Example ===\n")

    # Generate a 2x3 random matrix
    print("Generating a 2x3 random matrix:")
    random_matrix = converter.generate_random_matrix()
    print(random_matrix)
    print(f"Matrix shape: {random_matrix.shape}\n")

    # Flatten the matrix to a list of floats
    float_list = random_matrix.flatten().tolist()
    print(f"Flattened float list: {float_list}\n")

    # Convert floats to integers and sum them
    total = converter.convert_and_sum(float_list)
    print(f"Converted to integers and summed: {total}\n")

    # Another example with custom float list
    print("=== Custom Float List Example ===\n")
    custom_floats = [3.7, 5.2, 8.9, 1.3, 4.6]
    print(f"Input floats: {custom_floats}")

    # Convert to integers first to show the conversion
    converted = [int(f) for f in custom_floats]
    print(f"Converted to integers: {converted}")

    result = converter.convert_and_sum(custom_floats)
    print(f"Sum: {result}")

    print("Makhandia")
    print("racey")
    # tesing out 

    #test skills


#another test



#testing skils
    print ()