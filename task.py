import requests, json

token = {}

request_login = {"mobile": "8788132556", "email_notify": "", "email": "", "device_details": {"device": "miel", "device_id": "26fe0069320a5836", "device_ip_address": "192.168.1.9", "xdevice_serial_number": "unknown", "device_model": "2201117PI", "device_type": "Handset", "device_mac_address": "", "device_manufacturer": "Xiaomi", "unique_id": "miel", "is_device_emulator": "false", "is_location_enabled": "true", "latitude": 19.117117117117118, "longitude": 72.86528623824486, "fcm_id": "cksa-JsqTX60eFeAJChrU6:APA91bF7OtzoI901mKnEYC2dhq1s2-rOW0IbkkV5j1NzANBQfJ927u4jPXIDaJ9p6UW5W1jk5bW4Ex_h05NTiUDAYhL65Q156qZRX-hieUSJbkvGoZDCdTWWR9lqC7sqc32RhcC_1TjQ", "AddID": "4892a9fb-826d-480e-9e58-b26cc04c5ffd"}}
methode = "POST"
login = "https://devonboardingapi.fatakpay.com/user/send-otp/"
otp = "https://devonboardingapi.fatakpay.com/user/super-app/validate-otp"
superdashboard = "https://devonboardingapi.fatakpay.com/user/verify-user-superdashboard"

respose_login = requests.post(login, json=request_login,)
print("respose_login*****", respose_login.json())

request_otp = {"mobile": "8788132556", "otp": "1234", "whatsapp_update_consent": 1, "device_details": {"device": "miel", "device_id": "26fe0069320a5836", "device_ip_address": "192.168.1.9", "xdevice_serial_number": "unknown", "device_model": "2201117PI", "device_type": "Handset", "device_mac_address": "", "device_manufacturer": "Xiaomi", "unique_id": "miel", "is_device_emulator": "false", "is_location_enabled": "true", "latitude": 19.117117117117118, "longitude": 72.86528623824486, "fcm_id": "cksa-JsqTX60eFeAJChrU6:APA91bF7OtzoI901mKnEYC2dhq1s2-rOW0IbkkV5j1NzANBQfJ927u4jPXIDaJ9p6UW5W1jk5bW4Ex_h05NTiUDAYhL65Q156qZRX-hieUSJbkvGoZDCdTWWR9lqC7sqc32RhcC_1TjQ", "AddID": "4892a9fb-826d-480e-9e58-b26cc04c5ffd"}, "utm_source": "", "source": "Android", "mobile_otp_received": "false"}
respose_otp = requests.post(otp, json=request_otp,)
print("request_otp#####", respose_otp.json())

dic = respose_otp.json()
token['token'] = dic['data']['token']

request_superdasboard = {"device_details": {"device": "miel", "device_id": "26fe0069320a5836", "device_ip_address": "192.168.1.9", "xdevice_serial_number": "unknown", "device_model": "2201117PI", "device_type": "Handset", "device_mac_address": "", "device_manufacturer": "Xiaomi", "unique_id": "miel", "is_device_emulator": "false", "is_location_enabled": "true", "latitude": 19.117117117117118, "longitude": 72.86528623824486, "fcm_id": "cksa-JsqTX60eFeAJChrU6:APA91bF7OtzoI901mKnEYC2dhq1s2-rOW0IbkkV5j1NzANBQfJ927u4jPXIDaJ9p6UW5W1jk5bW4Ex_h05NTiUDAYhL65Q156qZRX-hieUSJbkvGoZDCdTWWR9lqC7sqc32RhcC_1TjQ", "AddID": "4892a9fb-826d-480e-9e58-b26cc04c5ffd"}, "app_version": "4.8", "source": "android"}
respose_dashboard = requests.post(superdashboard, json=request_superdasboard,)
print("respose_dashboard$$$$$", respose_dashboard.json())
