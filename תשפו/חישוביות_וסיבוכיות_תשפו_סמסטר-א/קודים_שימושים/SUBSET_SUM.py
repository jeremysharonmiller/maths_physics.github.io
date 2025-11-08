import numpy as np;
import pandas as pd;

transtn_functn = np.array([
#state          read_S  read_c  read_t new_state    wrt_S  wrt_c  wrt_t   mv_S     mv_c   mv_t
['q0',          '1',   '1',     'a',   'check_1',   '1',   '1',   'a',    'R',    'R',    'S'],
['check_1',     '1',   '1',     'a',   'check_1',   '1',   '1',   'a',    'R',    'R',    'S'],
['check_1',     '1',   '#',     'a',   'c_back_2',  '1',   '#',   'a',    'R',    'L',    'S'],
['check_1',     '#',   '1',     'a',   'c_back_3',  '#',   '1',   'a',    'R',    'L',    'S'],
['check_1',     '#',   '#',     'a',   'check_1',   '#',   '#',   'a',    'R',    'R',    'S'],
['check_1',     '_',   '1',     'a',   'rej',       '_' ,  '1',   'a',    'R',    'R',    'S'],
['check_1',     '1',   '_',     'a',   'rej',       '1',   '_',   'a',    'R',    'R',    'S'],
['check_1',     '_',   '_',     'a',   's_c_back',  '_',   '_',   'a',    'L',    'L',    'S'],
['check_1',     '#',   '_',     'a',   's_c_back',  '#',   '_',   'a',    'L',    'L',    'S'],
['check_1',     '#',   '_',     'a',   'rej',       '#',   '_',   'a',    'R',    'R',    'S'],
['check_1',     '_',   '#',     'a',   'rej',       '_',   '#',   'a',    'R',    'R',    'S'],
['c_back_2',    '1',   '1',     'a',   'c_back_2',  '1',   '1',   'a',    'R',    'L',    'S'],
['c_back_2',    '#',   '1',     'a',   'c_back_2',  '#',   '1',   'a',    'R',    'L',    'S'],
['c_back_2',    '1',   '1',     'a',   'c_back_2',  '1',   '1',   'a',    'S',    'L',    'S'],
['c_back_2',    '1',   '_',     'a',   'check_1',   '1',   '_',   'a',    'S',    'R',    'S'],
['c_back_2',    '1',   '#',     'a',   'check_1',   '1',   '1',   'a',    'S',    'R',    'S'],
['c_back_3',    '1',   '1',     'a',   'c_back_3',  '1',   '1',   'a',    'S',    'L',    'S'],
['c_back_3',    '1',   '_',     'a',   'check_1',   '1',   '_',   'a',    'S',    'R',    'S'],
['c_back_3',    '1',   '#',     'a',   'check_1',   '1',   '#',   'a',    'S',    'R',    'S'],
['s_c_back',    '1',   '#',     'a',   's_c_back',  '1',   '#',   'a',    'L',    'L',    'S'],
['s_c_back',    '#',   '1',     'a',   's_c_back',  '#',   '1',   'a',    'L',    'L',    'S'],
['s_c_back',    '#',   '#',     'a',   's_c_back',  '#',   '#',   'a',    'L',    'L',    'S'],
['s_c_back',    '1',   '1',     'a',   's_c_back',  '1',   '1',   'a',    'L',    'L',    'S'],
['s_c_back',    '_',   '1',     'a',   's_c_back_1',  '_',   '1',   'a',    'R',    'L',    'S'],
['s_c_back',    '_',   '#',     'a',   's_c_back_1',  '_',   '#',   'a',    'R',    'L',    'S'],
['s_c_back',    '1',   '_',     'a',   's_c_back_2',  '1',   '_',   'a',    'L',    'R',    'S'],
['s_c_back',    '#',   '_',     'a',   's_c_back_2',  '#',   '_',   'a',    'L',    'R',    'S'],
['s_c_back',    '_',   '_',     'a',   'add',       '_',   '_',   'a',    'R',    'R',    'S'],
['s_c_back_1',  '1',   '1',     'a',   's_c_back_1',  '1',   '1',   'a',    'S',    'L',    'S'],
['s_c_back_1',  '1',   '#',     'a',   's_c_back_1',  '1',   '#',   'a',    'S',    'L',    'S'],
['s_c_back_1',  '1',   '_',     'a',   'add',  '1',   '_',   'a',    'S',    'R',    'S'],
['s_c_back_2',  '1',   '1',     'a',   's_c_back_2',  '1',   '1',   'a',    'L',    'S',    'S'],
['s_c_back_2',  '#',   '1',     'a',   's_c_back_2',  '#',   '1',   'a',    'L',    'S',    'S'],
['s_c_back_2',  '_',   '1',     'a',   'add',          '_',   '1',   'a',    'R',    'S',    'S'],
['add',         'a',   '1',     'a',   'add',          'a',   '1',   'a',    'S',    'R',    'S'],
['add',         'a',   '#',     'a',   'add_1',        'a',   '1',   'a',    'S',    'R',    'S'],
['add',       'a',   '_',     'a',   'back_c_1',  'a',   '_',   'a',    'S',    'L',    'S'],
['add_1',       'a',   '1',     'a',   'add_1',  'a',   '1',   'a',    'S',    'R',    'S'],
['add_1',       'a',   '#',     'a',   'add_1',  'a',   '#',   'a',    'S',    'R',    'S'],
['add_1',       'a',   '_',     'a',   'drop',  'a',   '_',   'a',    'S',    'L',    'S'],
['drop',       'a',   '1',     'a',   'back_c',  'a',   '_',   'a',    'S',    'L',    'S'],
['back_c',      'a',   '1',     'a',   'back_c',  'a',   '1',   'a',    'S',    'L',    'S'],
['back_c',      'a',   '#',     'a',   'back_c',  'a',   '#',   'a',    'S',    'L',    'S'],
['back_c',      'a',   '_',     'a',   'add',  'a',   '_',   'a',    'S',    'R',    'S'],
['back_c_1',      'a',   '1',     'a',   'back_c_1',  'a',   '1',   'a',    'S',    'L',    'S'],
['back_c_1',      'a',   '#',     'a',   'back_c_1',  'a',   '#',   'a',    'S',    'L',    'S'],
['back_c_1',    'a',   '_',     'a',   'compare',  'a',   '_',   'a',    'S',    'R',    'S'],
['compare',    'a',   '1',     '1',   'compare',  'a',   '1',   '1',    'S',    'R',    'R'],
['compare',    'a',   '1',     '_',   'rej',  'a',   '1',   '_',    'S',    'R',    'R'],
['compare',    'a',   '_',     '1',   'rej',  'a',   '_',   '1',    'S',    'R',    'R'],
['compare',    'a',   '_',     '_',   'acc',  'a',   '_',   '_',    'S',    'S',    'S']
])

df = pd.DataFrame(transtn_functn);

df.columns = ['state','read_S','read_c','read_t','new_state','wrt_S','wrt_c','wrt_t','mv_S','mv_c','mv_t']

# Works ends in state 'add'
# s = np.array([1,3,4,5,6])
# c = np.array([3,4,5,6]);

# Works ends in state 'add'
# s = np.array([1,3,4])
# c = np.array([3,4]);

# Works ends in state 'rej'
# s = np.array([1,3,4])
# c = np.array([3,4,7]);

# Works ends in state 'add'
# s = np.array([1,3,4,5,6,2])
# c = np.array([3,4, 6]);

# Works ends in state 'add'
# s = np.array([1,2,3,4,5,6])
# c = np.array([3,4, 6]);

# Works ends in state 'add'

# s = np.array([1,3,4,2])
# c = np.array([3,4]);


s = np.array([1,30,12,40])
c = np.array([12,40]);

s_tape = ['_'] 
c_tape = ['_']
t_tape = ['_']

for a in s:
    for b in range(a):
        s_tape = s_tape + ['1']
    s_tape = s_tape + ['#']
s_tape[-1] =  '_';

for a in c:
    for b in range(a):
        c_tape = c_tape + ['1']
    c_tape = c_tape + ['#']
c_tape[-1] =  '_';

t = sum(c);

for a in range(t):
    t_tape = t_tape + ['1']
t_tape = t_tape + ['_']


mu = '_'
q = 'q0'
sigma = [ s_tape[1] , c_tape[1], t_tape[1] ]
v = [ s_tape[2:] , c_tape[2:], t_tape[2:] ]

k=0

i1 = 1
i2 = 1
i3 = 1
while not(q=='rej' or q=='add'):
    # print("stage k=%d\n"%k)
    # print("state=%s" % q)
    
    read_1 = s_tape[i1]
    read_2 = c_tape[i2]
    read_3 = t_tape[i3]
    
    df1 = df.loc[ (df['state']==q) & (df['read_S']==read_1)  & (df['read_c']==read_2)   ]
    
    wrt_1 = df1['wrt_S'].values[0]
    wrt_2 = df1['wrt_c'].values[0]
    wrt_3 = df1['wrt_t'].values[0]
    
    mv_1 = df1['mv_S'].values[0]
    mv_2 = df1['mv_c'].values[0]
    mv_3 = df1['mv_t'].values[0]

    q = df1['new_state'].values[0]
    
    s_tape[i1] = wrt_1
    c_tape[i2] = wrt_2
    # t_tape[i3] = wrt_3    

    s_tape_str = "| ";
    for i,a in enumerate(s_tape):
        s_tape_str += " "
        s_tape_str += a
        if i == i1:
            s_tape_str += "*|"
        else:
            s_tape_str += " |"
    # print("%s"% s_tape_str)
    
    c_tape_str = "| ";
    for i,a in enumerate(c_tape):
        c_tape_str += " "
        c_tape_str += a
        if i == i2:
            c_tape_str += "*|"
        else:
            c_tape_str += " |"
    # print("%s"% c_tape_str)
    
    t_tape_str = "| ";
    for i,a in enumerate(t_tape):
        t_tape_str += " "
        t_tape_str += a
        if i == i3:
            t_tape_str += "*|"
        else:
            t_tape_str += " |"
    # print("%s\n\n"% t_tape_str)
    
    if mv_1 == 'R':
        i1 = i1 + 1
    elif mv_1 == 'L':
        i1 =  i1 -1
    elif mv_1 == 'S':
        i1 = i1

    if mv_2 == 'R':
        i2 = i2 + 1
    elif mv_2 == 'L':
        i2 =  i2 -1
    elif mv_1 == 'S':
        i2 = i2

    if mv_3 == 'R':
        i3 = i3 + 1
    elif mv_3 == 'L':
        i3 =  i3 -1
    elif mv_3 == 'S':
        i3 = i3
    
    k = k + 1
        
    # print("new state=%s\n" % q)
    # print("--------------------------------------------------" )

print("new state=%s\n" % q)

s_tape_str = "| ";
for i,a in enumerate(s_tape):
    s_tape_str += " "
    s_tape_str += a
    if i == i1:
        s_tape_str += "*|"
    else:
        s_tape_str += " |"
print("%s"% s_tape_str)

c_tape_str = "| ";
for i,a in enumerate(c_tape):
    c_tape_str += " "
    c_tape_str += a
    if i == i2:
        c_tape_str += "*|"
    else:
        c_tape_str += " |"
print("%s"% c_tape_str)

t_tape_str = "| ";
for i,a in enumerate(t_tape):
    t_tape_str += " "
    t_tape_str += a
    if i == i3:
        t_tape_str += "*|"
    else:
        t_tape_str += " |"
print("%s\n\n"% t_tape_str)

addQ = False

if q=='add':
    addQ = True
    
while(addQ and ( q!='compare')):

    # print("stage k=%d\n"%k)
    # print("state=%s" % q)
    
    read_1 = s_tape[i1]
    read_2 = c_tape[i2]
    read_3 = t_tape[i3]
    
    df1 = df.loc[ (df['state']==q) &  (df['read_c']==read_2)   ]
    
    wrt_1 = df1['wrt_S'].values[0]
    wrt_2 = df1['wrt_c'].values[0]
    wrt_3 = df1['wrt_t'].values[0]
    
    mv_1 = df1['mv_S'].values[0]
    mv_2 = df1['mv_c'].values[0]
    mv_3 = df1['mv_t'].values[0]

    q = df1['new_state'].values[0]
    
    # s_tape[i1] = wrt_1
    c_tape[i2] = wrt_2
    # t_tape[i3] = wrt_3    

    s_tape_str = "| ";
    for i,a in enumerate(s_tape):
        s_tape_str += " "
        s_tape_str += a
        if i == i1:
            s_tape_str += "*|"
        else:
            s_tape_str += " |"
    # print("%s"% s_tape_str)
    
    c_tape_str = "| ";
    for i,a in enumerate(c_tape):
        c_tape_str += " "
        c_tape_str += a
        if i == i2:
            c_tape_str += "*|"
        else:
            c_tape_str += " |"
    # print("%s"% c_tape_str)
    
    t_tape_str = "| ";
    for i,a in enumerate(t_tape):
        t_tape_str += " "
        t_tape_str += a
        if i == i3:
            t_tape_str += "*|"
        else:
            t_tape_str += " |"
    # print("%s\n\n"% t_tape_str)
    
    if mv_1 == 'R':
        i1 = i1 + 1
    elif mv_1 == 'L':
        i1 =  i1 -1
    elif mv_1 == 'S':
        i1 = i1

    if mv_2 == 'R':
        i2 = i2 + 1
    elif mv_2 == 'L':
        i2 =  i2 -1
    elif mv_1 == 'S':
        i2 = i2

    if mv_3 == 'R':
        i3 = i3 + 1
    elif mv_3 == 'L':
        i3 =  i3 -1
    elif mv_3 == 'S':
        i3 = i3
    
    k = k + 1
        
    # print("new state=%s\n" % q)
    # print("--------------------------------------------------" )

print("new state=%s\n" % q)

s_tape_str = "| ";
for i,a in enumerate(s_tape):
    s_tape_str += " "
    s_tape_str += a
    if i == i1:
        s_tape_str += "*|"
    else:
        s_tape_str += " |"
print("%s"% s_tape_str)

c_tape_str = "| ";
for i,a in enumerate(c_tape):
    c_tape_str += " "
    c_tape_str += a
    if i == i2:
        c_tape_str += "*|"
    else:
        c_tape_str += " |"
print("%s"% c_tape_str)

t_tape_str = "| ";
for i,a in enumerate(t_tape):
    t_tape_str += " "
    t_tape_str += a
    if i == i3:
        t_tape_str += "*|"
    else:
        t_tape_str += " |"
print("%s\n\n"% t_tape_str)


compareQ = False

if q=='compare':
    compareQ = True
    
while(compareQ and   q!='acc' ):

    # print("stage k=%d\n"%k)
    # print("state=%s" % q)
    
    read_1 = s_tape[i1]
    read_2 = c_tape[i2]
    read_3 = t_tape[i3]
    
    df1 = df.loc[ (df['state']==q) &  (df['read_c']==read_2) & (df['read_t']==read_3)   ]
    
    wrt_1 = df1['wrt_S'].values[0]
    wrt_2 = df1['wrt_c'].values[0]
    wrt_3 = df1['wrt_t'].values[0]
    
    mv_1 = df1['mv_S'].values[0]
    mv_2 = df1['mv_c'].values[0]
    mv_3 = df1['mv_t'].values[0]

    q = df1['new_state'].values[0]
    
    # s_tape[i1] = wrt_1
    c_tape[i2] = wrt_2
    t_tape[i3] = wrt_3    

    s_tape_str = "| ";
    for i,a in enumerate(s_tape):
        s_tape_str += " "
        s_tape_str += a
        if i == i1:
            s_tape_str += "*|"
        else:
            s_tape_str += " |"
    # print("%s"% s_tape_str)
    
    c_tape_str = "| ";
    for i,a in enumerate(c_tape):
        c_tape_str += " "
        c_tape_str += a
        if i == i2:
            c_tape_str += "*|"
        else:
            c_tape_str += " |"
    # print("%s"% c_tape_str)
    
    t_tape_str = "| ";
    for i,a in enumerate(t_tape):
        t_tape_str += " "
        t_tape_str += a
        if i == i3:
            t_tape_str += "*|"
        else:
            t_tape_str += " |"
    # print("%s\n\n"% t_tape_str)
    
    if mv_1 == 'R':
        i1 = i1 + 1
    elif mv_1 == 'L':
        i1 =  i1 -1
    elif mv_1 == 'S':
        i1 = i1

    if mv_2 == 'R':
        i2 = i2 + 1
    elif mv_2 == 'L':
        i2 =  i2 -1
    elif mv_1 == 'S':
        i2 = i2

    if mv_3 == 'R':
        i3 = i3 + 1
    elif mv_3 == 'L':
        i3 =  i3 -1
    elif mv_3 == 'S':
        i3 = i3
    
    k = k + 1
        
    # print("new state=%s\n" % q)
    # print("--------------------------------------------------" )

print("new state=%s\n" % q)

s_tape_str = "| ";
for i,a in enumerate(s_tape):
    s_tape_str += " "
    s_tape_str += a
    if i == i1:
        s_tape_str += "*|"
    else:
        s_tape_str += " |"
print("%s"% s_tape_str)

c_tape_str = "| ";
for i,a in enumerate(c_tape):
    c_tape_str += " "
    c_tape_str += a
    if i == i2:
        c_tape_str += "*|"
    else:
        c_tape_str += " |"
print("%s"% c_tape_str)

t_tape_str = "| ";
for i,a in enumerate(t_tape):
    t_tape_str += " "
    t_tape_str += a
    if i == i3:
        t_tape_str += "*|"
    else:
        t_tape_str += " |"
print("%s\n\n"% t_tape_str)
