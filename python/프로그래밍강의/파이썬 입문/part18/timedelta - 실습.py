"""
문제 설명
hundred_after가 지금으로부터 100일 후, 9시 정각을 값으로 가지는 datetime클래스의 인스턴스가 되도록 만들어 보세요. (단, 정각의 기준은 초 단위까지만 맞으면 됩니다.)

timedelta 클래스를 이용하여 시간 연산을 해봅시다.

addtime = datetime.timedelta(days = 10)
datetime.datetime.now() + addtime    # 10일 후
datetime.datetime.now() - addtime    # 10일 전

thedate = datetime.datetime.now().replace(hour = 10, minute=0, second = 0)
          + datetime.timedelta(days = 3)       # 3일 후 10시 정각

"""

import datetime

addtime = datetime.timedelta(days = 100)
# hundred_after = datetime.datetime.now() + addtime

hundred_after = datetime.datetime.now().replace(hour = 9, minute=0, second = 0)+ addtime
          

print("{}/{}/{}  {}:{}:{}".format(hundred_after.year,hundred_after.month, hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))



# import datetime
# addtime = datetime.timedelta(days = 100)
# hundred_after = datetime.datetime.now().replace(hour = 9,minute = 0 , second = 0) + addtime

# print("{}/{}/{} {}:{}:{}".format(hundredafter.year,hundredafter.month, hundredafter.day, hundredafter.hour, hundredafter.minute, hundredafter.second))