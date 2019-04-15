def percentage(x, y):
    """
    Give the percentage of a value base on a total value
    @params:
        x   - Required : value of percentage to be obtained
        y   - Required : total value from where percentage will be obtained

    @return:
       - percentage value as string (str)
       - if any of the values is zero the operation can't be performed
         then, the function will return 'N/A'
    """
    if x != 0 and y != 0:
        result = float(((x) / y) * 100)
        
        return '%' + '{0:.2f}'.format(result)  # return only 2 number after .
    else:
        return '%0'
