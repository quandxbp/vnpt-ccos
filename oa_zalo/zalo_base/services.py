import requests
from .credentials import ZALO_CRE
from .models import ZaloUser
from .zalo_sdk import ZaloSDK
from .automation import regist_phone_package
# 895596865423073839
class ZaloService:

    def __init__(self):
        self.z_sdk = ZaloSDK(ZALO_CRE['access_token'])
        self.title = "Dịch vụ đăng ký gói cước tự động"
        self.image_url = "https://i.imgur.com/aydbpqZ.png"
    
    def store_user_info(self, user_id, **info):
        is_existed = ZaloUser.objects.filter(user_id=user_id).exists()
        if not is_existed:
            new_user = ZaloUser(
                user_id = user_id, 
                name = info.get('name', False),
                phone = info.get('phone', False),
                city = info.get('city', False),
                district = info.get('district', False),
                address = info.get('address', False),
                ward = info.get('ward', False),
                )
            new_user.save()
        else:
            existed_user = ZaloUser.objects.get(user_id=user_id)
            existed_user.name = info.get('name', False)
            existed_user.phone = info.get('phone', False)
            existed_user.city = info.get('city', False)
            existed_user.district = info.get('district', False)
            existed_user.address = info.get('address', False)
            existed_user.ward = info.get('ward', False)

            existed_user.save()
        return {
            'success': 1,
            'message': "Success",
            'zalo_user_id': user_id,
        }
    
    def regist_phone(self, user_id, message):
        
        splitted_terms = message.split('-')
        try:
            phone = splitted_terms[1]
            package = splitted_terms[2]

            result = regist_phone_package(phone, package)
            if result:
                message = f"""Đăng ký thành công cho số điện thoại {phone} với gói cước {package}"""
            else:
                message = f"""Đăng ký không thành công, hệ thống chưa được kích hoạt, liên hệ với phòng bán hàng để được hỗ trợ!"""
            return self.z_sdk.post_message(user_id, message=message)
        except Exception as error:
            message = """Đăng ký gói cước không thành công, cú pháp đăng ký là #dangky-{số điện thoại}-{tên gói cước}
Ví dụ: #dangky-0835401499-VD149"""
            return self.z_sdk.post_message(user_id, message=message)
    
    def action_by_event(self, event_name, datas):
        if event_name == 'follow':
            user_id = datas['follower']['id']
            self.store_user_info(user_id)
            return self.z_sdk.request_user_info(
                user_id = user_id,
                title = self.title,
                image_url=self.image_url
                )
        if event_name == "user_submit_info":
            user_id = datas['sender']['id']
            info = datas['info']
            self.store_user_info(user_id, **info)
            message = f"""Cảm ơn anh/chị {datas['info'].get('name', "Chưa xác định")}-{datas['info'].get('phone', "Chưa xác định")} đã cung cấp thông tin"""
            return self.z_sdk.post_message(user_id, message=message)

        if event_name == "user_send_text":
            user_id = datas['sender']['id']
            message = datas['message']['text']
            if "#dangky" in message:
                return self.regist_phone(user_id, message)


    