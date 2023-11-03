import os
# ACCESS KEY 요청
print("코드 발급 : https://console.kakaoicloud-kr-gov.com/settings/access-keys")
key_id = input("ApplicationID : {사용자 액세스 키 ID}를 입력하세요 : ")
key_pw = input("ApplicationSecret : {사용자 액세스 보안 키}를 입력하세요 : ")

os.system('pip install pip==18.1')

os.system('pip install ujson-5.3.0-cp311-cp311-win_amd64.whl')
os.system('pip install rasa')

# 필수 커널 패키지 다운로드
# os.system('pip install pip --upgrade')
os.system('pip install setuptools --upgrade')
os.system('pip install kiml --index-url https://pypi.ml.kakaoicloud-kr-gov.com/simple --trusted-host pypi.ml.kakaoicloud-kr-gov.com')

# 환경 변수 지정 | "HOME" 정보에 KIML 등록
os.system('setx HOME c:\kiml')

try:
    os.system('kiml login')
    os.system(key_id)
    os.system(key_pw)
except:
    pass
os.system('python -m pip install --upgrade pip')