from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse
from lp17teens.util import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericRelation
from six import python_2_unicode_compatible
from hitcount.models import HitCountMixin, HitCount

# Create your models here.

@python_2_unicode_compatible   
class VidStream(models.Model):
    streamer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length = 250,blank=True,null=True)
    description = models.TextField(max_length=600)
    upload_date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='')
    hit_count_generic = GenericRelation(HitCount,object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    def __str__(self):
    	return self.title 
    def get_absolute_url(self):
    	return reverse("video-detail", kwargs={"pk": self.pk})

@receiver(pre_save, sender=VidStream)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)
# Create your models here.
