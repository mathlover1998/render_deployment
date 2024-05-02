from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    GENDER = (("male", "Male"), ("female", "Female"), ("other", "Other"))
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(
        max_length=20, choices=GENDER, default="other", null=False
    )

    class Meta:
        managed = True
        db_table = "Profiles"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        