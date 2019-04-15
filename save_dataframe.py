import pandas as pd
from datetime import datetime as dt


def current_time():
    #returns current date in string format

    return dt.now().strftime('%Y-%m-%d %H %M %S')


def df_to_excel(df, outputFile, sheetName='sheet1'):
    '''save an pandas DataFrame to an Excel file
       @params:
           df            - Required : DataFrame to be converted (pandas dataFrame)
           outputFile    - Required : path and name of the output file (str)
           sheetName     - Optional : name of the sheet
    '''

    try:
        #.xlsx already in the outputfile string
        if '.xlsx' in outputFile:
            outputFile = outputFile +"_" + current_time()
        else:
            #in case user forgot '.xlsx extension'
            outputFile = outputFile +"_" + current_time()+ ".xlsx"

        writer = pd.ExcelWriter(outputFile, engine='xlsxwriter')
        df.to_excel(writer, sheetName)
        writer.save()
        writer.close()
        print("Success!! " + outputFile + " Created ")

    except Exception as e:
        print("Failed to convert File!: {}".format(e))
