# Задача 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(num_rows * num_columns):
        row = i // num_columns + 1
        col = i % num_columns + 1
        result = operation(row, col)
        print(f"{result} ", end="")
        if col == num_columns:
            print()
print_operation_table(lambda x, y: x * y)