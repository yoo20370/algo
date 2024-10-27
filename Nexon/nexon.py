N = int(input())

layer = list(map(int, input().split()))

def findMinGeneration(layer) :

    gen = 1
    sel = 0
    maxVal = max(layer)

    while True :
        if layer.count(maxVal) == len(layer) :
            gen -= 1
            return gen
        if maxVal - layer[sel] == 2 and gen % 2 != 0 :
            gen += 1
            continue
        if gen % 2 == 0 :
            if layer[sel] + 2 > maxVal:
                gen += 1
                continue
            layer[sel] += 2 
        else :
            layer[sel] += 1
        
        if maxVal == layer[sel] :
            sel += 1
            gen += 1
            continue
        gen += 1
print(findMinGeneration(layer))