def check_file_exit(file, message=None):

    '''
    Checks if a file exists. Abort with a message if don't
    :param file       - Required : path and name of file (str) 
    :param message:   - Optional : custom aborting message
    :return:
           True  - if file exists (Bool)
           end script if file don't exist
    '''     
    # default message
    message = file + " can't be found. Aborting the script "
    if os.path.isfile(file):
        
        return True
    
    else:
        sys.exit(message)
