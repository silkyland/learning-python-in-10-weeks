import math


def get_primes(nums):
    return [num for num in nums if is_prime(num)]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(get_primes([2, 3, 4, 5, 71, 45, 66]))
