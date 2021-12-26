def recursão(x,y) :
    if y== 0:
        return 0
    elif y==1:
        return x
    else:
        return x+recursão(x, y-1)
    
    
print(recursão(14,60))
