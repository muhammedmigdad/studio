from django.db import models


EVENT_TYPE_CHOICES = [
    ('Wedding', 'Wedding'),
    ('Baby Birthday', 'Baby Birthday'),
    ('Model Shoot', 'Model Shoot'),
    ('Nikah Photography', 'Nikah Photography'),
    ('Engagement', 'Engagement'),
    ('Portrait', 'Portrait'),
]

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services')
    
    
    
    class meta:
        db_table = "service"
        verbose_name = "service"
        verbose_name_plural = "services"
        ordering = ['-id']
    

    def __str__(self):
        return self.title
    
    

class WeddingPhotography(models.Model):
    image = models.ImageField(upload_to='wedding_photos')
    
    class meta:
        db_table = "wedding_photography"
        verbose_name = "wedding_photography"
        verbose_name_plural = "wedding_photographys"
        ordering = ['-id']
    
    def __str__(self):
        return self.image.name
    
class Filims(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='wedding_photos')
    videolink = models.URLField(max_length=200)
    
    class meta:
        db_table = "filim"
        verbose_name = "filim"
        verbose_name_plural = "filims"
        ordering = ['-id']
    
    def __str__(self):
        return self.image.name
    
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='portfolio_images')
    
    class meta:
        db_table = "portfolio"
        verbose_name = "portfolio"
        verbose_name_plural = "portfolios"
        ordering = ['-id']


    def __str__(self):
        return self.title
    
    
class GelleryPortfolio(models.Model):
    image = models.ImageField(upload_to='portfolio_images')
    
    class meta:
        db_table = "gellery"
        verbose_name = "gellery"
        verbose_name_plural = "gellerys"
        ordering = ['-id']


    def __str__(self):
        return self.image.name
    
    
class Enquiry(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    enquiry_number = models.BigIntegerField()
    location_of_shoot = models.CharField(max_length=255)
    event_date = models.DateField()
    event_address_details = models.TextField()
    event_type = models.CharField(max_length=255, choices=EVENT_TYPE_CHOICES)
    
    class meta:
        db_table = "enquiry"
        verbose_name = "enquiry"
        verbose_name_plural = "enquirys"
        ordering = ['-id']


    def __str__(self):
        return self.full_name
    
    
class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.BigIntegerField()
    location_of_shoot = models.CharField(max_length=255)
    event_date = models.DateField()
    event_address_details = models.TextField()
    event_type = models.CharField(max_length=255, choices=EVENT_TYPE_CHOICES)
    
    class meta:
        db_table = "contact"
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        ordering = ['-id']

    def __str__(self):
        return self.full_name
    
    


    
    
    




