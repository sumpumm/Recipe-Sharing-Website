from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class RecipeCategory(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    title=models.CharField(max_length=255)
    category=models.ForeignKey(RecipeCategory,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='recipe/images',default="")
    ingredients = models.TextField()
    procedure = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

