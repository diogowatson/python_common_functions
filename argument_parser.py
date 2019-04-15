def create_argument_parser():
    '''
    argument parser
    basic usage:
        parser = create_argument_parser()
        args = parser.parse.parse_args()

    '''
    arg_parser = argparse.ArgumentParser(description='Script to parser arguments')
    arg_parser.add_argument('input_file',
                            type=str,
                            help='path and name of input file')
    arg_parser.add_argument('output_file',
                            type=str,
                            help='output file name and path')
    
    return arg_parser
