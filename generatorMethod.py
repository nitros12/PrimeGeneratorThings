def check_prime():
    while True:
        count1 = (yield)
        count2 = 2
        while count2**2 <= count1:
            if not count1 % count2:
                break
            count2 += 1
        else:
            yield True
            continue
        yield False
        continue

class PrimeRange:
    '''prime range generator

    Arguments
    ------------------
    Start:  first value to start on
    Stop: last value to run
    Step: how many values to jump on
    '''
    def __init__(self, start=0, stop=2, step=1):
        self.start=start
        self.stop=stop
        self.step=step
        self.primer = check_prime()
        self.mygen = self.generator()

    def generator(self):
        for i in range(self.start, self.stop, self.step):
            next(self.primer)
            if self.primer.send(i):
                yield i

    def __iter__(self):
        return self.mygen

    def __next__(self):
        return next(self.mygen)

print("The first few prime numbers are:")
for i in PrimeRange(start=2, stop=50, step=1):
    print(i)
