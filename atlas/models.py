from django.db import models

#Import User method for django
from django.contrib.auth.models import User
'''End Of Import'''
#---------------------------------------------------------------------#


#################################################################################################################################################################################
# MODEL FOR USER!
#################################################################################################################################################################################

#...Class USER added here...
class User(models.Model):
#Attribute Variables for User class to represent different columns in database
    '''
    name-: This is the name of the User
    avatar-: A picture of the user
    '''
    name = models.OneToOneField(User, related_name='usname',on_delete=models.CASCADE)
    bio = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    contact_info = models.CharField(max_length=50)

    
    '''Method to filter database results'''
    def __str__(self):
        return self.name

#################################################################################################################################################################################
