#reading each FASTA entry one at a time and storing it in dictionaries
fname=input("Enter the name of the file\n")
print(fname,"\n")
try:
    f=open(fname) #FASTA files contain DNA sequences with each ID representing a a DNA sequences. It is used for DNA sequence allignment
except IOError:
    print("File does no exist")
seqs={}#each of these dictionaries contain a DNA sequence corresponding to the respective ID
l=list()
rcount=0
for line in f:
    line=line.rstrip()
    if line.startswith('>'):
        rcount=rcount+1
        words=line.split()
        name=words[0][1:]
        seqs[name]=""
    else:
        seqs[name]=seqs[name]+line
#to find the ORFs
#an ORF is a part of the reading frame of a  DNA sequence starting with 'AGC' and ending with either 'TAG' or 'TAA' or 'TGA'
stop_codon=["TAG","TGA","TAA"]
def orf1(seq):#reading frame 1
    start_indices=list()
    stop_indices=list()
    for a in range(0,len(seq),3):
        if seq[a:a+3]=="ATG":
            start_indices.append(a)
    for b in range(0,len(seq),3):
        if seq[b:b+3] in stop_codon:
            stop_indices.append(b)
    mark=0
    orf=list()
    for i in range(len(start_indices)):
        for j in range(len(stop_indices)):
            if (start_indices[i]<stop_indices[j]) and (start_indices[i]>mark):
                orf.append(seq[start_indices[i]:stop_indices[j]+3])
                mark=stop_indices[j]+3
                break
    return orf
def orf2(seq):#reading frame 1
    start_indices=list()
    stop_indices=list()
    for a in range(1,len(seq),3):
        if seq[a:a+3]=="ATG":
            start_indices.append(a)
    for b in range(1,len(seq),3):
        if seq[b:b+3] in stop_codon:
            stop_indices.append(b)
    mark=0
    orf=list()
    for i in range(len(start_indices)):
        for j in range(len(stop_indices)):
            if (start_indices[i]<stop_indices[j]) and (start_indices[i]>mark):
                orf.append(seq[start_indices[i]:stop_indices[j]+3])
                mark=stop_indices[j]+3
                break
    return orf
def orf3(seq):#reading frame 1
    start_indices=list()
    stop_indices=list()
    for a in range(2,len(seq),3):
        if seq[a:a+3]=="ATG":
            start_indices.append(a)
    for b in range(2,len(seq),3):
        if seq[b:b+3] in stop_codon:
            stop_indices.append(b)
    mark=0
    orf=list()
    for i in range(len(start_indices)):
        for j in range(len(stop_indices)):
            if (start_indices[i]<stop_indices[j]) and (start_indices[i]>mark):
                orf.append(seq[start_indices[i]:stop_indices[j]+3])
                mark=stop_indices[j]+3
                break
    return orf
#storing the orfs of different frames and their respective lengths in 3 different lists
orfs_rf1=list()
orfs_rf2=list()
orfs_rf3=list()
l1=list()
l2=list()
l3=list()
for s in seqs.values():
    orfs_rf1=orf1(s)
    for j in orfs_rf1:
        l1.append(len(j))
    orfs_rf2=orf2(s)
    for j in orfs_rf2:
        l2.append(len(j))
    orfs_rf3=orf3(s)
    for j in orfs_rf3:
        l3.append(len(j))
print("The length of the longest ORF in reading frame 1 is ",max(l1),"\n")
print("The length of the longest ORF in reading frame 2 is",max(l2),"\n")
print("The length of the longest ORF in reading frame 3 is ",max(l3),"\n")
m=[max(l1),max(l2),max(l3)]
print("The length of the longest ORF in all sequences in any reading frame is",max(m),"\n")
