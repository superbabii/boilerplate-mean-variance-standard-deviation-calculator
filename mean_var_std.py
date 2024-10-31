import numpy as np

def calculate(numbers):
    # Check if the input list has exactly 9 elements
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list to a 3x3 Numpy array
    matrix = np.array(numbers).reshape(3, 3)
    
    # Create the dictionary to store results
    calculations = {
        'mean': [
            list(matrix.mean(axis=0)),
            list(matrix.mean(axis=1)),
            matrix.mean().tolist()
        ],
        'variance': [
            list(matrix.var(axis=0)),
            list(matrix.var(axis=1)),
            matrix.var().tolist()
        ],
        'standard deviation': [
            list(matrix.std(axis=0)),
            list(matrix.std(axis=1)),
            matrix.std().tolist()
        ],
        'max': [
            list(matrix.max(axis=0)),
            list(matrix.max(axis=1)),
            matrix.max().tolist()
        ],
        'min': [
            list(matrix.min(axis=0)),
            list(matrix.min(axis=1)),
            matrix.min().tolist()
        ],
        'sum': [
            list(matrix.sum(axis=0)),
            list(matrix.sum(axis=1)),
            matrix.sum().tolist()
        ]
    }
    
    return calculations
