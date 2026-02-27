from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content= models.TextField(max_length=1000)
    create_at = models.DateTimeField(default=timezone.now)
    image= models.ImageField(upload_to="post_images", blank=True, null=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})


