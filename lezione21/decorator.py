class myDecorator:

    @staticmethod
    def elapsedTime(func):
        
        def wrapper(*args):
            import time

            start = time.time()

            func(args)

            print(f"Time elapsed: {time.time() - start}")

        return wrapper

    
    @staticmethod
    def elapsedTimeR(func):
        
        def wrapper(*args):
            import time
            start = time.time()

            ret = func(*args)
            ret1 = time.time() - start

            if isinstance(ret, tuple):
                return ret + (ret1, )

            return ret, ret1

        return wrapper
    


@myDecorator.elapsedTimeR
def prova1(a, b, c):
    return a + b + c

@myDecorator.elapsedTimeR
def prova2(a, b, c):
    return a + b, b + c


print(prova1(1,2,3))
print(prova2(1,2,3))
a, b, e = prova2(1,2,3)
print(a,b, e)




