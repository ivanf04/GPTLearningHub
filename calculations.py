# Math - 143M project 1 calculating books multiplications 
class project1: 
    Ns = [11, 12, 13]
    counts = []
    for i in range(len(Ns)):
        n = Ns[i]
        operationCount = ((n ** 3) / 3) + (n ** 2) - (n /3)
        counts.append(operationCount)
    print(counts)