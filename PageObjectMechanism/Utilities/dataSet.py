import pytest

# data_tuple = [("Nahid Hassan", "Niloy", "1414"), ("Nabil", "Hossain", "0417"), ("Joy", "Rahaman", "0457")]
# data_dictonary = [{"firstName": "Nahid Hassan", "lastName": "Niloy","postalCode":"1414"},
#                   {"firstName": "Nabil", "lastName": "Hossain","postalCode":"1424"}, ]
from PageObjectMechanism.TestData.homePageData import HomePageData

@pytest.fixture(params=HomePageData.data_dictonary)
def getData(self, request):
    return request.param
