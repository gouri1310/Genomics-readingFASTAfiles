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
 #to find repeats of a given length n
while(1):
    r=input("Enter the length n of the substring you want to perform the operations on or enter done if you don't want to do so \n")
    if r=='done':
        break
    n=int(r)
    def repeat_l(seq):
        repeats=list()
        for i in range(len(seq)):
            repeats.append(seq[i:i+n])
        return repeats
    rep=list()
    all_n_repeats=list()
    for a in seqs.values():
        rep=repeat_l(str(a))
        for j in rep:
            all_n_repeats.append(j)

    count1=dict()
    for l in all_n_repeats:
        count1[l]=count1.get(l,0)+1
    s=sorted(count1.values())[-1]
    max_occur=list()
    for l in count1.values():
        max_occur.append(l)
    print("The number of times different substrings of length ",n," occur maximum times is ",max_occur.count(s),"\n")
    for k,v in count1.items():
        if int(v)==int(s):
            print("The maximum occuring DNA substring of length ",n,"and the number of times it occurs is \t ",(k,v),"\n")
            break       
f.close()
