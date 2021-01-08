from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

  """ Time Stamped Model """

  created = models.DateTimeField(auto_now_add=True) 
  # 모델이 생성된 날짜를 써줌
  updated = models.DateTimeField(auto_now=True) 
  # 새로운 날짜로 업데이트

  # 위 필드들이 데이터베이스로 가기 원하지 않음
  # 이 모델을 쓰는 다른 모델이 데이터베이스에 가야함 => abstract model: 확장을 위한 추상모델
  class Meta:
    abstract = True