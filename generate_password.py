#!/ustr/bin/python

DOCSTRING = ''' generate a password with length "passlen" with no duplicate characters in the password '''

import random

SS = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
PASSLEN = 8
p = "".join(random.sample(SS, PASSLEN))
print p
