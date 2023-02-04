from django.db import models
from .category import Category
from .localisation import Localisation
from .type import Type
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Annonce(models.Model):
    titre_Annonce = models.CharField(max_length=300)
    type_Annonce = models.ForeignKey(Type,on_delete=models.CASCADE )
    category_Annonce= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    surface_Annonce = models.IntegerField(null = True)
    description_Annonce = models.CharField(max_length=250, default='', blank=True, null= True)
    prix_Annonce = models.FloatField(null=True)
    date_Annonce = models.DateTimeField(default=timezone.now)
    #images_Annonce= models.ImageField(upload_to='uploads/')
    localisation_Annonce = models.ForeignKey(Localisation, on_delete=models.CASCADE,default= 1)
    
    def __str__(self):
        return self.titre_Annonce

    
    @staticmethod
    def get_annonces_by_id(ids):
        return Annonce.objects.filter (id__in=ids)
    @staticmethod
    def get_all_annonce():
        return Annonce.objects.all()

    @staticmethod
    def get_all_annonces_by_categoryid(category_id):
        if category_id:
            return Annonce.objects.filter (category_Annonce =category_id)
        else:
            return Annonce.get_all_annonce()
    @staticmethod
    def get_all_annonces_by_typeid(type_id):
        if category_id:
            return Annonce.objects.filter (type_Annonce =type_id)
        else:
            return Annonce.get_all_annonce()
    @staticmethod
    def get_all_annonces_by_locationid(location_id):
        if category_id:
            return Annonce.objects.filter (localisation_Annonce =category_id)
        else:
            return Annonce.get_all_annonce()

#-------------------------------
def get_image_filename(instance, filename):
    title = instance.annonce_id.titre_Annonce
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  
#---------------------------------------
class Images(models.Model):
    annonce_id = models.ForeignKey(Annonce,on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')

#----------------------------------------------
class AnnonceManager (models.Model) :
    ancid = models.IntegerField(primary_key=True)
    titre_Annonce = models.CharField(max_length=300)
    type_Annonce = models.ForeignKey(Type,on_delete=models.CASCADE )
    wilaya_Annonce=models.CharField(max_length=100)
    commune_Annonce=models.CharField(max_length=100)
    periode_Annonce=models.CharField(max_length=100)
    class Meta :
        db_table = "liste_annonce"

#----------------------------------------------
class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.TextField()
    numero = models.TextField()

    def __str__(self):
        return self.user.username

#----------------------------------------------
class Offre(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.user.username
