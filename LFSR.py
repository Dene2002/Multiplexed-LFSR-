import random as r
!pip install pylfsr 
import pylfsr 
from pylfsr import LFSR
state=[1] 
for i in range(3):
    t=(r.randint(0,1))
    state.append(t)
print("the initial seed value for the Captain LFSR is: ")
print(state)
fpoly = [4,3]
L = LFSR(initstate=state,fpoly=fpoly,counter_start_zero=False)
print('count \t state \t\toutbit \t seq')
print('-'*50)
loop=(((2**4)-1)+10)
for _ in range(loop):
    print(L.count,L.state,'',L.outbit,L.seq,sep='\t')
    L.next()
print('-'*50)
print("the sequence generated for the captain LFSR is: ")
print('Output: ',L.seq)  
seed=[]
for i in range(4):
    seed.append(L.seq[i]) 
print("the seed value for the other three LFSRs are: ") 
print(seed)
L1 = LFSR(initstate=state,fpoly=fpoly,counter_start_zero=False)
print('count \t state \t\toutbit \t seq')
print('-'*50)
for _ in range(loop):
    print(L1.count,L1.state,'',L1.outbit,L1.seq,sep='\t')
    L1.next()
print('-'*50)
print("the sequence generated for LFSR 1 is: ")
print('Output: ',L1.seq)
L2 = list(L1.seq)
L3 = list(L1.seq) 
print("the sequence generated for LFSR 2 is: ")
print(L2)
print("the sequence generated for LFSR 3 is: ")
print(L3)
L1=list(L1.seq)
for i in range(8): 
    if(L3[i]==1):
        del L1[0] 
        for j in range(2):
            del L2[j]
res=[]
if(len(L1)>len(L2)):
    for i in range(len(L2)):
        res.append((L1[i]+L2[i])%2)
else:
    for i in range(len(L1)):
        res.append((L1[i]+L2[i])%2) 
print('-'*100) 
print("the final sequnece generated: ")
print(res) 
    
        
        
