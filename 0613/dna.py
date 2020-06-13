def avg(a,b):
    s= (a+b)/2
    return s
in1=int(input("값1:"))
in2=int(input("값2:"))
r=avg(in1,in2)
print("평균=",r)

def comp(seq):
    comp_dict={'A':'T','T':'A','C':'G','G':'C'}
    seq_comp=""
    n=int(len(seq))-1
    while n>-1:
        seq_rev=seq_rev+seq[n]
        n=n-1
        return seq_rev
