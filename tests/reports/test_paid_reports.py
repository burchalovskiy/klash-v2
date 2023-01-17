from app.services.BAD.classes.paid_report_module import PaidReport
from tests.reports.responses import *
from tests.reports.fixtures import *
from tests.reports.mocks import mock_request


class TestCompanyClass(object):
    def setup_method(self):
        self.test_class = PaidReport()
        self.vin = 'X4XKR094200K24720'
        self.number_plate = 'Т733АЕ178'

    async def test_registration_service(self):
        with mock_request(return_value=registrations_response):
            result = await self.test_class.registrations_service.request(self.number_plate)
        assert result == registration

    async def test_fines_service(self):
        with mock_request(return_value=fines_response):
            result = await self.test_class.fines_service.request(self.vin)
        assert result == fines

    async def test_policy_info_service(self):
        with mock_request(return_value=policy_info_response):
            result = await self.test_class.policy_service.request(self.vin)
        assert result == policy

    async def test_wanted_info_service(self):
        with mock_request(return_value=wanted_info_response):
            result = await self.test_class.wanted_service.request(self.vin)
        assert result == wanted

    async def test_restricted_info_service(self):
        with mock_request(return_value=restricted_info_response):
            result = await self.test_class.restricted_service.request(self.vin)
        assert result == restricted

    async def test_pts_info_service(self):
        with mock_request(return_value=pts_response):
            result = await self.test_class.pts_service.request(self.vin)
        assert result == pts

    async def test_taxi_info_service(self):
        with mock_request(return_value=taxi_response):
            result = await self.test_class.taxi_service.request(self.vin)
        assert result == taxi

    async def test_mileage_info_service(self):
        with mock_request(return_value=mileage_info_response_good):
            result = await self.test_class.mileage_service.request(self.vin)
        assert result == mileage_good

        with mock_request(return_value=mileage_info_response_bad):
            result = await self.test_class.mileage_service.request(self.vin)
        assert result == mileage_bad
