from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, Model, DateField, TextField, CASCADE, IntegerField


class UserAll(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = DateField(null=False)
    country = TextField(null=True)
    city = TextField(null=True)
    email_confirm = TextField(null=True, max_length=100)
    # like

    def __str__(self):
        return '<User user={} birthday={} country={} city={} >'.format(self.user, self.birthday, self.country, self.city)


class Post(Model):
    title = TextField(max_length=40, null=True)
    img = TextField(null=True)
    body = TextField(null=True, max_length=300)
    country = TextField(null=True)
    city = TextField(null=True)
    # like
    # comments

    def __str__(self):
        return '<User title={} img={} body={} country={} city={} >'.format(self.title, self.img, self.body, self.country, self.city)


class Comments(Model):
    post = ForeignKey('Post', on_delete=CASCADE, related_name='comments')
    body = TextField(null=True, max_length=100)

    def __str__(self):
        return '<User post={} body={}>'.format(self.post, self.body)


class Like(Model):
    post = ForeignKey('Post', on_delete=CASCADE, related_name='like')
    user = ForeignKey(User, on_delete=CASCADE, related_name='like')
    like = IntegerField(null=True)

    def __str__(self):
        return '<User user={} liks={} >'.format(self.user, self.like)