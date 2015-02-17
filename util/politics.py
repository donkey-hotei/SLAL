"""
Analyzing voting data using SLAL
"""
from Vector import Vector
from Vector import list2vector, zero_vector

US_file = open('US_Senate_voting_data_109.txt')
UN_file = open('UN_voting_data.txt')
US_voting_data = [ ]
UN_voting_data = [ ]


# These two while loops make the program run very slow initially....
while 1:
    line = US_file.readline()
    if not line:
        break
    US_voting_data.append(line.rstrip('\n').strip().split())

while 1:
    line = UN_file.readline()
    if not line:
        break
    UN_voting_data.append(line.rstrip('\n').strip().split())

# Now we're going to turn these lists of data into dictionaries
US_voting_dict = { data[0]: list2vector([int(i) for i in data[3:]])
                   for data in US_voting_data }

p = { data[0] : (data[1],data[2]) for data in US_voting_data }
democrats = [ senator for senator in p.keys() if p[senator][0] == 'D' ] # filter our democrats
republicans = [ senator for senator in p.keys() if p[senator][0] == 'R' ] # filter out republicans...

UN_voting_dict = { data[0]: list2vector([int(i) for i in data[3:]])
                   for data in UN_voting_data }

def compare_policy(voting_dict, A, B):
    """
    Compares the policy of two countries/senators
    by taking the dot product of their voting vectors.
    """
    return voting_dict[A] * voting_dict[B]



def average_policy(voting_dict, par): pass
    


