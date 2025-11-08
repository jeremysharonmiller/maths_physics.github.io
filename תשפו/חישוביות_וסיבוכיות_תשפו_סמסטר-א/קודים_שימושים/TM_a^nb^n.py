InputStr = 'aabbb'
InputArr = list(InputStr)

FilmArr = ['_','_'] + InputArr + ['_','_'] 

# Define the states of the Turing Machine

StateStrs = ['q0','q1','q2','q3']
Letters = ['a','b','_']

def delta(state, states,letter,letters):
    DeltaTable = [
     #      a                       b                           _
     # q0
     [      ('q1' , '_' , 'R'),    ('rej' , 'b' , 'L'),       ('acc' , '_' , 'R')  ],
     # q1
     [      ('q1' , 'a' , 'R'),    ('q1' , 'b' , 'R'),        ('q2' , '_' , 'L')   ],
     # q2
     [      ('rej' , 'a' , 'L'),    ('q3' , '_' , 'L'),       ('rej' , '_' , 'L')    ],
     # q3
     [      ('q3' , 'a' , 'L'),   ('q3' , 'b' , 'L'),        ('q0' , '_' , 'R')   ]
     ]
    
    j = letters.index(letter)
    i = states.index(state)
    
    return DeltaTable[i][j];

WrittenFilmArr = FilmArr;

i=2;
q='q0'
x=WrittenFilmArr[i] 
 
# while not(q=='rej' or q=='acc'):
#     x = WrittenFilmArr[i] 
    
#     Delta = delta(q,StateStrs,x,Letters)
    
#     mu = ''.join(WrittenFilmArr[:i])
#     sigma = ''.join(WrittenFilmArr[i])
#     nu = ''.join(WrittenFilmArr[i+1:])
#     print("%s & %s & %s & %s \\\\" % (mu,q,sigma,nu))
    
#     q = Delta[0]
#     x = Delta[1]
#     RL = Delta[2] 
#     WrittenFilmArr[i] = x
#     if RL == 'R':
#         i+= 1
#     else:
#         i+= -1
    
# print(q)

k=0
while not(q=='rej' or q=='acc'):
    x = WrittenFilmArr[i] 
    
    Delta = delta(q,StateStrs,x,Letters)
    
    mu = ''.join(WrittenFilmArr[:i])
    sigma = ''.join(WrittenFilmArr[i])
    nu = ''.join(WrittenFilmArr[i+1:])
    print("k=%d: %s %s %s %s " % (k,mu,q,sigma,nu))
    
    q = Delta[0]
    x = Delta[1]
    RL = Delta[2] 
    WrittenFilmArr[i] = x
    if RL == 'R':
        i+= 1
    else:
        i+= -1
    
    k+= 1
print(q)