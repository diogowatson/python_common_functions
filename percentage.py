def percentage(x, y):
    '''
    Give the percentage of a value base on a total value
    @params:
        x   - Required : value of percentage to be obtained
        y   - Required : total value from whre percentage will be obtained
    
    @return:
       - percentage value as string (str)
       - if any of the values is zero the operatin can't be performed
         then, the function will return 'N/A'
    '''
    if x != 0 and y != 0:
        percentage = lambda x, y: int(((x) /y) * 100)
        
        return '%' + str(percentage(x, y))
    else:
        
        return 'N/A'
