from base_test import BaseTest
from pages.chair_page import ChairPage
from units.save_text import write_text


class GetData(BaseTest):
    def test_get_chair_data(self):
        chair_page = ChairPage(self.driver)
        vendor_code = chair_page.get_vendor_code()
        assert (vendor_code != None)
        availability_for_delivery = chair_page.get_availability_for_delivery()
        assert (availability_for_delivery != None)
        availability_forecast_in_Poland = chair_page.get_availability_forecast_in_Poland()
        assert (availability_forecast_in_Poland != None)
        availability_in_Lviv = chair_page.get_availability_in_Lviv()
        assert (availability_in_Lviv != None)
        list_result_data = [vendor_code, availability_for_delivery,
                            availability_forecast_in_Poland, availability_in_Lviv]
        for i in range(len(list_result_data)):
            list_result_data[i] = chair_page.check_list[i] + \
                ": " + list_result_data[i]
        text_result = " \n".join(list_result_data)
        write_text(text_result)
