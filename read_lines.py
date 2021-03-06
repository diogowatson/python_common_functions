def read_lines(number_of_lines, file, output_file):
    '''
    Read an N number of lines of a file and save it in a new file
    @param:
        number_of_lines    - Required : number of lines to be read (int)
        file               - Required : file to be read (str)
        output_file        - Required : output file (str)
    '''
    with open(file) as f, open(output_file,'w+') as out:
        head = [next(f) for x in range(number_of_lines)]
        out.writelines(head)
        
        out.close()
        f.close()
