from django.db import models

# Create your models here.


class Owner(models.Model):
    owner_name = models.CharField(max_length=45)
    owner_email = models.CharField(max_length=300)
    owner_age = models.IntegerField()

    class Meta:
        db_table = "owner"


class Dogs(models.Model):
    dog_name = models.CharField(max_length=45)
    dog_age = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    class Meta:
        db_table = "dogs"