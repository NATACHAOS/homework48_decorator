"""Сложить 3 числа и определить простое оно или составное"""


def is_prime(func):
    def wrapper(*args):
        k = 0
        gen_result = sum(args)
        for i in range(2, gen_result // 2 + 1):
            if (gen_result % i == 0):
                k = k + 1
        if (k <= 0):
            print("Число простое")
        else:
            print("Число не является простым")

        return gen_result

    return wrapper


@is_prime
def sum_three(*args):
    result = sum(args)
    return result


result = sum_three(2, 3, 6)
print(result)