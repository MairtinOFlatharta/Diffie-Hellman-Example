#!/usr/bin/env python
import argparse
from math import gcd, sqrt, floor
from random import choice, randrange

from endpoint import Endpoint, MitM


quick_prime_check = False


def main():
    global quick_prime_check
    parser = argparse.ArgumentParser(
        description='Demonstrate Diffie-Hellman key algorithm between two '
                    'parties. Also demonstrates a Man-in-the-Middle attack.')

    # Argument that speeds up prime search by introducing tiny chance of
    # returning non-prime number
    parser.add_argument(
        '-q',
        '--quick',
        action='store_true',
        help='Defines method for generating primes between given bounds. '
             'Including this option will check each prime candidate against '
             'all numbers from 2 - square root number. Runs faster than '
             'normal method, but introduces small chance of chosen prime not '
             'actually being a prime number.')

    args = parser.parse_args()

    if args.quick:
        quick_prime_check = True

    prime = get_random_prime(10000, 100000)
    prim_root = get_prim_root(prime)

    # Generate private keys for Bob, Alice and Mallory
    private_key_1, private_key_2, private_key_3 = \
        (randrange(10000, 100000) for i in range(3))

    # Create objects representing 2 legitimate client and a MitM
    bob = Endpoint('Bob', private_key_1, prime, prim_root)
    alice = Endpoint('Alice', private_key_2, prime, prim_root)
    mallory = MitM('Mallory', private_key_3, prime, prim_root)

    # Instantiate public keys
    bob_public = bob.gen_public_key()
    alice_public = alice.gen_public_key()
    mallory_public = mallory.gen_public_key()

    # Generating full session keys between users
    print('=====Bob/Alice connection=====')
    bob.gen_full_key(alice_public)
    alice.gen_full_key(bob_public)

    print(bob)
    print(alice)

    print('=====Bob/Mallory connection=====')
    bob.gen_full_key(mallory_public)
    mallory.gen_full_key(bob_public)

    print(bob)
    print(mallory)

    print('=====Alice/Mallory connection=====')
    alice.gen_full_key(mallory_public)
    mallory.gen_full_key(alice_public)

    print(alice)
    print(mallory)

    # Crack private keys using prime, prime root and public keys
    print('=====Mallory cracking private keys=====')
    mallory.crack_private_key(bob)
    mallory.crack_private_key(alice)


def get_prim_root(prime):
    # Get some random upper bound value for calculated primitive roots
    range_upper_bound = randrange(20, prime)

    # Generate coprime set for this numder
    coprime_set = {x for x in range(1, prime) if gcd(x, prime) == 1}

    # Calculate prime roots in range of 20
    # (Getting all of them takes way too long)
    prim_roots = [r for r in range(range_upper_bound - 20, range_upper_bound)
                  if coprime_set == {pow(r, powers, prime)
                  for powers in range(1, prime)}]

    # Return 1 radnom primitive root
    return choice(prim_roots)


def get_random_prime(lower, upper):
    check_list = None
    # If number is even, add 1 to it. This is so we can check only odd
    # numbers, letting us skip half of the specified range
    if not lower & 1:
        lower += 1

    # Build list of primes if using slower prime checking method
    if not quick_prime_check:
        check_list = build_check_list(upper)

    # Generate all primes between upper and lower. Pick one at random
    prime_list = [x for x in range(lower, upper, 2) if is_prime(x, check_list)]
    return choice(prime_list)


def is_prime(num, check_list=None):
    global quick_prime_check
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True

    # Use quicker method to check primes. Has a 99.382% chance of correctly
    # identifying if a number is not prime in the range of 10,000 - 100,000
    if quick_prime_check:
        for i in range(2, floor(sqrt(num))):
            if num % i == 0:
                return False
        return True

    # When using slower method, build up list of primes that will be used to
    # check if other numbers are prime. This speeds up the process a lot
    if check_list is None:
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        return True

    # Check_list provided, do thorough checks to see if number is prime by
    # performing modulo using all listed prime numbers
    else:
        for i in check_list:
            if i > num // 2:
                return True
            if num % i == 0:
                return False
        return True

    return True


def build_check_list(upper):
    # Before checking primes using slower method, build list of primes from
    # 2 - upper limit/2. This reduces the number of comparisons done without
    # compromising correctness of prime list
    primes = []
    for i in range(2, upper // 2):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == '__main__':
    main()
