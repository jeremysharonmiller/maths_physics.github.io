InputStr = 'aaaaaaaa'
InputArr = list(InputStr)

FilmArr = ['_','_'] + InputArr + ['_','_'] 

# Define the states of the Turing Machine

StateStrs = ['none','one','even','odd','back']
Letters = ['a','v','_']

def delta(state, states,letter,letters):
    DeltaTable = [
     #      a                       v                           _
     # none
     [      ('one' , 'v' , 'R'),    ('none' , 'v' , 'R'),       ('rej' , '_' , 'R')  ],
     # one
     [      ('even' , 'a' , 'R'),    ('one' , 'v' , 'R'),        ('acc' , '_' , 'L')   ],
     # even
     [      ('odd' , 'v' , 'R'),    ('even' , 'v' , 'R'),       ('back' , '_' , 'L')    ],
     # odd
     [      ('even' , 'a' , 'R'),   ('odd' , 'v' , 'R'),        ('rej' , '_' , 'R')   ],
     # back
     [      ('back' , 'a' , 'L'),   ('back' , 'v' , 'L'),       ('none' , '_' , 'R')   ]
     ]
    
    j = letters.index(letter)
    i = states.index(state)
    
    return DeltaTable[i][j];

WrittenFilmArr = FilmArr;

i=2;
q='none'
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
    k += 1     
print(q)