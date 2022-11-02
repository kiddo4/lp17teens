from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField
from lp17teens.util import unique_slug_generator
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from six import python_2_unicode_compatible

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
    	return self.name
		
    def get_absolute_url(self):
        return reverse('home')

@python_2_unicode_compatible    
class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length = 250, blank=True,null=True)
	image = models.ImageField(default='default.jpg', upload_to='Blog-image')
	Body = RichTextUploadingField(blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('Category', related_name='posts')
	hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

	class Meta:
	   ordering = ('-created_on',)
	def __str__(self):
		return self.title
	
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=60)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
     
     
class Socialmediahandle(models.Model):
	Whatsapp = models.URLField(blank=True,null=True)
	Instagram = models.URLField(blank=True,null=True)
	Facebook = models.URLField(blank=True,null=True)

    
	
@receiver(pre_save, sender=Post)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)
		

# Create your models here.
