from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="наименование")
    description = models.TextField(verbose_name="описание", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="наименование")
    description = models.TextField(verbose_name="описание", null=True, blank=True)
    preview = models.ImageField(
        upload_to="previews/", verbose_name="изображение", null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        null=True,
        blank=True,
    )
    price = models.IntegerField(verbose_name="цена")
    created_at = models.DateField(verbose_name="дата создания", null=True, blank=True)
    updated_at = models.DateField(verbose_name="дата изменения", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("name",)
