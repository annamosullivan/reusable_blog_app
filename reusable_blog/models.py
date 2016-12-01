from django.db import models
from django.utils import timezone
from django.conf import settings

class Tag(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.slug

class Post(models.Model):
    class Meta:
        app_label="reusable_blog"

	# author is linked to a logged in user in the "auth_user" table
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0) # Record how often a post is seen
    tag = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
   

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




 #tags = models.ManyToManyField(Tag)
