from django.db import models

# Create your models here.
class coronaTelangana(models.Model):
    date=models.CharField(max_length=200)
    positiveCases = models.CharField(max_length=200)
    negativeCases = models.CharField(max_length=200)
    deaths = models.CharField(max_length=200)
    caseFatalityRate= models.CharField(max_length=200)
    recoveryRate = models.CharField(max_length=200)
    homeIsolation =models.CharField(max_length=200)
    samplesTested=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.date
class coronaDist(models.Model):
    date=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    positiveCases = models.CharField(max_length=200)
    def __str__(self):
        return self.district + self.date
        
class coronaLab(models.Model):
    type=models.CharField(max_length=200)
    centers=models.CharField(max_length=2000)
    def __str__(self):
        return self.type
class coronaRapid(models.Model):
    
    district=models.CharField(max_length=200)
    centers = models.CharField(max_length=2000)
    def __str__(self):
        return self.district 
class coronaCenter(models.Model):
    
    district=models.CharField(max_length=200)
    centers = models.CharField(max_length=2000)
    def __str__(self):
        return self.district 