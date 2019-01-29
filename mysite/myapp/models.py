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

#------------------------------------------------------------------------------------------------------------------------------------------

class Skillset(models.Model):
    skill_category = models.CharField(max_length = 25)

    def __str__(self):
        return (self.skill_category)

class Skills(models.Model):
    skillset = models.ForeignKey(Skillset
    , related_name='skill_list', on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

    def __str__(self):
        return (self.skill)

#----------------------------------------------------------------------------------------------------------------------------

class Recommendations(models.Model):
    name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    recommendation = models.CharField(max_length=500)

    def __str__(self):
        return (self.name)

#---------------------------------------------------------------------------------------------------------------------------

class Contact(models.Model):
    contact_img = models.ImageField(upload_to='myapp/static/')
    email = models.EmailField()
    phone_no = models.CharField(max_length=20)
    linkedin = models.URLField()

    def __str__(self):
        return (self.email)

#------------------------------------------------------------------------------------------------------------------------------

class Home(models.Model):
    wel_message = models.CharField(max_length=50)

    def __str__(self):
        return (self.wel_message)

class HomeImage(models.Model):
    images = models.ForeignKey(Home, related_name='img_list', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='myapp/static/')

    def __str__(self):
        return (self.img.url)

class Paragraph(models.Model):
    paragraph = models.ForeignKey(Home, related_name='para_list', on_delete=models.CASCADE)
    intro_text = models.TextField()

    def __str__(self):
        return (self.intro_text)
