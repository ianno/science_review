import csv
import re

#regex representing a number with decimal digits
RE_NUM = '^\d+$'
RE_NAME = '^no.*$'


def read_triple_base(filename, col1, col2, col3, skip=3):
    """
    Reads triples in position col1, col2, and col3 from a certain file 'filename'
    """
    csv_file = open(filename)
    csv_reader = csv.reader(csv_file)

    # read the three columns, then put them together
    c1 = []
    c2 = []
    c3 = []

    l_count = 0
    for l in csv_reader:
        #skip first 3 lines
        if l_count < skip:
            l_count = l_count + 1

        else:
            v1 = l[col1]
            v2 = l[col2]
            v3 = l[col3]

            #verifies that v1..v3 contain proper digits
            if (re.match(RE_NUM, v1) is None or
                re.match(RE_NUM, v2) is None or
                re.match(RE_NUM, v3) is None):
                print 'The triple %s, %s, %s contains '\
                    'a non-number' % (v1, v2, v3)
            else:
                    c1.append(v1)
                    c2.append(v2)
                    c3.append(v3)

    return (c1, c2, c3)

def read_rts_colony():
    """
    special format to match number in paper
    """
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


def read_rts_coulter():
    FILE = './data/Bishayee Coulter Counts.10.20.97-7.16.01.csv'

    #columns containing the triples
    COL_T1 = 2
    COL_T2 = 3
    COL_T3 = 4

    return read_triple_base(FILE, COL_T1, COL_T2, COL_T3)

def read_others_colony():
    FILE = './data/Other Investigators in Lab.Colony Counts.4.23.92-11.27.02.csv'

    #columns containing the triples
    COL_T1 = 3
    COL_T2 = 4
    COL_T3 = 5

    return read_triple_base(FILE, COL_T1, COL_T2, COL_T3)

def read_others_coulter():
    FILE = './data/Other Investigators in Lab.Coulter Counts.4.15.92-5.21.05.csv'

    #columns containing the triples
    COL_T1 = 2
    COL_T2 = 3
    COL_T3 = 4

    return read_triple_base(FILE, COL_T1, COL_T2, COL_T3)


def read_outside1_coulter():
    FILE = './data/Outside Lab 1.Coulter Counts.6.7.91-4.9.99.csv'

    #columns containing the triples
    COL_T1 = 1
    COL_T2 = 2
    COL_T3 = 3

    return read_triple_base(FILE, COL_T1, COL_T2, COL_T3, 1)

def read_outside2_coulter():
    FILE = './data/Outside Lab 2.Coulter Counts.6.6.08-7.7.08.csv'

    #columns containing the triples
    COL_T1 = 1
    COL_T2 = 2
    COL_T3 = 3

    return read_triple_base(FILE, COL_T1, COL_T2, COL_T3, 2)

def read_outside3_colony():
    FILE = './data/Outside Lab 3.Colony Counts.2.4.10-5.21.12.csv'

    #columns containing the triples
    COL_T1 = 1
    COL_T2 = 2
    COL_T3 = 3

    return read_triple_base(FILE, COL_T1, COL_T2, COL_T3,2)
