dna=input("please entera valid nucleotide sequence: ")
dna=dna.lower() if dna.isupper() else dna
exit = ""
while exit!="x":
    option=input('\
                press 1 to reverse your DNA\n\
                press 2 to find compliment of your DNA\n\
                press 3 to find reverse compliment of your DNA\n\
                press 4 to find GC content\n\
                press 5 to convert your DNA into RNA\n\
                press 6 to find the start and stop codon positions\n\
                press 7 to find gc skew or content\n\
                press x to exit\n')
    def func2(dna):
        return dna[::-1]
    def func3(dna):
        comp=list(dna)
        for i in range(len(comp)):
            if comp[i] is 'a':
                comp[i]='t'
            elif comp[i] is 't':
                comp[i]='a'
            elif comp[i] is 'c':
                comp[i]='g'
            elif comp[i] is 'g':
                comp[i]='c'
        return "".join(comp)
    def func4(dna):
        comp=list(dna[::-1])
        for i in range(len(comp)):
            if comp[i] is 'a':
                comp[i]='t'
            elif comp[i] is 't':
                comp[i]='a'
            elif comp[i] is 'c':
                comp[i]='g'
            elif comp[i] is 'g':
                comp[i]='c'
        return "".join(comp)
    def func5(dna):
        length=len(dna)
        gc=0
        dna1=list(dna)
        for i in range(length):
            if dna1[i] is 'c' or dna1[i] is 'g':
                gc+=1
        return (gc/length)*100
    def func6(dna):
        dna=list(dna)
        codons=[]
        var1=0
        var2=3
        for i in range(len(dna)//3):
            codons.append("".join(dna[var1:var2]))
            var1+=3
            var2+=3
        print(codons)
        start=0
        stop=0
        for i in range(len(codons)):
            if codons[i] == 'atg':
                start=i
            elif codons[i] == 'taa' or codons[i] == 'tga' or codons[i] == 'tag':
                stop=i
        return start,stop
    def func7(dna):
        dna=list(dna)
        for i in range(len(dna)):
            if dna[i] is 't':
                dna[i]='u'
        return "".join(dna)
    def func8(dna):
        dna=list(dna)
        g=0
        c=0
        for i in range(len(dna)):
            if dna[i] is 'g':
                g+=1
            elif dna[i] is 'c':
                c+=1
        if g == c:
            return 0
        else:
            return (c-g)/(c+g)
    if option is '1':
        print(func2(dna))
    elif option is '2':
        print(func3(dna))
    elif option is '3':
        print(func4(dna))
    elif option is '4':
        print('gc content is: {}'.format(func5(dna)))
    elif option is '6':
        start,stop=func6(dna)
        print('start codon start site is: {} and stop codon start site is: {}'.format(start*3,stop*3))
    elif option is '5':
        print(func7(dna))
    elif option is '7':
        print('gc skew or content is : {}'.format(func8(dna)))
    else:
        exit = input("press x to exit: ")
