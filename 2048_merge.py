test_line = [4,0,2,2]

def Merge_l(line):
    length = len(line)
    num = 0
    baffer = 0
    new_line = []
    while num < length:
        if line[num] > 0:
            if baffer == 0:  
                baffer = line[num]
            else:
                if baffer == line[num]:
                    new_line.append(baffer*2)
                    baffer = 0
                else:
                    new_line.append(baffer)
                    baffer = line[num]
        num = num +1    
    if baffer > 0:
        new_line.append(baffer)
    new_length = len(new_line) 
    while new_length < length:
        new_line.append(0)
        new_length = len(new_line)
    print new_line
    
def Merge(line,start,direkt):
    length = len(line)
    num = 0
    pos = start
    baffer = 0
    new_line = []
    while num < length:
        if line[pos] > 0:
            if baffer == 0:  
                baffer = line[pos]
            else:
                if baffer == line[pos]:
                    new_line.append(baffer*2)
                    baffer = 0
                else:
                    new_line.append(baffer)
                    baffer = line[pos]
        pos = pos + direkt
        num = num +1    
    if baffer > 0:
        if direkt > 0:
            new_line.append(baffer)
        else:
            new_line.insert(0, baffer)
    new_length = len(new_line) 
    while new_length < length:
        if direkt > 0:
            new_line.append(0)
        else:
            new_line.insert(0, 0)
        new_length = len(new_line)
    print new_line   
    
    
Merge_l(test_line)  
Merge_l([2,2,2,2,2])
Merge(test_line,-1,-1)
Merge([2,4,2,2,2],-1,-1)
Merge([2,2,2,4,2],-1,-1)
