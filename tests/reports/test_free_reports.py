from app.services.BAD.classes.free_report_module import FreeReport
from tests.reports.responses import *
from tests.reports.fixtures import *
from tests.reports.mocks import mock_influx, mock_request, mock_db


class TestCompanyClass(object):
    def setup_method(self):
        self.test_class = FreeReport()
        self.vin = 'X4XKR094200K24720'
        self.number_plate = 'Т733АЕ178'

    async def test_by_number_plate_service(self):
        with mock_request(return_value=car_info_np_response):
            result = await self.test_class.by_number_plate_service.request(self.number_plate)
        result['id'] = '7cbc6bff-e475-4a33-86d0-cb2b93b6fef4'
        assert result == basic_report_np

    async def test_by_vin_number_service(self):
        with mock_request(return_value=car_info_vin_response):
            result = await self.test_class.by_vin_number_service.request(self.vin)
        result['id'] = '7cbc6bff-e475-4a33-86d0-cb2b93b6fef4'
        assert result == basic_report_vin

    async def test_report_invoke_by_vin(self):
        with mock_request(return_value=car_info_vin_response), mock_influx(), mock_db(
            'free_report_module.FreeReport._create_report', return_value=None
        ):
            result = await self.test_class.invoke(self.vin)
        result['id'] = '7cbc6bff-e475-4a33-86d0-cb2b93b6fef4'
        assert result == free_report_vin

    async def test_report_invoke_by_number_plate(self):
        with mock_request(return_value=car_info_np_response), mock_influx(), mock_db(
            'free_report_module.FreeReport._create_report', return_value=None
        ):
            result = await self.test_class.invoke(self.number_plate)
        result['id'] = '7cbc6bff-e475-4a33-86d0-cb2b93b6fef4'
        assert result == free_report_np
