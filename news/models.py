from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_articles')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    Model representing a comment made by a user on a news article.
    Attributes:
        news (ForeignKey): A reference to the News model instance. This field connects the comment to the specific news article it relates to.
                             The 'related_name' attribute ('comments') provides an easy reverse lookup from a News instance to all its associated comments.
        user (ForeignKey): A reference to the User model instance representing the author of the comment.
                             The 'related_name' attribute ('comments') facilitates reverse querying to list all comments created by the user.
        content (TextField): Contains the textual content of the comment. A TextField is chosen to handle large amounts of text without a maximum length constraint.
        created_at (DateTimeField): Records the date and time when the comment was created.
                                    The 'auto_now_add=True' parameter ensures that this timestamp is automatically set to the current date and time upon creation.
    Methods:
        __str__():
            Provides a human-readable string representation of the Comment instance.
            This method returns a formatted string that indicates the comment's author and the associated news article, enhancing readability in contexts like the Django Admin interface.
    """
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.news}'