from django.db import models
from core import models as core_models

# Create your models here.
class Conversation(core_models.TimeStampedModel):

  """ Conversation Model Definition """
  # 대화방
  participants = models.ManyToManyField("users.User", blank=True)
  
  def __str__(self):
    return str(self.created)


class Message(core_models.TimeStampedModel):

  """ Message Model Definition """
  # 한 개의 메세지
  message = models.TextField()
  user = models.ForeignKey("users.User", on_delete=models.CASCADE)
  conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.user} says: {self.text}"

