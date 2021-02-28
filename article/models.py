from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="YAZAR")
    title = models.CharField(max_length=50, verbose_name="BAŞLIK")
    content = models.TextField(verbose_name="İÇERİK") #verbose_name ile görüntülenen başlığı değiştirdik
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="OLUŞTURMA TARİHİ")

    def __str__(self):
        return self.title #article_object yerine title verisini döndürdük
