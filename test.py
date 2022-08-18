def threen(n):
    seq = []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            seq.append(n)
        else:
            n = (n*3)+1
            seq.append(n)
    return False if seq[-3:] != [4, 2, 1] else True


i = 2**68
while True:
    print(f"{str(threen(i))}: {str(i)}", end="\r") if threen(
        i) == True else quit()
    i += 1
