from itertools import zip_longest

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __add__(self, target):
        return Polynomial([sum(i) for i in list(zip_longest(self.coeff, target.coeff, fillvalue=0))])

    def __sub__(self, target):
        return Polynomial([sum(i) for i in list(zip_longest(self.coeff, [j * -1 for j in target.coeff], fillvalue=0))])

    def __call__(self, x):
        return sum([coeff * (x ** power) for power, coeff in enumerate(self.coeff)])

    def __mul__(self, target):
        new_coeffs = [0] * ((len(self.coeff) * len(target.coeff)) - 1)

        for a, b in enumerate(self.coeff):
            for c, d in enumerate(target.coeff):
                new_coeffs[a+c] += (b * d)

        end = len(new_coeffs)

        for i in new_coeffs[::-1]:
            if i == 0:
                end -= 1
            else:
                break

        return Polynomial(new_coeffs[0:end])

    def differentiate(self):
        new_coeffs = [0] * (len(self.coeff) - 1)

        for index, coeff in enumerate(self.coeff):
            new_coeffs[index - 1] += index * coeff

        self.coeff = new_coeffs

    def derivative(self):
        new_coeffs = [0] * (len(self.coeff) - 1)

        for index, coeff in enumerate(self.coeff):
            new_coeffs[index - 1] += index * coeff

        return Polynomial(new_coeffs)