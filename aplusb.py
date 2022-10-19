with open('dataset_3363_2.txt') as text:
    for line in text:
        line = line.strip()
        newline = ''
        newlit = ''
        newnumb = ''
        numb = {'0','1','2','3','4','5','6','7','8','9'}
        for i in range(0, len(line)):
            if line[i] in numb:
                newnumb+=line[i]
            else:
                newlit=line[i]
            if i == len(line)-1:    
                    liter = newlit*int(newnumb)
                    newline+=liter
            elif line[i+1] not in numb:    
                liter = newlit*int(newnumb)
                newline+=liter
                newnumb=''
        print(newline)    