import lib


# Call the sieve of Eratosthenes and sum the primes found.
def compute():
	ans = sum(lib.list_primes(1999999))
	return str(ans)


if __name__ == "__main__":
	print(compute())

