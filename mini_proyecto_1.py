import pandas as pd
import random

# Define operations and their corresponding lambda functions
operations = {
    'SUM': None,
    'SUB': None,
    'MUL': None,
    'DIV': None,
    'POW': None  # limit exponent to avoid very large numbers
}

# Generate data
data = []
for _ in range(1000):
    operation = random.choice(list(operations.keys()))
    operand_1 = random.randint(1, 1000)
    operand_2 = random.randint(1, 1000)
    if operation == 'POW' and operand_2 < 10: operand_2 = random.randint(1, 15)
    data.append([operation, operand_1, operand_2])

# Create DataFrame
df = pd.DataFrame(data, columns=['operation', 'operand_1', 'operand_2'])

# Save to CSV
csv_path = './data/math_operations.csv'
df.to_csv(csv_path, index=False)