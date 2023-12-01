from django.db import models
from django.db import models
import uuid
from django.contrib.auth.models import User


class BaseModel(models.Model):
    uuid =models.UUIDField(default=uuid.uuid4 , editable=False , primary_key=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Todo(BaseModel):
    todo_name=models.CharField(max_length=100)
    todo_description=models.CharField(max_length=134321)
    is_completed = models.BooleanField(default=False)
    todo_date=models.DateField()
    user=models.ForeignKey(User , on_delete=models.CASCADE , related_name="user_todo")
