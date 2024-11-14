from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'users'

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    def __str__(self):
        return f'{self.user.name} at {self.room.name} on {self.attendance_date}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.name} commented on {self.room.name}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'comments'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.name} liked {self.comment.comment_text}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'likes'

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.name} disliked {self.comment.comment_text}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'dislikes'
    
    def delete(self, *args, **kwargs):
        raise Exception("Cannot delete a dislike")
    def save(self, *args, **kwargs):
        raise Exception("Cannot save a dislike")
    def update(self, *args, **kwargs):
        raise Exception("Cannot update a dislike")
    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return Dislike.objects.get(pk=value)
    def to_python(self, value):
        if value is None:
            return None
        return Dislike.objects.get(pk=value)
    def get_prep_value(self, value):
        if value is None:
            return None
        return value.pk


