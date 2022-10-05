def isPowerofTwo(n:int)->bool:
    if n ==1:
        return True
    elif n==0:
        return False
    return (n & (n-1))==0
