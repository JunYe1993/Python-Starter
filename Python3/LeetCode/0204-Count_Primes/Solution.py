class Solution:
    
    def countPrimes(self, n: int) -> int:
        # Based on the Sieve of Eratosthenes
        # We can easily elimiate the non-prime number        
        if n < 3: return 0
        primes = [1]*n
        primes[0] = primes[1] = 0
        num = 2
        while num*num < n:
            if primes[num]:
                # Elimiate all multiple of the prime.     
                for index in range(num*num, n, num):
                    primes[index] = 0
            num += 1
        return sum(primes)

    # 4000ms, first thught.
    def QcountPrimes(self, n: int) -> int:
        # For n = 0, 1, 2 case.
        if n < 3: return 0

        # Loop though 3 ~ n to find every prime number.
        primes = [2]
        for num in range(3, n):
            # Cause is ascending order.
            # If number can be divided by previous prime number,
            # its not prime number
            isPrime = True
            for prime in primes:
                # Note if prime*prime bigger than the number,
                # then there is no rest prime number can divide the number.
                if prime*prime > num: break
                if num % prime == 0:
                    isPrime = False
                    break
            if isPrime: primes.append(num)
        return len(primes)

    