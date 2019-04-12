def test_dic(dic):
    '''
    Print a dictionary keys and lenght
    Used to check if a Dic has arrays of same value before being converted to Pandas DataFrame
    @param:
        dic     - Required : python dictionary (dic)
    '''
    for keys in dic:
        print('{} : {}'.format(keys, len(dic[keys])))
