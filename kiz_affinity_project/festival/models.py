from django.db import models
import uuid
# Create your models here.
class Participant(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    quiz_type = models.CharField(max_length=10)  # "quiz1" ou "quiz2"
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class DiscountCode(models.Model):
    code = models.CharField(max_length=10, unique=True, default=uuid.uuid4().hex[:10].upper())
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)


