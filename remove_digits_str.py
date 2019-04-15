def remove_digits_str(s):
    '''
    Remove digits from a string
    @param:
        s    - Required : (str)
    '''
    no_digits = []
    for caracters in s:
        if not caracters.isdigit():
            no_digits.append(caracters)
            
    # join all elements of the list
    return ''.join(no_digits)
    
