# Generated by Django 3.0.2 on 2020-02-02 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy_books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Book Name')),
                ('pages', models.IntegerField(verbose_name='Tot. No. of Pages')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cost')),
                ('rating', models.FloatField(verbose_name='Rating of Book')),
                ('pubdate', models.DateField(verbose_name='Publication Date')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Publisher Name')),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Author Name'),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Store Name')),
                ('books', models.ManyToManyField(to='buy_books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='buy_books.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy_books.Publisher'),
        ),
    ]
