from django.db import models

class Person(models.Model):
    person_name = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=16)
    age = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    post_code = models.CharField(max_length=12)
    full_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.person_name
