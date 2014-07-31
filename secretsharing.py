"""
Applications of the SLAL:
Threshold Secret Sharing

by dynsne
"""


"""
Recall in the Perfect Secrecy notebook a method for splitting a secret into two pieces
so that both were required to recover the secret. The method used GF(2). One could 
generalize this to split a secret among four people, so that jointly they could 
recover the secret but any three could not. However it would be risky to rely on all
four people showing up for a meeting. 

Here we will instead use a threshold-secret-sharing scheme, a scheme buy which we could share 
a secret among four people so that any three could jointly recover the secret, but any two could not.
There are such schemes that use fields other than GF(2), but let's see if it can be done using GF(2)




"""
from GF2 import one, zero
from GF2util import randomGF2
from vectorutil import list2vector

def choose_secret_vector(s, t):
	"""
	Input: GF2 field elements s and t (i.e: bits)
	Output: a random 6-vector u such that a0*u == s and b0*u == t
	"""
	a0 = list2vector([one, one, zero, one, zero, one])
	b0 = list2vector([one, one, zero, zero, zero, one])
	while True:
		u = randomGF2(6)
		if a0 * u == s and b0 * u == t:
			return u
		else:
			continue
"""
However, be warned: Do not use the above procedure if you really intend to keep a secret. 
Python's random module does not generate crytographically secure psuedorandom bits. 
In particular a rouge individual could use his shares to actually figure it out, the state
of the pseudorandom-number generator, predict future psuedorandom numbers, and break
the security of the scheme. 
"""

# Finding the vectors that satisfy the requirement.
"""
We have decided that 
a0 = list2vector([one, one, zero, one, zero, one]) and
b0 = list2vector([one, one, zero, zero, zero, one])

Our goal is to select vectors a1..a4 and b1...b4 over GF2 so that the requirement is satisfied:
-- For any three pairs of, the correpsonding 6-vectors are linearly independent. ---
"""



if __name__ == '__main__':
	print( choose_secret_vector(one, one) )
