from getxml import getnrexml
from xmltocsv import xmltocsv
from csvtodf import csvtodf

def main():

    filepath = 'C:\\Users\\gwilliams\\Desktop\\Python Experiments\\work projects\\NRE_XML_Parsing\\'
    filename = 'NRE_Data_Extracted.csv'
    #These usernames and password require an account to be created for the National Rail DataPortal
    #Such an account can be created at https://opendata.nationalrail.co.uk/registration
    #Note that accounts are deleted by NR after 6 months of inactivity.

    userid = 'gregory.williams@orr.gov.uk'
    userpassword = 'ORRis1derful!'

    print("starting to get the NRE XML Data from NRE...\n")
    xml = getnrexml(userid,userpassword)
    
    xmltocsv(xml,filepath,filename ,99)

    #convert to pandas dataframe
    df = csvtodf(filepath,filename)

    #convertdf to xlsx
    df.to_excel(filepath + filename.replace('csv','xlsx'),sheet_name='NRE_Data')

    #placeholder for importing into datawarehouse later
    #senddatatodw(df)

if __name__ == '__main__':
    main()