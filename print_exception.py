import os, sys

def print_exception(e):
    """
    print an customized exception
    param@:
        e   -Required : exeception string
        
    usage:
        - Use function after an except Exception catch
        example:
        except Exeption as e:
            print_exception(e)
    """
    
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno, e)
