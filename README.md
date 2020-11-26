# Stations_Data_from_XML
This was written at the office of rail and road to automate the extraction of data relating to stations from NR's Open feeds source.

# Installation
This was written as a Visual Studio project, so VS will be required to open the .sln file.

# Usage
An account needs to be created for the National Rail data portal [here](https://opendata.nationalrail.co.uk/registration).  These accounts last for 6 months before they expire.
set the `userid` and `userpassword` variables in lines 13 and 14 of `main` to pass your credentials to the URL request.

The stations data will be exported both as a raw xml file and as a csv file in the "output" folder within the project.


