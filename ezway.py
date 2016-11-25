import math

class NonPrimeFound(Exception):
    pass

print("the first few prime numbers are:")
for i in range(2, 50):
    try:
        for k in range(2, int(math.sqrt(i))):
            if not i % k:
                raise NonPrimeFound
    except NonPrimeFound:
        pass
    else:
        print(i)
