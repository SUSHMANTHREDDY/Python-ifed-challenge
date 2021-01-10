import math 
def nearestPerfectSquare(x):
    if(x<=0):
        return 0
    sr = math.sqrt(x) 
    pk=math.floor(sr)
    pk*=pk
    return pk
