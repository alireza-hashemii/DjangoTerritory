# Generated by Django 4.1.7 on 2023-04-16 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_category_blog_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"verbose_name": "مقاله", "verbose_name_plural": "مقالات"},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["-position"],
                "verbose_name": "دسته بندی",
                "verbose_name_plural": "دسته بندی ها",
            },
        ),
        migrations.AlterField(
            model_name="blog",
            name="category",
            field=models.ManyToManyField(related_name="blogs", to="blog.category"),
        ),
    ]