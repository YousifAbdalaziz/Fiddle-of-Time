from django.db import models
from django.contrib import auth

# Create your models here.
class Publisher(models.Model):

    name = models.CharField(max_length=50, help_text='The name of the publisher')
    website = models.URLField(help_text="The publisher's website" )
    email = models.EmailField(help_text="The publisher's email adress")

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=70, help_text='title of the book')
    publication_date = models.DateTimeField(max_length = 20, help_text='Date the book was published')
    isbn = models.CharField(max_length=20, verbose_name='ISBN number of the book')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributor= models.ManyToManyField('Contributor', through='BookContributor')

    def __str__(self):
        return self.title

class Contributor(models.Model):

    first_name = models.CharField(max_length=50, help_text="the contributor's first name")
    last_name  = models.CharField(max_length=50, help_text="The contributors last name")
    email = models.EmailField(help_text='the contact email for the contributor')

    def __str__(self):
        return self.first_name




class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHER = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co_author'
        EDITOR = 'EDITOR', 'Editor'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name='The role the contributor had in this book', choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    content = models.TextField(help_text='The Review Text')
    rating = models.IntegerField(help_text='the rating the reviewer has given')
    date_created = models.DateTimeField(auto_now_add=True, help_text='the date and time the review has been created')
    date_edited = models.DateTimeField(null = True, help_text='The date and time the review was last edited')
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text='the book that this review is for')
