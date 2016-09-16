import csv
import re

#regex representing a number with decimal digits
RE_NUM = '^\d+$'
RE_NAME = '^no.*$'

def read_rts_count():
    FILE = './data/Bishayee Colony Counts 10.27.97-3.8.01.csv'

    #columns containing the triples
    COL_T1 = 3
    COL_T2 = 4
    COL_T3 = 5

    #file contains some 'no match', or 'no xxx' exp.
    #it seems they are eliminated from counting
    COL_NAME = 0

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

    return (c1, c2, c3)
