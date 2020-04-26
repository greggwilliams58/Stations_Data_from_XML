import pytest
import requests
from main import getrawxml
from main import baby_test
from getxml import requesttoken


def test_requesttoken():
    response = requesttoken('greggwilliams58@gmail.com','Sardonic1789!')
    expected = "{'username': 'greggwilliams58@gmail.com', 'roles': {'ROLE_STANDARD': True, 'ROLE_KB_API': True}, 'token': 'greggwilliams58@gmail.com:1587918185000:bHweEQtGv26ykHytBJpJbG8JtH0pCzG0ZboIWqEzS7E='}"
    assert response['username'] == 'greggwilliams58@gmail.com'
    assert response['roles']['ROLE_STANDARD'] is True
    assert response['roles']['ROLE_KB_API'] is True
    assert response['token'].startswith("gregg")


@pytest.mark.parametrize("folder,filename",
[("C:\\Users\\Greg\\Documents\\GitHub\\Stations_Data_from_XML\\NRE_XML_Parsing\\NRE_XML_Parsing\\raw_xml_data\\",
  "NRE_Station_Dataset_2018_raw.xml"),
 ("C:\\Users\\Greg\\Documents\\GitHub\\Stations_Data_from_XML\\NRE_XML_Parsing\\NRE_XML_Parsing\\raw_xml_data\\",
  "NRE_Station_Dataset_2019_raw.xml")])
def test_getrawxml(folder,filename):
    answer = getrawxml(folder
                       ,filename)
    assert isinstance(answer, str) is True


@pytest.mark.parametrize("folder,filename",
[("C:\\Users\\Greg\\Documents\\GitHub\\Stations_Data_from_XML\\NRE_XML_Parsing\\NRE_XML_Parsing\\raw_xml_data\\",
  "NRE_Station_Dataset_2018_raw.xml"),
 ("C:\\Users\\Greg\\Documents\\GitHub\\Stations_Data_from_XML\\NRE_XML_Parsing\\NRE_XML_Parsing\\raw_xml_data\\",
  "NRE_Station_Dataset_2019_raw.xml")])
def test_getrawxml_is_xml(folder,filename):
    answer = getrawxml(folder,filename)
                       
    assert answer.startswith("<") is True

def test_get_rawxml_wrong_file_name():
    with pytest.raises(FileNotFoundError):
        getrawxml("C:\\Users","NRE_Station_Dataset_2018_raw.xml")


def test_baby_test():
    assert baby_test(3) == 4