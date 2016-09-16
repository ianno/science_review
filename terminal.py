"""
Verification of the terminal digits test.
In this case the three colony counts are considered independent
extrations.
The hypotesis is that the last digit of each count can be modeled
as a draw from a uniform distribution.
"""

import csv
import re
import numpy as np
import scipy as sp
import scipy.stats as stats

#file name
FILE = './data/Bishayee Colony Counts 10.27.97-3.8.01.csv'

#columns containing the triples
COL_T1 = 3
COL_T2 = 4
COL_T3 = 5

#file contains some 'no match', or 'no xxx' exp.
#it seems they are eliminated from counting
COL_NAME = 0

#regex representing a number with decimal digits
RE_NUM = '^\d+$'
RE_NAME = '^no.*$'

FREQ = 1./10
DF = 9 #degrees of freedom

csv_file = open(FILE)
csv_reader = csv.reader(csv_file)

# read the three columns, then put them together
c1 = []
c2 = []
c3 = []

l_count = 0
invalid_mode = False
for l in csv_reader:
    #skip first 3 lines
    if l_count < 3:

        l_count = l_count + 1

    else:

        v1 = l[COL_T1]
        v2 = l[COL_T2]
        v3 = l[COL_T3]
        exp = l[COL_NAME]

        if invalid_mode and exp == '':
            print 'invalid exp(%s)' % (exp)
            continue
        else:
            invalid_mode = False


        #verifies that v1..v3 contain proper digits
        if (re.match(RE_NUM, v1) is None or
            re.match(RE_NUM, v2) is None or
            re.match(RE_NUM, v3) is None):
            print 'The triple %s, %s, %s contains '\
                'a non-number' % (v1, v2, v3)
        elif re.match(RE_NAME, exp):
             print 'non valid exp (%s)' % exp
             invalid_mode = True
        else:
                c1.append(v1)
                c2.append(v2)
                c3.append(v3)


print len(c1)+len(c2)+len(c3)

"""
there is a problem in counting the triples.
which method are they using?
a comment line explaining it would be really useful.

At the end, we were able to 'decode' the policy that was followed.
(excluding invalid experiments).

It still doesn't work w=for other files, or for the terminal digits test...
"""

#merge Counts
total_c = c1 + c2 + c3

#take only last digit
lst = [int(x[-1]) for x in total_c]

#compute frequencies
freq = {}
exp_freq = len(lst)*FREQ

#not nice.
#find a smarter way to do this
#maybe scipy.stats.histogram
for i in range(0,10):
    freq[i] = len([1 for x in lst if x==i])

chi_val = 0
for i, f in freq.items():
    chi_val = chi_val + ( (f - exp_freq) ** 2) / exp_freq

print freq
print chi_val

#find P-value for chi_valq
p_val = sp.stats.chisqprob(chi_val, DF)
print p_val
