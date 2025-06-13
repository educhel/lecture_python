# (1)
# 오늘은 벚꽃축제 시즌!
# 카페 이벤트 메시지를 출력할 때, 모두 대문자로 출력해야 한다고 합니다.
# 아래 메시지를 모두 대문자로 변환하는 코드를 작성하세요

event_msg = "Welcome to Spring Blossom Festival!"
event_msg = event_msg.upper() # 대문자화
# event_msg = event_msg.lower() # 소문자화
# event_msg = event_msg.title() 
print(event_msg)

# (2)
# 리뷰를 확인하던 중, 어떤 손님이 오타를 내셨습니다.
# 아래 리뷰에서 'lattee'라는 잘못된 단어를 'latte'로 바꾸는 코드를 작성하세요

review = "The best lattee I have ever had."
review = review.replace('lattee','latte')
print(review)

# (3)
# 카페에서 이벤트 응모자를 공백(스페이스) 기준으로 나눈 리스트가 필요합니다.
# 응모자 명단을 리스트로 변환하세요.
applicants = "KimMinho LeeJisoo ParkSunghoon"
applicants_list = applicants.split(' ')
print(applicants_list)

# (4)
# 주문 내역에 고객 이메일이 기록되어 있습니다.
# 이메일 주소에서 아이디(골뱅이 앞부분)만 추출하는 코드를 작성하세요.
email = "cafe_guest21@blossom.com"

# 방법 1 - split을 사용하는 방법
print(email.split('@')[0])

# 방법 2 - 슬라이싱
idx = email.find("@")
print(email[:idx])