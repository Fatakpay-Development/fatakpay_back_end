import requests, json
from datetime import datetime, date, timedelta


def perform_api_request(method, API, payload, TYPE):
    headers = {"Authorization": "Token ad3333b418f170e055a10b0c3941a6eccd16719d"}
    if method == "POST":
        response = requests.post(API, json=payload, headers=headers)
    else:
        response = requests.get(API, params=payload, headers=headers)
    response_data = response.json()
    if TYPE == "LIST":
        if "data" in response_data:
            response_data = response_data['data']['results']
    return response_data


#### Perform the API call
def processTheUserData(mobile, final_amount, final_max_amount):
    PRE_APPROVED_LIST_API = "https://devadminapi.fatakpay.com/central-api/v1/call-api"
    ### process the payload+
    pre_approved_payload = {}
    pre_approved_payload['datapoint'] = "loan_application_list_view"
    pre_approved_payload['stage_id'] = "9"
    pre_approved_payload['source'] = "Onboarding"
    pre_approved_payload['product_master'] = "1"
    pre_approved_payload['flag'] = "all"
    pre_approved_payload['name'] = mobile
    ### call the API
    pre_approved_data = perform_api_request("GET", PRE_APPROVED_LIST_API, pre_approved_payload, "LIST")
    if len(pre_approved_data) == 0:
        return "Application not found"
    application_id = pre_approved_data[0]['id']
    print(application_id)
    ###### now move the application to underwriting
    STAGE_CHANGE_API_URL = "https://devadminapi.fatakpay.com/central-api/v1/call-api"
    ### process the payload
    move_underwriting_payload = {}
    move_underwriting_payload['applications'] = f"[{application_id}]"
    move_underwriting_payload['datapoint'] = "update_multi_application_status"
    move_underwriting_payload['remarks'] = "Moved from automation script"
    move_underwriting_payload['source'] = "Onboarding"
    move_underwriting_payload['stage_id'] = "3"
    ### call the API
    underwriting_data = perform_api_request("POST", STAGE_CHANGE_API_URL, move_underwriting_payload, "STAGE_MOVEMENT")
    print(underwriting_data)
    ###### now give the manual offer
    GIVE_MANUAL_OFFER_API = "https://devadminapi.fatakpay.com/central-api/v1/call-api"
    ### process the payload
    manual_offer_payload = {}
    manual_offer_payload['application_id'] = application_id
    manual_offer_payload['datapoint'] = "manual_offer"
    manual_offer_payload['final_amount'] = final_amount
    manual_offer_payload['final_max_amount'] = final_max_amount
    manual_offer_payload['source'] = "Onboarding"
    ### call the API
    manual_offer_data = perform_api_request("POST", GIVE_MANUAL_OFFER_API, manual_offer_payload, "MANUAL_OFFER")
    print(manual_offer_data)

    
mobile = input("Enter the mobile number: ")
final_amount = input("Enter the final amount: ")
final_max_amount = input("Enter the final max amount: ")
processTheUserData(mobile, final_amount, final_max_amount)
