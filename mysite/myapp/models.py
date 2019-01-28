from django.db import models

# Create your models here.

class Experience(models.Model):
    company = models.CharField(max_length = 30)
    role = models.CharField(max_length = 25)
    from_date = models.DateField()  
    #Constraint should be added to from_date to not choose a future date
    to_date = models.DateField()
    #Constraint should be added to to_date to not choose a future date
    current_company = models.BooleanField()

    def __str__(self):
        return (self.role)
        
    
class Responsibility(models.Model):
    exp = models.ForeignKey(Experience, related_name='res_list', on_delete = models.CASCADE)
    res = models.CharField(max_length = 50)

    def __str__(self):
        return (self.res)