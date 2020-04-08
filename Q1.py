# CMT309 Coursework 1
# student number:C1977152

def cycle_convert(x,n):
    r = [int, float, bool, str, complex, int, float, bool, str]
    for i in range(len(r)):
        while n > 0 and i < 5:
            if type(x) == r[i]:
                break
            else:
                i+=1
                continue
        x = r[i + n](x)
        return x
    for i in range(len(r)):
        while n < 0 and i > 5:
            if type(x) == r[i]:
                break
            else:
                i+=1
                continue
        x = r[i + n](x)
        return x



