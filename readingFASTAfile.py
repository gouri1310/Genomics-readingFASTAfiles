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
for v in seqs.values():
    l.append(len(v))
long_seq=max(l)
short_seq=min(l)
maxim=l.count(long_seq)
minim=l.count(short_seq)
print("Total number of records is \t",rcount,"\n")
print("The longest DNA sequence is of length \t",long_seq,"\n")
print("The number of DNA sequences in the FASTA file with length equal to longest length is \t",maxim,"\n")
print("The shortest DNA sequence is of length \t ",short_seq,"\n")
print("The number of DNA sequences in the FASTA file with length equal to shortest length is \t",minim,"\n")
for k,v in seqs.items():
    if len(v)==(int(long_seq)):
        print("The identifier of the longest sequence is \t",k,"\n")
    if len(v)==(int(short_seq)):
        print("The identifier of the shortest sequence is \t",k,"\n")
f.close()
