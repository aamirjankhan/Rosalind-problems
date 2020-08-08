dna='''ttcacctatgaatggactgtccccaaagaagtaggacccactaatgcagatcctgtg
tgtctagctaagatgtattattctgctgtggatcccactaaagatatattcactgggcttattgggccaa
tgaaaatatgcaagaaaggaagtttacatgcaaatgggagacagaaagatgtagacaaggaattctattt
gtttcctacagtatttgatgagaatgagagtttactcctggaagataatattagaatgtttacaactgca
cctgatcaggtggataaggaagatgaagactttcaggaatctaataaaatgcactccatgaatggattca
tgtatgggaatcagccgggtctcactatgtgcaaaggagattcggtcgtgtggtacttattcagcgccgg
aaatgaggccgatgtacatggaatatacttttcaggaaacacatatctgtggagaggagaacggagagac
acagcaaacctcttccctcaaacaagtcttacgctccacatgtggcctgacacagaggggacttttaatg
ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg
gcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgg
gattattccccacaaagggagtgggaaaaggagctgcatcatttacaagagcagaatgtttcaaatgcat
ttttagataagggagagttttacataggctcaaagtacaagaaagttgtgtatcggcagtatactgatag
cacattccgtgttccagtggagagaaaagctgaagaagaacatctgggaattctaggtccacaacttcat
gcagatgttggagacaaagtcaaaattatctttaaaaacatggccacaaggccctactcaatacatgccc
atggggtacaaacagagagttctacagttactccaacattaccaggtgaaactctcacttacgtatggaa
aatcccagaaagatctggagctggaacagaggattctgcttgtattccatgggcttattattcaactgtg
gatcaagttaaggacctctacagtggattaattggccccctgattgtttgtcgaagaccttacttgaaag
tattcaatcccagaaggaagctggaatttgcccttctgtttctagtttttgatgagaatgaatcttggta
cttagatgacaacatcaaaacatactctgatcaccccgagaaagtaaacaaagatgatgaggaattcata
gaaagcaataaaatgcatgctattaatggaagaatgtttggaaacct'''
EcoR1='gaattc'
BamH1='ggatcc'
HindIII='aagctt'
def findsites(restrictionsite,dna):
           index=dna.find(restrictionsite)
           return(index)

for i in range(1):
           r=findsites(EcoR1,dna)
           
           m=dna.count(EcoR1)
           
           print('EcoR1 sites are: '+str(m))
           print(r)
           for l in range (m-1):
               a=dna.find(EcoR1, r+5)
               print(a)
               r=a
for j in range(1):
           r=findsites(BamH1,dna)
           
           m=dna.count(BamH1)
           
           print('BamH1 sites are: '+str(m))
           print(r)
           for l in range (m-1):
               a=dna.find(BamH1, r+5)
               print(a)
               r=a
for k in range(1):
           r=findsites(HindIII,dna)
           
           m=dna.count(HindIII)
           print('HindIII sites are: '+str(m))
           print(r)
           if m>0:
               
               for l in range (m-1):
                   a=dna.find(HindIII, r+5)
                   print(a)
                   r=a
