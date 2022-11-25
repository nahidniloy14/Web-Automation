import pytest


@pytest.fixture()
#@pytest.fixture(scope="class")  # will be executed in the class level
def setup():
    print("I am header")
    yield  # will wait until the header gets printed and then after it will to start working with the footer
    print("I am footer")


#used in dataDrivenFixture.py
def dataLoad():
    print("User Created")
    return ("name", "age", "gmail")

#used in multiple dataset.py
@pytest.fixture(params=["chrome","firefox","brave"])
#@pytest.fixture(params=[("chrome","1200"),("firefox","None","1300"),"brave"])
def browser(request):
    return request.param


# conftest will be available to all fixture  related tests
