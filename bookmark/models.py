from django.db import models
from django.urls import reverse

# Create your models here.
# 모델 : 데이터베이스를 sql없이 다루려고 모델을 사용한다.
# 우리가 데이터를 객체화해서 다루겠다.
# 모델 = 테이블
# 모델의 필드(변수) = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값

class Bookmark(models.Model): # class 사용, 앞글자는 대문자로
    site_name = models.CharField(max_length=100) # 글자 100글자까지 저장할래
    url = models.URLField('Site URL') # url을 사이트 이름으로 할게
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류 : 글자/숫자
    # 2. 제약 사항 (몇 글자까지?)
    # 3. 폼의 종류
    # 4. 폼에서 제약 사항

    def __str__(self): # 어드민에 등록한 이름 형식 설정
        return "이름 : "+self.site_name+", 주소 : "+self.url

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])





















## => 모델은 데이터 베이스 :
## 모델을 만들었다 => DB에 어떤 데이터를 어떤 형태로 넣을지 결정 !
## makemigrateions => 모델의 변경사항을 추적해서 기록
## 마이그레이션(migrate) => db에 모델의 내용을 반영(테이블 생성)
