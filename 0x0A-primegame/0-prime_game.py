#!/usr/bin/python3

""" Prim Game Algorithm Python """


def isWinner(n, nums):
    """ Checks who wins the game """
    ben = 0
    maria = 0
    x = 0
    while x < n:
        prime = sieve_era(nums[x - 1])
        len_prime = len(prime)

        if nums[x] == 1:
            ben += 1
        elif len_prime % 2 == 0:
            ben += 1
        elif len_prime % 2 != 0:
            maria += 1

        x += 1

    if ben > maria:
        return 'Ben'
    elif ben < maria:
        return 'Maria'
    else:
        return None


def sieve_era(n):
    """ Sieve of Erastosthenes algorithm
    which generates prime numbers
    """
    prime = [True] * (n+1)
    prime_nums = []
    p = 2
    while (p * p <= n):

        if prime[p] is True:
            for i in range(p*p, n + 1, p):
                prime[i] = False

        p += 1

    for i in range(2, n+1):
        if prime[i]:
            prime_nums.append(i)
    return prime_nums
