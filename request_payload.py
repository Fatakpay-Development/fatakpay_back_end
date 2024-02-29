import requests, json


def send_otp_payload():
    data = {
        "mobile": "8788132556",
        "email_notify": "",
        "email": "",
        "device_details": {
            "device": "miel",
            "device_id": "26fe0069320a5836",
            "device_ip_address": "10.101.151.151",
            "xdevice_serial_number": "unknown",
            "device_model": "2201117PI",
            "device_type": "Handset",
            "device_mac_address": "",
            "device_manufacturer": "Xiaomi",
            "unique_id": "miel",
            "is_device_emulator": "false",
            "is_location_enabled": "true",
            "latitude": 19.117117117117118,
            "longitude": 72.86528623824486,
            "fcm_id": "cksa-JsqTX60eFeAJChrU6:APA91bF7OtzoI901mKnEYC2dhq1s2-rOW0IbkkV5j1NzANBQfJ927u4jPXIDaJ9p6UW5W1jk5bW4Ex_h05NTiUDAYhL65Q156qZRX-hieUSJbkvGoZDCdTWWR9lqC7sqc32RhcC_1TjQ"
        }
    }
    return data


def validate_otp_payload():
    data = {
        "mobile": "8788132556",
        "otp": "1234",
        "whatsapp_update_consent": 1,
        "device_details": {
            "device": "miel",
            "device_id": "26fe0069320a5836",
            "device_ip_address": "10.101.151.151",
            "xdevice_serial_number": "unknown",
            "device_model": "2201117PI",
            "device_type": "Handset",
            "device_mac_address": "",
            "device_manufacturer": "Xiaomi",
            "unique_id": "miel",
            "is_device_emulator": "false",
            "is_location_enabled": "true",
            "latitude": 19.117117117117118,
            "longitude": 72.86528623824486,
            "fcm_id": "cksa-JsqTX60eFeAJChrU6:APA91bF7OtzoI901mKnEYC2dhq1s2-rOW0IbkkV5j1NzANBQfJ927u4jPXIDaJ9p6UW5W1jk5bW4Ex_h05NTiUDAYhL65Q156qZRX-hieUSJbkvGoZDCdTWWR9lqC7sqc32RhcC_1TjQ",
            "AddID": "4892a9fb-826d-480e-9e58-b26cc04c5ffd"
        },
        "utm_source": "",
        "source": "Android",
        "mobile_otp_received": "false"
    }
    return data


def dashboard_one():
    data = {
        "device_details": {
            "device": "miel",
            "device_id": "26fe0069320a5836",
            "device_ip_address": "10.101.151.151",
            "xdevice_serial_number": "unknown",
            "device_model": "2201117PI",
            "device_type": "Handset",
            "device_mac_address": "",
            "device_manufacturer": "Xiaomi",
            "unique_id": "miel",
            "is_device_emulator": "false",
            "is_location_enabled": "true",
            "latitude": 19.117117117117118,
            "longitude": 72.86528623824486,
            "fcm_id": "cksa-JsqTX60eFeAJChrU6:APA91bF7OtzoI901mKnEYC2dhq1s2-rOW0IbkkV5j1NzANBQfJ927u4jPXIDaJ9p6UW5W1jk5bW4Ex_h05NTiUDAYhL65Q156qZRX-hieUSJbkvGoZDCdTWWR9lqC7sqc32RhcC_1TjQ",
            "AddID": "4892a9fb-826d-480e-9e58-b26cc04c5ffd"
        },
        "app_version": "4.8",
        "source": "android"
    }
    return data


def submmit_name():
    data = {
        "first_name": "Abhilash",
        "last_name": "Girkar",
        "ref_code": "",
        "app_language_id": 1
    }
    return data


def check_employee_details(company_name):
    data = {
        "company_name": company_name,
        "employee_code": None
    }
    return data


def submit_employee_details(employer_id, company_name):
    data = {
        "employment_type_id": 1,
        "user_type": "B2B",
        "employer_id": employer_id,
        "company_name": company_name,
        "employee_code": ""
    }
    return data


def dashboard_two():
    data = {
        "device_details": {
            "device": "miel",
            "device_id": "26fe0069320a5836",
            "device_ip_address": "10.101.151.151",
            "xdevice_serial_number": "unknown",
            "device_model": "2201117PI",
            "device_type": "Handset",
            "device_mac_address": "",
            "device_manufacturer": "Xiaomi",
            "unique_id": "miel",
            "is_device_emulator": "false",
            "is_location_enabled": "true",
            "latitude": 19.117117117117118,
            "longitude": 72.86528623824486,
            "fcm_id": "cksa-JsqTX60eFeAJChrU6:APA91bF7OtzoI901mKnEYC2dhq1s2-rOW0IbkkV5j1NzANBQfJ927u4jPXIDaJ9p6UW5W1jk5bW4Ex_h05NTiUDAYhL65Q156qZRX-hieUSJbkvGoZDCdTWWR9lqC7sqc32RhcC_1TjQ",
            "AddID": "4892a9fb-826d-480e-9e58-b26cc04c5ffd"
        },
        "app_version": "4.8",
        "source": "android"
    }
    return data


def create_loan_appliaction():
    data = {
        "application_type": "card",
        "device_details": {
            "device": "miel",
            "device_id": "26fe0069320a5836",
            "device_ip_address": "10.101.151.151",
            "xdevice_serial_number": "unknown",
            "device_model": "2201117PI",
            "device_type": "Handset",
            "device_mac_address": "",
            "device_manufacturer": "Xiaomi",
            "unique_id": "miel",
            "is_device_emulator": "false",
            "is_location_enabled": "true",
            "latitude": 19.117117117117118,
            "longitude": 72.86528623824486,
            "fcm_id": "cksa-JsqTX60eFeAJChrU6:APA91bF7OtzoI901mKnEYC2dhq1s2-rOW0IbkkV5j1NzANBQfJ927u4jPXIDaJ9p6UW5W1jk5bW4Ex_h05NTiUDAYhL65Q156qZRX-hieUSJbkvGoZDCdTWWR9lqC7sqc32RhcC_1TjQ"
        }
    }
    return data


def pan_validation(application_id):
    data = {
        "document_type": "PAN",
        "id_number": "BXZPG2865A",
        "application": "%s" % application_id,
        "dob": "09-10-1997",
        "latitude": 19.117117117117118,
        "longitude": 72.86528623824486
    }
    return data


def record_app_log(user_id):
    data = {
        "Event": "PAN_DONE",
        "User": "%s" % user_id,
        "RedirectedTo": "AADHAAR_PAGE",
        "DocumentType": "NSDL",
        "ApplicationType": "CREDIT",
        "Source": "Android"
    }
    return data


def aadhaar_ocr(application_id):
    data = {"application": "%s" % application_id,
            "document_type": "AADHAR",
            "skip_pan_step": "0"
            }
    return data


def income_page(application_id):
    data = {
        "model": "UserIncomeDetail",
        "user_entered_amount": "65000",
        "residence_type": 1,
        "application": "%s" % application_id,
        "edit": False
    }
    return data


def fetch_offer_proposed(application_id):
    data = {
        "application": int(application_id)
    }
    return data


def offer_accept(offer_prop_id):
    data = {
        "source": "LMS",
        "datapoint": "accept_offer",
        "endpoint": "%s" % offer_prop_id
    }
    return data


def nominee_details(application_id):
    data = {
        "references": [
            {
                "application": application_id,
                "name": "Deepak",
                "mobile": "8788132554",
                "relationship": "Father"
            }
        ]
    }

    return data


def save_address(city, pincode):
    data = {
        "address_1": "Test",
        "address_2": "Test",
        "city": "%s" % city,
        "pincode": "%s" % pincode,
        "state": "MAHARASHTRA",
        "latitude": 19.117117117117118,
        "longitude": 72.86528623824486,
        "confirm_address": True
    }
    return data
