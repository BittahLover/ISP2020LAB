from Task3.task3 import add_vectors
from Task3.task3 import sub_vectors

first = [3, 5, 6]
second = [3, 5, 10]

format_vectors = add_vectors(first, second)
format_vectors_wrong = sub_vectors(first, second)

print("\nformat vectors = " + str(format_vectors))
print("\nformat vectors = " + str(format_vectors_wrong))