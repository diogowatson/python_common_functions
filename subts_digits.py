def subst_digits(value):
    '''
    substitutes any digit in the strig for #
    
    @Params:
        value     - Required : string to be converted (str)
        
    @returns:
        string 
    '''
    new_value = ''
    for c in value:
        if c.isdigit():
            c = '#'
        new_value += c
    
    return new_value
