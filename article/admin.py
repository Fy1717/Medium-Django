from django.contrib import admin
from .models import Article


# Register your models here.
# Admin panelinde kullanacaklarımızı burda tanımladık
@admin.register(Article) #decorater  kullanarak oluşturdum
class ArticleAdmin(admin.ModelAdmin): #admin panelini özelleştirmek için bu şekilde yazıyorum
    list_display = ["title", "author", "created_date"] #başlıkta hangi verilerin görüneceğini belirttim
    list_display_links = ["title", "created_date"] #alanlar için link özelliği ekledik
    search_fields = ["title", "content"] #sayfanın üzerinde title ve contente göre bir search alanı oluşturur
    list_filter = ["created_date", "author"] #sayfanın yanında tarihe göre bir filter alanı gösterir

    class Meta:
        model = Article
