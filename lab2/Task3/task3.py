def add_vectors(v, w):
    return [vi + wi for vi, wi in zip(v, w)]


def sub_vectors(v, w):
    return [vi - wi for vi, wi in zip(v, w)]


def constant_multiply(c, v):
    return [c * vi for vi in v]


def scalar_multiply(v, w):
    return sum(vi * wi for vi, wi in zip(v, w))


def len_vector(v):
    return len(v)


def index_elem(c, v):
    return v[c]


def stroka_vector(v):
    return ' '.join(str(e) for e in v)


def compare(v, w, true='equal', false='non_equal', ):
    for i in range(len_vector(v)):
        if index_elem(i, v) == index_elem(i, w):
            continue
        elif index_elem(i, v) != index_elem(i, w):
            return false
    return true


python_list_1 = [3, 5, 6]
python_list_2 = [3, 5, 10]
print(constant_multiply(20, python_list_2))
print(add_vectors(python_list_1, python_list_2))
print(sub_vectors(python_list_1, python_list_2))
print(scalar_multiply(python_list_1, python_list_2))
print(len_vector(python_list_2))
print(index_elem(2, python_list_1))
print(stroka_vector(python_list_1))
print(compare(python_list_2, python_list_1))
