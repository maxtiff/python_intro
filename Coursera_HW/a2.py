def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    if len(dna) > 0:
        for nucleotide in dna:
            if nucleotide in 'ATCG':
                return len(dna)
            else:
                return 'Error'
    else:
        return 'Error'

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if get_length(dna1) > get_length(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    nuke_count = 0

    if len(dna1) and len(dna2) > 0:
        for letter in dna:
            if letter in nucleotide:
                nuke_count = nuke_count + 1
            
        return nuke_count
    else:
        return 'Error'

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    if len(dna1) and len(dna2) > 0:
        if dna2 in dna1:
            return True
        else:
            return False
    else:
        return 'Error'

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the input is a valid DNA sequence (A, T, C, G).

    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('AATTCCGG')
    True
    >>> is_valid_sequence('aATC')
    False
    >>> is_valid_sequence('')
    False

    '''
    valid = True
    
    if len(dna) > 0:
        for nucleotide in dna:
            if nucleotide not in 'ATCG':
                valid = False
                return valid
            
        return valid
            
    else:
        return 'Enter a DNA sequence'

def insert_sequence(dna1, dna2, int):
    ''' (str, str, int) -> str

    Inserts dna2 into dna1 at index int if and only if both dna inputs are valid and then returns the concatenated value.

    >>> insert_sequence('ATTG', 'AC', 2)
    'ATTACG'
    >>> insert_sequence('','TGA',3)
    'Error - Please provide a valid DNA sequence'
    >>> insert_sequence('AAGCT', 'TGA', 0)
    'TGAAAGCT'
    >>> insert_sequence('AACCGT', 'TGCA', 6)
    'Error - invalid index for interpolation to dna1'

    '''

    sequence = ''

    if is_valid_sequence(dna1) and is_valid_sequence(dna2):
        if int < len(dna1):
            sequence = dna1[:int] + dna2 + dna1[int:]
            return sequence
        else:
            return 'Error - invalid index for interpolation to dna1'
    else:
        return 'Error - Please provide a valid DNA sequence' 
            
    
                
