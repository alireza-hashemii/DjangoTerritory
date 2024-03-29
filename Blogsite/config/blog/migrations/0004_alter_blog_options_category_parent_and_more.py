# Generated by Django 4.1.7 on 2023-05-05 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blog_options_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "ordering": ["-publish"],
                "verbose_name": "مقاله",
                "verbose_name_plural": "مقالات",
            },
        ),
        migrations.AddField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="children",
                to="blog.category",
                verbose_name="زیردسته",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="is_active",
            field=models.BooleanField(verbose_name="دسته بندی فعال باشد ؟"),
        ),
        migrations.AlterField(
            model_name="category",
            name="position",
            field=models.IntegerField(verbose_name="جایگاه دسته بندی"),
        ),
        migrations.AlterField(
            model_name="category",
            name="publish",
            field=models.DateTimeField(auto_now=True, verbose_name="تاریخ"),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(verbose_name="نشانی دسته بندی"),
        ),
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=50, verbose_name="عنوان دسته بندی"),
        ),
    ]
