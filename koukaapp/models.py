from django.db import models

# Create your models here.
class BlogContent(models.Model):
    CATEGORY = (("mob","MOB"),
                ("weapon","武器"),
                ("config","設定"),
                ("world","世界"),
                ("useful","便利"),
                )
    ICON = (("mob-icon","MOB型"),
            ("weapon-icon","武器型"),
            ("config-icon","設定型"),
            ("world-icon","世界型"),
            ("useful-icon","便利型"),
            )
    title = models.CharField(
        verbose_name="MOD名",
        max_length=150
        )
    content = models.TextField(
        verbose_name="紹介文",
        )
    link = models.CharField(
        verbose_name="リンク",
        max_length=150
        )
    posted_at = models.DateTimeField(
        verbose_name="投稿日時",
        auto_now_add=True
        )
    category = models.CharField(
        verbose_name="カテゴリ",
        max_length=50,
        choices=CATEGORY
        )
    icon = models.CharField(
        verbose_name="アイコンの種類",
        max_length=50,
        choices=ICON,
        default="世界型",
        )
    img_key = models.CharField(
        verbose_name="挿入画像のキー",
        default="noimage.png",
        )
    
    def __str__(self):
        return self.title