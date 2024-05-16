#   KEY WORD ARGS
def esempio_kwargs(**kwargs):    #passo numero arbitrario di parametri
    #kwargs: keyword args

    if "alpha" in kwargs:
        alpha: float = kwargs["alpha"] #kwargs è come un dizionario 
    
    return alpha

#utilizzo
ret = esempio_kwargs(alpha="a", beta="b", gamma="c")

print(ret)

def esempio_args(*args):    #passo numero arbitrario di parametri
    #args: iterative list args

    if len(args) > 0:
        alpha: float = args[0]
    
    return alpha

ret = esempio_kwargs(alpha="a", beta="b", gamma="c")
print(ret)