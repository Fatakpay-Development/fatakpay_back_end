import base64
import requests
import json


def post_req(url, payload, headers):
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def get_req(url, headers):
    response = requests.get(url, headers=headers)
    return response.json()


def file_upload(file_path):
    with open(file_path, "rb") as file:
        pdf_data = file.read()
    base64_encoded_pdf = base64.b64encode(pdf_data).decode('utf-8')
    return base64_encoded_pdf


def post_ocr(url, payload, files_aadhaar, header):
    response = requests.post(url, data=payload, files=files_aadhaar, headers=header)
    return response.json()


def selfie_upload(url, payload, file, header):
    response = requests.put(url, data=payload, files=file, headers=header)
    return response.json()


def put_req(url, payload, header):
    response = requests.put(url, json=payload, headers=header)
    return response.json()
