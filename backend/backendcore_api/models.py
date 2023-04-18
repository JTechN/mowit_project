
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    rating = models.ImageField(default='rating-0.png', upload_to='rating')

    def __str__(self):
        return self.user.username

    # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)  # Open image
        rtg = Image.open(self.rating.path)

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            # Save it again and override the larger image
            img.save(self.image.path)
        if rtg.height > 300 or rtg.width > 300:
            output_size = (300, 300)
            rtg.thumbnail(output_size)  # Resize image
            rtg.save(self.image.path)

################
