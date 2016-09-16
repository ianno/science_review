"""
Verification of the terminal digits test.
In this case the three colony counts are considered independent
extrations.
The hypotesis is that the last digit of each count can be modeled
as a draw from a uniform distribution.
"""

import csv
import re

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
