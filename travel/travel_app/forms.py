from django.forms import ModelForm
from travel_app.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'summary', 'text', 'image']
