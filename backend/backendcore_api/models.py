
from django.db.models import Avg
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)  # Open image

        # resize image
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)  # Resize image
            # Save it again and override the larger image
            img.save(self.image.path)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(UserInfo, self).save(*args, **kwargs)


# class RatingInfo(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     CurrentRating = models.ImageField(
#         default='rating-0.png', upload_to='rating')

#     def __str__(self):
#         return self.user.username


class Post(models.Model):
    header = models.CharField(max_length=100, default="Header")
    text = models.TextField()

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.header}: {self.average_rating()}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.header}: {self.rating}"
