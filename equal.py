"""
Verification of the equal digits test.
In this case the three colony counts are considered independent
extrations.
The hypotesis is that the last pair of digits being equal
(for experiments with at least three digits)
behaves as a draw from a uniform distribution, that is, 10% chance
"""

from read_files import *
import numpy as np
import scipy as sp
import scipy.stats as stats


FREQ = 1./10
DF = 9 #degrees of freedom

c1, c2, c3 = read_rts_colony()

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

#take only experiments with at least 3 digits
big_c = [x for x in total_c if len(x) >= 3]
print len(big_c)

#take only last 2 digits
lst = [x[-2:] for x in big_c]

#compute frequencies
freq = {}
exp_freq = len(lst)*FREQ
rest_freq = len(lst)*(1-FREQ)
#exp_freq = 5155*FREQ
#rest_freq = 5155*(1-FREQ)

#not nice.
#find a smarter way to do this
#maybe scipy.stats.histogram
for i in range(0,10):
    i_s = str(i)
    freq[i_s+i_s] = len([1 for x in lst if x[0]==i_s and x[1]==i_s])

sum_eq = 1.*sum(freq.values())
#sum_eq = 636.

#case equal pair
chi_val = ((sum_eq - exp_freq) ** 2) / exp_freq
#rest
chi_val = chi_val + ( ((len(lst)-sum_eq) - rest_freq) ** 2) / rest_freq
#chi_val = chi_val + ( ((5155-sum_eq) - rest_freq) ** 2) / rest_freq


print freq
print sum_eq/len(lst)
#print sum_eq/5155
print chi_val

#find P-value for chi_valq
p_val = sp.stats.chisqprob(chi_val, 1)
print p_val

"""
here we have a problem...
we get 6.44*10-9 instead of 3.3*10-8.

the 6.4 can be easily explained. (different counts: 643 over 5177 vs 636 over 5155, or 12.4% vs 12.3%)

the 10-9 vs 10-8 is also explained in the same way.
check commented code to plug paper values.
How have they calculated it?
here we use chi2

we actually get 2.21419848076e-08 with their values...
"""
