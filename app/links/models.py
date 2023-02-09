from django.db import models
from shortuuid.django_fields import ShortUUIDField
from accounts.models import User

# Create your models here.

class Link(models.Model):
    id = ShortUUIDField(
        length=4,
        primary_key=True,
    )
    original_url = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)