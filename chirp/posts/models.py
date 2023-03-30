from django.db import models
from django.urls import reverse
from users.models import Profile

class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,)
    body = models.TextField(max_length=1000)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    # avatar = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.pk,))

    class Meta:
        ordering = ['-created']
