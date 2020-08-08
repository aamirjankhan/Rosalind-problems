from Bio import SeqIO
file="sequence.gb"
output=open("Top3.faa", "w")
record=SeqIO.parse(file, "genbank")
rec=next(record)
print('The genes with the top 3 longest lengths have beens saved in Top3.faa')
for f in rec.features:
        end=f.location.end.position
        start=f.location.start.position
        length=end-start
        bug=(rec.seq)
        if f.type=='CDS':
            if 'gene' in f.qualifiers:
                        if length>7000:
                                geneName=f.qualifiers['gene']
                                name=str(geneName)
                                lenth=str(length)
                                seq=str(bug[start:end])
                                output.write('>')
                                output.write(lenth)
                                output.write('\n')
                                output.write(seq)
                                output.write('\n')
output.close()
# 2 code
import re

F=open('fasta.txt','r')

re_seq=re.compile('>GNOM\s(\d+)\ssequence\s(\d+)\n((?:\w*\n)*)')

numlist=[]
lenlist=[]

for occurence in re_seq.finditer(F.read()):
    gnom,num,seq=occurence.groups()
    numlist.append(num)
    lenlist.append(len(seq))
    print (gnom,num,len(seq))

maxl=max(lenlist)

print ("max length :",maxl)

for num,length in zip(numlist,lenlist):
   if length==maxl:
      maxnum=num

print ("max number :",maxnum)
