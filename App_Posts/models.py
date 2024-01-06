from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField(max_length=264, blank=True)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-uploaded_date']


class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='Liked_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}:{}'.format(self.user, self.post)
