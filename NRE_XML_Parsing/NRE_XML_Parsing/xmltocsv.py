from bs4 import BeautifulSoup
import csv
from html.parser import HTMLParser
import datetime


def xmltocsv(xlmstring,outputfilepath, filename,sourceitemid):
    """
    This takes a string in XML fomat an converts it to a CSV file.  It also strips out HTML tags, formats dates and adds sourceitemid and date of extraction information

    Parameters
    xmlstring:      a string containing NRE XML data
    outputfilepath: a string specifying the file path where data is sent
    filename:       a string specifying the csv filename
    sourceitemid:   a number specifying the sourceitemid number for later loading into the datawarehouse

    Returns
    A CSV file exported to the outputfilepath
    datafile:       
    """


    #fd = open("xmlsample.xml", encoding='utf-8')  
    #soup = BeautifulSoup(fd,'lxml-xml', from_encoding='utf-8')

    soup = BeautifulSoup(xlmstring,'lxml-xml')

    print("preparing the csv file")
    #create a blank csv object
    datafile = open(outputfilepath + filename, 'w',newline='')
    csvwriter = csv.writer(datafile)

    #create the header of the csv file
    station_data_head = []
    station_data_head.append('source_item_id')
    station_data_head.append('datedataextractedfromNRE')
    station_data_head.append('ChangedBy') 
    station_data_head.append('ChangeDate')
    station_data_head.append('CrsCode')
    station_data_head.append('NationalLocationCode')
    station_data_head.append('Station_Name')
    station_data_head.append('Sixteen Character Name')
    station_data_head.append('PostalAddressLine_1')
    station_data_head.append('PostalAddressLine_2')
    station_data_head.append('PostalAddressLine_3')
    station_data_head.append('PostalAddressLine_4')
    station_data_head.append('PostCode')
    station_data_head.append('Longitude')
    station_data_head.append('Latitude')
    station_data_head.append('StationOperator')
    station_data_head.append('StationStaffing')
    station_data_head.append('CustomerHelpPoints')
    station_data_head.append('StaffHelpAvaliable')
    station_data_head.append('StaffHelpAvaliableNotes')
    station_data_head.append('InductionLoop')
    station_data_head.append('AccessibleTicketMachines')
    station_data_head.append('HeightAdjustedTicketCounter')
    station_data_head.append('RampForTrainAccess')
    station_data_head.append('Nearest Station with more facilities1')
    station_data_head.append('Nearest Station with more facilities2')
    station_data_head.append('NationalKeyToilet')
    station_data_head.append('StepFreeNotes')
    station_data_head.append('StepAccessCoverage')
    station_data_head.append('ImpairedMobilitySetDown')
    station_data_head.append('WheelchairsAvailable')
    station_data_head.append('CarparkSpaces')
    station_data_head.append('CarparkAcccessibleSpaces')
    station_data_head.append('AcccessibleTaxiNotes')
    station_data_head.append('AccessibleCarparkEquipment')
    station_data_head.append('CarparkCCTV')
    station_data_head.append('TOCRef')
    station_data_head.append('AccessibleCarparkEquipmentNote')
    station_data_head.append('Helpline_number')
    station_data_head.append('Helpline_open_Monday_to_Sunday')
    station_data_head.append('Helpline_open')
    station_data_head.append('Helpline_closed')
    station_data_head.append('Helpline_notes')
    station_data_head.append('CarPark_EmailAddress')
    station_data_head.append('CarParkCharges_Off-Peak')
    station_data_head.append('CarParkCharges_PerHour')
    station_data_head.append('CarParkCharges_Daily')
    station_data_head.append('CarParkCharges_Weekly')
    station_data_head.append('CarParkCharges_Monthly')  
    station_data_head.append('CarParkCharges_ThreeMonthly')  
    station_data_head.append('CarParkCharges_SixMonthly')    
    station_data_head.append('CarParkCharges_Annual')
    station_data_head.append('CarParkCharges_Saturday')
    station_data_head.append('CarParkCharges_Sunday')  
    station_data_head.append('CarParkCharges_Note') 
    #requested by Chris Casanovas

    
     
      #,[CarPark_Charges_Note_cdata]

    #populate the csv with the header
    csvwriter.writerow(station_data_head)
    
    #create list for the station data
    station_data = []

    print("Extracting the data from the XML file\n")

    #get each set of station data
    for count,stn in enumerate(soup.find_all('Station')):
       #get individual elements
        
        try:
            changedby = stn.ChangeHistory.ChangedBy.get_text()
        except AttributeError:
            changedby = None

        try:
            changeddate = stn.ChangeHistory.LastChangedDate.get_text()
        
        except AttributeError:
            changeddate = None

        try:
            crscode = stn.CrsCode.get_text()
        except AttributeError:
            crscode = None

        try:
            nlc = stn.AlternativeIdentifiers.NationalLocationCode.get_text()
        except AttributeError:
            nlc = None

        try:
            stn_name = stn.Name.get_text()
        except AttributeError:
            stn_name = None
        
        try:
            sixteencharname = stn.SixteenCharacterName.get_text()
        except AttributeError:
            sixteencharname = None

        #loop through children elements with same names and append to a list
        add_list = []
        for child in stn.Address.PostalAddress.A_5LineAddress.stripped_strings:
            add_list.append(child)  
            
        add1 = add_list[0]
        add2 = add_list[1]
        add3 = add_list[2]
        add4 = add_list[3]

        try:
            postcode = stn.Address.PostalAddress.A_5LineAddress.PostCode.get_text()
        except AttributeError:
            postcode = None

        try: 
            long = stn.Longitude.get_text()
        except AttributeError:
            long = None

        try:
            lat = stn.Latitude.get_text()
        except AttributeError:
            lat = None

        try:
            stnoperator = stn.StationOperator.get_text()
        except AttributeError:
            stnoperator = None
        
        try:
            stnstaffing = stn.Staffing.StaffingLevel.get_text()
        except AttributeError:
            stnstaffing = None
            
        try:
            cust_helpppoints = stn.InformationSystems.CustomerHelpPoints.Available.get_text()
        except AttributeError:
            cust_helppoints = None

        try:
            staffhelpflag = stn.Accessibility.StaffHelpAvailable.Available.get_text()
        except AttributeError:
            staffhelpflag = None

        try:
            staffhelpnote = stn.Accessibility.StaffHelpAvailable.Annotation.Note.get_text()
        except AttributeError:
            staffhelpnote = None

        try:
            inductionloop = stn.Accessibility.InductionLoop.get_text()
        except AttributeError:
            inductionloop = None
        
        try:
            accessibleticketmachines = stn.Accessibility.AccessibleTicketMachines.Available.get_text()
        except AttributeError:
            accessibleticketmachines = None

        try:
            heightadjustedcounter = stn.Accessibility.HeightAdjustedTicketOfficeCounter.Available.get_text()
        except AttributeError:
            heightadjustedcounter = None

        try:
            trainramp = stn.Accessibility.RampForTrainAccess.Available.get_text()
        except AttributeError:
            trainramp = None

        #loop through children elements with same names and append to a list
        stnlist = []
        try:
            for sub_stn1 in stn.Accessibility.NearestStationsWithMoreFacilities.stripped_strings:
                
                #print(type(sub_stn1))
                
                stnlist.append(sub_stn1)
               
                try:
                    neareststation1 = stnlist[0]
                except IndexError:
                    neareststation1 = None

                try:
                    neareststation2 = stnlist[1]
                except IndexError:
                    neareststation2 = None
  
        except AttributeError:
            neareststation1 = None

        try:
            natkeytoilet = stn.Accessibility.NationalKeyToilets.Available.get_text()
        except AttributeError:
            natkeytoilet = None

        try:
            stepfreenotes = stn.Accessibility.StepFreeAccess.Annotation.Note.get_text()
        except AttributeError:
            stepfreenotes = None

        try:
            stepaccesscoverage = stn.StepFreeAccess.Coverage.get_text()
        except AttributeError:
            stepaccesscoverage = None

        try:
            setdown = stn.Accessibility.ImpairedMobilitySetDown.Available.get_text()
        except AttributeError:
            setdown = None

        try:
            wheelchairs = stn.Accessibility.WheelchairsAvailable.Available.get_text()
        except AttributeError:
            wheelchairs = None

        try:
            carparkspaces = stn.Interchange.CarPark.Spaces.get_text()
        except AttributeError:
            carparkspaces = None
  
        try:
            carparkaccessablespaces = stn.Interchange.CarPark.NumberAccessibleSpaces.get_text()
        except AttributeError:
            carparkaccessablespaces = None

        try:
            accessibletaxinotes = stn.Accessibility.AccessibleTaxis.Annotation.Note.get_text()
        except AttributeError:
            accessibletaxinotes = None
    
        try:
            accessiblecarparkequipment = stn.Interchange.CarPark.AccessibleCarParkEquipment.get_text()
        except AttributeError:
            accessiblecarparkequipment = False
        
        try:
            carparkcctv = stn.Interchange.CarPark.Cctv.get_text()
        except AttributeError:
            carparkcctv = False
        
        try:
            tocref = stn.TrainOperatingCompanies.TocRef.get_text()
        except AttributeError:
            tocref = None

        try:
            accessiblecarparkequipmentnote = stn.Interchange.CarPark.AccessibleCarParkEquipmentNote.get_text()
        except AttributeError:
            accessiblecarparkequipmentnote = None
        
        try:
            helpline_number = stn.Accessibility.Helpline.ContactDetails.Annotation.Note.get_text()
        except AttributeError:
            helpline_number = None
        
        try:
            helpline_days_open = stn.Accessibility.Helpline.Open.DayAndTimeAvailability.DayTypes.MondayToSunday.get_text()
        except AttributeError:
            helpline_days_open = None
        
        try:
            helpline_open = stn.Accessibility.Helpline.Open.DayAndTimeAvailability.OpeningHours.StartTime.get_text()
        except AttributeError:
            helpline_open = None

        try:
            helpline_closed = stn.Accessibility.Helpline.Open.DayAndTimeAvailability.OpeningHours.EndTime.get_text()
        except AttributeError:
            helpline_closed = None
        
        try:
            helpline_notes = stn.Accessibility.Helpline.Annotation.Note.get_text()
        except AttributeError:
            helpline_notes = None
        try:
            carparkemail = stn.Interchange.CarPark.EmailAddress.get_text()
        except AttributeError:
            carparkemail = None

        try:
            carparkchargesoffpeak = stn.CarPark.Charges.Offpeak.get_text()
        except AttributeError:
            carparkchargesoffpeak = None

        try:
            carparkchargesperhour = stn.CarPark.Charges.PerHour.get_text()
        except AttributeError:
            carparkchargesperhour = None
        
        try:
            carparkchargesdaily = stn.CarPark.Charges.Daily.get_text()
        except AttributeError:
            carparkchargesdaily = None
        
        try:
            carparkchargesweekly = stn.CarPark.Charges.Weekly.get_text()
        except AttributeError:
            carparkchargesweekly = None

        try:
            carparkchargesmonthly = stn.CarPark.Charges.Monthly.get_text()
        except AttributeError:
            carparkchargesmonthly = None

        try:
            carparkchangesthreemonthly = stn.CarkPark.Charges.ThreeMonthly.get_text()
        except AttributeError:
            carparkchargesthreemonthly = None
        
        try:
            carparkchargessixmonthly = stn.CarPark.Charges.SixMonthly.get_text()
        except AttributeError:
            carparkchargessixmonthly = None
        
        try:
            carparkchargesannual = stn.CarPark.Charges.Annual.get_text()
        except AttributeError:
            carparkchargesannual = None
        
        try:
            carparkchargessaturday = stn.CarPark.Charges.Saturday.get_text()
        except AttributeError:
            carparkchargessaturday = None
        
        try:
            carparkchargessunday = stn.CarPark.Charges.Sunday.get_text()
        except AttributeError:
            carparkchargessunday = None

        try:
            carparkchargesnote = stn.CarPark.Charges.Note.get_text()
        except AttributeError:
            carparkchargesnote = None



        #format date
        changeddate = changeddate.replace('T00:00:00.000Z','')
        changeddate = changeddate.replace('T00:00:00.000+01:00','')
        if helpline_open:
            helpline_open = helpline_open.replace(':00.000','')

        if helpline_closed:
            helpline_closed = helpline_closed.replace(':00.000','')


        #strip html tags
        if neareststation1:
            neareststation1 = strip_tags(neareststation1)

        if neareststation2:
            neareststation2 = strip_tags(neareststation2)

        if stepfreenotes:
            stepfreenotes = strip_tags(stepfreenotes)
        
        if staffhelpnote:
            staffhelpnote = strip_tags(staffhelpnote)
        
        if accessibletaxinotes:
            accessibletaxinotes = strip_tags(accessibletaxinotes)
        
        if carparkchargesnote:
            carparkchargesnote = strip_tags(carparkchargesnote)
        
        if helpline_number:
            helpline_number = strip_tags(helpline_number)

        if helpline_notes:
            helpline_notes = strip_tags(helpline_notes)


        #add the elements from the dictionaries to the list
        station_data.append(sourceitemid)
        station_data.append(datetime.date.today())
        station_data.append(changedby)
        station_data.append(changeddate)
        station_data.append(crscode)
        station_data.append(nlc)
        station_data.append(stn_name)
        station_data.append(sixteencharname)
        station_data.append(add1)
        station_data.append(add2)
        station_data.append(add3)
        station_data.append(add4)
        station_data.append(postcode)
        station_data.append(long)
        station_data.append(lat)
        station_data.append(stnoperator)
        station_data.append(stnstaffing)
        station_data.append(cust_helpppoints)
        station_data.append(staffhelpflag)
        station_data.append(staffhelpnote)
        station_data.append(inductionloop)
        station_data.append(accessibleticketmachines)
        station_data.append(heightadjustedcounter)
        station_data.append(trainramp)
        station_data.append(neareststation1)
        station_data.append(neareststation2)
        station_data.append(natkeytoilet)
        station_data.append(stepfreenotes)
        station_data.append(stepaccesscoverage)
        station_data.append(setdown)
        station_data.append(wheelchairs)
        station_data.append(carparkspaces)
        station_data.append(carparkaccessablespaces)
        station_data.append(accessibletaxinotes)
        station_data.append(accessiblecarparkequipment)
        station_data.append(carparkcctv)
        station_data.append(tocref)
        station_data.append(accessiblecarparkequipmentnote)
        station_data.append(helpline_number)
        station_data.append(helpline_days_open)
        station_data.append(helpline_open)
        station_data.append(helpline_closed)
        station_data.append(helpline_notes)
        station_data.append(carparkemail)
        station_data.append(carparkchargesoffpeak)
        station_data.append(carparkchargesperhour)
        station_data.append(carparkchargesdaily)
        station_data.append(carparkchargesweekly)
        station_data.append(carparkchargesmonthly)
        station_data.append(carparkchargesthreemonthly)
        station_data.append(carparkchargessixmonthly)
        station_data.append(carparkchargesannual)
        station_data.append(carparkchargessaturday)
        station_data.append(carparkchargessunday)
        station_data.append(carparkchargesnote)




        #write the list to the CSV file
        csvwriter.writerow(station_data)
        print(f"\r{count} stations written to file", end="")

        #clear the list to prepare next row
        station_data = []

        #close the csv file
    datafile.close()
    #print(type(datafile))
    
    print("\n All records written to file.  Finished.")
    return datafile


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


if __name__ == '__main__':
    main()
