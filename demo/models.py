from django.db import models

# Create your models here.
class Post(models.Model):
	post_id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length = 200)
	desc = models.TextField()
	

	def __unicode__(self):
	 	return self.title

class Story(models.Model):
	postTitle = models.ForeignKey(Post)
	storyTitle = models.CharField(max_length = 200)
	storyDesc = models.CharField(max_length = 200)
	
	def __unicode__(self):
	 	return self.storyTitle