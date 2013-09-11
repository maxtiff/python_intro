def convert_to_c(fahrenheit):
    '''(number) -> float

    Returns the number of Celsius degrees equivalent to Fahrenheit degrees
    
    >>> convert_to_c(32)
    0.0
    >>> convert_to_c(212)
    100.0
    '''
    return (fahrenheit - 32) * (5/9)

    
