class Vector:
    def __init__(self, v, w, c):
        self.w = w
        self.v = v
        self.c = c

    def add_vectors(self, v, w):
        return [vi + wi for vi, wi in zip(v, w)]

    def sub_vectors(self, v, w):
        return [vi - wi for vi, wi in zip(v, w)]

    def constant_multiply(self, c, v):
        return [c * vi for vi in v]

    def scalar_multiply(self, v, w):
        return sum(vi * wi for vi, wi in zip(v, w))

    def len_vector(self, v):
        return len(v)

    def index_elem(self, c, v):
        return v[c]

    def stroka_vector(self, v):
        return ' '.join(str(e) for e in v)

    def compare(self, v, w, true='equal', false='non_equal', ):
        for i in range(self.len_vector(v)):
            if self.index_elem(i, v) == self.index_elem(i, w):
                continue
            elif self.index_elem(i, v) != self.index_elem(i, w):
                return false
        return true


vector1 = Vector([3, 5, 6], [3, 5, 10], 20)
print(vector1.sub_vectors([3, 5, 6], [3, 5, 10]))
print(vector1.add_vectors([3, 5, 6], [3, 5, 10]))
print(vector1.constant_multiply(20, [3, 5, 6]))
print(vector1.scalar_multiply([3, 5, 6], [3, 5, 10]))
print(vector1.len_vector([3, 5, 6]))
print(vector1.index_elem(2, [3, 5, 6]))
print(vector1.stroka_vector([3, 5, 6]))
print(vector1.compare([3, 5, 6], [3, 5, 10], true='equal', false="non_equal"))

