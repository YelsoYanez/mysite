from django.db import models

# Create your models here.

# TODO: Read django on forms for validation
class Business(models.Model):
    business_type = models.CharField(max_length=200)
    businees_name = models.CharField(max_length=200)
    business_address = models.CharField(max_length=200)
    businees_telephone = models.CharField(max_length=11)
    businees_fax = models.CharField(max_length=11)
    businees_email = models.CharField(max_length=200)


# TODO: Adjust the max length of the char fields
class BusinessResponse(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_response = models.CharField(max_length=200)


class UserComments(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    comment_reviewer = models.CharField(max_length=30)
    comment_publish_date = models.DateTimeField('date published')
    comment_text = models.CharField(max_length=250)