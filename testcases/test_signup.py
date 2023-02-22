import pytest
import softest as softest
from pages2.signup_launch_page import LoginLaunchPage
from ddt import ddt, data, file_data, unpack
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestEnterDetails(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def form_setup(self):
        self.llp = LoginLaunchPage(self.driver)

    # @data(("Rohit", "Sharma", "rohitsharma@gmail.com", "IT Manager", "HelloIT", "75", 1234567890, "FR"))
    # @unpack
    # @file_data("../testdata/details.json")
    # @file_data("../testdata/detail_2.yaml")
    # @data(*Utils.read_data_from_excel("D:\\Book1excel.xlsx", "Sheet2"))
    @data(*Utils.read_data_from_csv("C:\\Users\\nagar\\PycharmProjects\\testEnterLogin\\testdata\\user_details2.csv"))
    @unpack
    def test_enter_fields(self, fr_nm, l_n, email, job_title, com_name, no_of_com_emp, ph_no, com_country):
        user_details = self.llp.enter_data_to_fields(fr_nm, l_n, email, job_title, com_name, no_of_com_emp, ph_no,
                                                     com_country)
        # if user_details == True:
        #     self.log.info("Successfully done...")
        # elif user_details != True:
        #     self.log.warning("something went wrong")

# how to run
# pytest -vs --html=reports/report1.html
