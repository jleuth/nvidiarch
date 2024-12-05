from django.db import models

# Create your models here.

class Rating(models.Model):
    driver = models.CharField(
        max_length=20, 
        verbose_name='Driver ID', 
        help_text='Unique identifier for the driver'
    )
    name = models.CharField(
        max_length=50, 
        default='Anonymous', 
        verbose_name='Reviewer Name', 
        help_text='Name of the person giving the rating'
    )
    rating = models.IntegerField(
        default=0, 
        verbose_name='Rating Score', 
        help_text='Rating score from 0 to 5'
    )
    comment = models.TextField(
        verbose_name='Comment', 
        help_text='Detailed comment about the driver'
    )
    date = models.DateField(
        verbose_name='Date of Rating', 
        help_text='Date when the rating was given'
    )

    distro = models.CharField(
        max_length=50, 
        verbose_name='Linux Distro', 
        help_text='Linux distribution used by the reviewer', 
        default=''
    )

    email = models.EmailField( 
        verbose_name='Email', 
        help_text='Add your email if you want to be notified of new driver releases, so you can update and rate the new driver',
        default=''
    )

    class Meta:
        verbose_name = 'Driver Rating'
        verbose_name_plural = 'Driver Ratings'
        ordering = ['-date']

    def __str__(self):
        return f'{self.name} rated {self.driver} with {self.rating} stars'