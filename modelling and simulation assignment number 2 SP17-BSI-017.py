def Cal_GC(dna):
        length=len(dna)
        gc=0
        dna1=list(dna)
        for i in range(length):
            if dna1[i] is 'c' or dna1[i] is 'g':
                gc+=1
        return (gc/length)*100
Sequences = []
score = []
exit_ = ""
while exit_ != "x":
    seq = input("please enter a valid nucleotide sequence: ")
    seq = seq.lower() if seq.isupper() else seq
    Sequences.append(seq)
    score.append(Cal_GC(seq))
    exit_ = input("press x to exit: ")
dict1 = dict()
dict1.update(zip(score,Sequences))

max_score_seq = dict1[max(dict1.keys())]
print(max_score_seq)
