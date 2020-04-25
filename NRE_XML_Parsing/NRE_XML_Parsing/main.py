from getxml import getnrexml
from xmltocsv import xmltocsv
from csvtodf import csvtodf
from bs4 import BeautifulSoup


def main():

    filepath = 'C:\\Users\\gwilliams\\Desktop\\Python Experiments\\work projects\\NRE_XML_Parsing\\'
    filename = 'NRE_Data_Extracted.csv'
    #These usernames and password require an account to be created for the National Rail DataPortal
    #Such an account can be created at https://opendata.nationalrail.co.uk/registration
    #Note that accounts are deleted by NR after 6 months of inactivity.

    userid = 'gregory.williams@orr.gov.uk'
    userpassword = 'ORRis1derful!'

    #use getnrexml to get xml file directly from NRE
    print("starting to get the NRE XML Data from NRE...\n")
    xml = getnrexml(userid,userpassword)
    
    #use getrawxml to open a historical raw xml file
    #xml = getrawxml("C:\\Users\\gwilliams\\Documents\\GitHub\\NRE_XML_Parsing\\NRE_XML_Parsing\\NRE_XML_Parsing\\raw_xml_data\\","NRE_Station_Dataset_2019_raw.xml")
    
    xmltocsv(xml,filepath,filename ,1)

    #convert to pandas dataframe
    df = csvtodf(filepath,filename)

    #convertdf to xlsx
    df.to_excel(filepath + filename.replace('csv','xlsx'),sheet_name='NRE_Data')

    #placeholder for importing into datawarehouse later
    #senddatatodw(df)


    def getrawxml(fp,fn):
        """
        This is to read in a previously extracted XML file and to pass it onto the generic process.

        Parameters
        fp:     A string representing the file path to the raw file
        fn:     A string representing the file name of the raw file

        Returns:
        xml_file:   A string containing the raw xml file.
        """
        print("starting to get the NRE XML Data from historical file")
        infile = open(fp,fn,"r",encoding="utf-8")
        xml_file = infile.read()
        return xml_file


if __name__ == '__main__':
    main()