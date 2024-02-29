import requests, json
import copy
import pytest
from utilities import *
from request_payload import *


@pytest.mark.usefixtures("url_link")
class TestApi:
    header = {'Content-Type': 'application/json'}
    user_id = None
    application_id = None
    company_name = None
    employee_id = None
    offer_prop_id = None
    pincode = "400708"
    district = None

    def test_send_otp(self, url_link):
        response = post_req(url_link + "/user/send-otp/", send_otp_payload(), TestApi.header)
        assert response["status_code"] == 200
        assert "OTP has been sent" in response['message']

    def test_validate_otp(self, url_link):
        response = post_req(url_link + "/user/super-app/validate-otp", validate_otp_payload(), TestApi.header)
        token = "Token " + response["data"]["token"]
        TestApi.header["Authorization"] = token
        TestApi.user_id = response["data"]['user_id']
        assert response['status_code'] == 200
        assert "Successfull" in response['message']

    def test_dashboard_one(self, url_link):
        response = post_req(url_link + "/user/verify-user-superdashboard", dashboard_one(), TestApi.header)
        assert response['status_code'] == 200
        assert "succesfully" in response['message']

    def test_submit_name(self, url_link):
        response = post_req(url_link + "/user/super-app/submit-name", submmit_name(), TestApi.header)
        TestApi.company_name = response['data']['company_details']['name']
        TestApi.employee_id = response['data']['company_details']['id']
        assert response['status_code'] == 200
        assert "Successfully" in response['message']

    def test_get_value(self, url_link):
        response = get_req(url_link + "/user/super-app/get-employment-details?loan_id=", TestApi.header)
        assert response['status_code'] == 200
        assert "Successfully" in response['message']

    def test_check_employee_details(self, url_link):
        response = post_req(url_link + "/user/super-app/check-employment-details",
                            check_employee_details(TestApi.company_name), TestApi.header)
        assert response['status_code'] == 200

    def test_submit_employee_details(self, url_link):
        response = post_req(url_link + "/user/super-app/submit-employment-details",
                            submit_employee_details(TestApi.employee_id, TestApi.company_name), TestApi.header)
        assert response['status_code'] == 200

    def test_dashboard_two(self, url_link):
        response = post_req(url_link + "/user/verify-user-superdashboard", dashboard_two(), TestApi.header)
        assert response['status_code'] == 200

    def test_create_loan_application(self, url_link):
        response = post_req(url_link + "/loan-application/v2/create-loan-application", create_loan_appliaction(),
                            TestApi.header)
        TestApi.application_id = response['data']['application_id']
        assert response['message'] == "Loan Application Created."

    def test_product_rule(self, url_link):
        response = get_req(url_link + "/loan-application/v1/fetch-product-rules", TestApi.header)
        assert response['status_code'] == 200

    def test_pan_validation(self, url_link):
        response = post_req(url_link + "/external-api/v1/validate-document", pan_validation(TestApi.application_id),
                            TestApi.header)
        assert response['status_code'] == 200

    def test_get_employee_details(self, url_link):
        response = get_req(url_link + "/user/super-app/get-employment-details?%s" % TestApi.application_id,
                           TestApi.header)
        assert response['status_code'] == 200

    def test_record_app_log(self, url_link):
        response = post_req(url_link + "/user/record-app-log/%s" % TestApi.user_id, record_app_log(TestApi.user_id),
                            TestApi.header)
        assert response['status_code'] == 200

    def test_validate_ocr(self, url_link):
        header = copy.deepcopy(TestApi.header)
        header.pop("Content-Type")
        files = {"file_front": open("ocr/front_aadhar.jpeg", "rb"), "file_back": open("ocr/back_aadhar.jpeg", "rb")}
        response = post_ocr(url_link + "/external-api/v1/validate-ocr", aadhaar_ocr(TestApi.application_id), files,
                            header)
        assert response['status_code'] == 200

    def test_get_application_nature_one(self, url_link):
        response = get_req(url_link + "/loan-application/v1/get-application-nature/%s" % TestApi.application_id,
                           TestApi.header)
        assert response['status_code'] == 200

    def test_income_page(self, url_link):
        response = post_req(url_link + "/loan-application/v1/loan-application", income_page(TestApi.application_id),
                            TestApi.header)
        assert response['status_code'] == 200

    def test_get_application_nature_two(self, url_link):
        response = get_req(url_link + "/loan-application/v1/get-application-nature/%s" % TestApi.application_id,
                           TestApi.header)
        assert response['status_code'] == 200

    def test_selfie_upload(self, url_link):
        header = copy.deepcopy(TestApi.header)
        header.pop("Content-Type")
        file = {"selfie": open("ocr/abhi_pass_img.jpeg", "rb")}
        payload = {}
        response = selfie_upload(url_link + "/user/edit-appuser/", payload, file, header)
        # if response["data"]["stage"] == 1:
        #     response = selfie_upload(url_link + "/user/edit-appuser/", payload, file, header)
        assert response['status_code'] == 200

    def test_update_appl_stage_from_pre_approved(self, url_link):
        payload = {}
        response = post_req(url_link + "/loan-application/v1/update-application-stage-from-pre-arppove/%s" % TestApi.application_id, payload,
                            TestApi.header)
        assert response['status_code'] == 200

    def test_fetch_offer_proposed(self, url_link):
        response = post_req(url_link + "/loan-application/v1/fetch-proposed-offer", fetch_offer_proposed(TestApi.application_id),
                            TestApi.header)
        TestApi.offer_prop_id = response["data"]["offer_data"][0]["id"]
        assert response['status_code'] == 200

    def test_offer_accept(self, url_link):
        response = put_req(url_link + "/central-api/v1/call-api", offer_accept(TestApi.offer_prop_id), TestApi.header)
        assert response['status_code'] == 200

    def test_get_accept_offer_info_one(self, url_link):
        response = get_req(url_link + "/central-api/v1/call-api?source=LMS&datapoint=get_accepted_offers&endpoint=%s" % TestApi.application_id,
                           TestApi.header)
        assert response['status_code'] == 200

    def test_nominee_details(self, url_link):
        response = post_req(url_link + "/loan-application/v1/add-edit-user-references", nominee_details(TestApi.application_id),
                            TestApi.header)
        assert response['status_code'] == 200

    def test_get_accept_offer_info_two(self, url_link):
        response = get_req(url_link + "/central-api/v1/call-api?source=LMS&datapoint=get_accepted_offers&endpoint=%s" % TestApi.application_id,
                           TestApi.header)
        assert response['status_code'] == 200

    def test_add_address_pincode(self, url_link):
        response = get_req(url_link + "/platform-central/get-pincode-data/%s" % TestApi.pincode, TestApi.header)
        TestApi.district = response["data"]["district"]
        assert response['status_code'] == 200

    def test_save_address(self, url_link):
        response = post_req(url_link + "/loan-application/v1/add-address/%s" % TestApi.application_id,
                            save_address(TestApi.district, TestApi.pincode), TestApi.header)
        assert response['status_code'] == 200


