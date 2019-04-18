def file_len(fname):
    """
    Returns the number of lines of a file
    @param:
         - fname    - Required : file name and path (str) 
    
    @return:
         - Number of lines (int) 
    """
    
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
