from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=25)
	def __str__(self):
		return "{}".format(self.name)
    
class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70, unique_for_date='published', null=True)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    featured = models.Boolean(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    def __str__(self):
        return '{} published on {}' .format(self.title, self.published.strftime("%d %B, %Y"))

#class Comment(models.Model):
 #   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  #  body = models.TextField()
   # posted = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    #def __str__(self):
     #   return "comment by {} on {}".format(self.author, self.post.title)

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    body = models.TextField()
    active = models.BooleanField(default=True)
    published = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return "comment by {} on {}".format(self.author, self.post)