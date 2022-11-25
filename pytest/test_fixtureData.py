import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2():
    def test_editProfile(self,dataLoad): #if we have to return dataLoad
        print(dataLoad)
        print(dataLoad[1])
# @pytest.mark.usefixtures("dataLoad")
# class EditProfile(BaseClass):
#   le  def test_editprofile(self, dataLoad):
#         log = self.getlogger()
#         log.info(dataLoad[0])
#if we want to return data we should pass fixture name also