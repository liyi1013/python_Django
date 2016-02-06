from article.models import Article

# Article.objects.create(title='Hello World', category='Python', content='Let us add a database item')

print Article.objects.all()[0]