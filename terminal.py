"""
Verification of the terminal digits test.
In this case the three colony counts are considered independent
extrations.
The hypotesis is that the last digit of each count can be modeled
as a draw from a uniform distribution.
"""

from read_files import *
import numpy as np
import scipy as sp
import scipy.stats as stats


FREQ = 1./10
DF = 9 #degrees of freedom

c1, c2, c3 = read_rts_count()

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
