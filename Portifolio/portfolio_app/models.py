from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=100)
    overview = models.TextField(max_length=500, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    challenges = models.TextField(max_length=500, blank=True, null=True)
    achievements = models.TextField(max_length=500, blank=True, null=True)
    featured_img = models.ImageField(blank=True, null=True)
    alt_text = models.CharField(max_length=100, blank=True, null=True)
    filter_class = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-date_created']

    def get_absolute_url(self):
        return reverse('portfolio_app:detail', kwargs={'pk': str(self.pk)})

    @property
    def imageURL(self):
        try:
            url = self.featured_img.url

        except:
            url = ''

        print('URL:' + '  ' + url)

        return url

    def __str__(self):
        return self.name


class Image(models.Model):
    project_name = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image_name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField()
    alt_text = models.CharField(max_length=100, blank=True, null=True)

    # def __str__(self):
    #     return self.image_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
            print('URL:' + '  ' + url)
        except:
            url = ''
        return url
