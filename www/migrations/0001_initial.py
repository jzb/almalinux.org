# Generated by Django 3.2.3 on 2021-05-14 12:29
from typing import List

import django.core.validators
import django_quill.fields  # type: ignore
from django.db import migrations, models

import commons.uploads


class Migration(migrations.Migration):
    initial = True

    dependencies: List = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('display_name', models.CharField(help_text='Name of the backer', max_length=100)),
                ('logo', models.FileField(help_text='Logo of the backer. MUST be a zero-margin SVG file!',
                                          upload_to=commons.uploads.segmented_upload_to,
                                          validators=[django.core.validators.FileExtensionValidator(['svg'])])),
                ('url', models.URLField(help_text='URL of the backer')),
                ('priority', models.PositiveIntegerField(default=0,
                                                         help_text='Absolute priority of the backer relative to other backers. The higher the priority, the earlier the backer will appear.')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('published', models.BooleanField(default=True, help_text='Uncheck to hide')),
                ('date',
                 models.DateTimeField(help_text='Date of publication. Will be displayed to public AFTER this date.')),
                ('lang',
                 models.CharField(choices=[('en', 'English (US)'), ('es', 'Español (España)'), ('ru', 'Русский')],
                                  db_index=True, default='en', max_length=7, verbose_name='Content language')),
                ('title', models.CharField(max_length=255)),
                ('slug',
                 models.SlugField(blank=True, help_text='Optional - leave empty to set automatically from Title.',
                                  max_length=255, verbose_name='Canonical title (slug)')),
                ('excerpt',
                 models.TextField(help_text='An excerpt to display in the article list view of the blog index.')),
                ('content', django_quill.fields.QuillField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lang',
                 models.CharField(choices=[('en', 'English (US)'), ('es', 'Español (España)'), ('ru', 'Русский')],
                                  db_index=True, default='en', max_length=7, verbose_name='Content language')),
                ('priority', models.PositiveIntegerField(default=0,
                                                         help_text='Absolute priority of the question relative to other questions in the same language. The higher the priority, the earlier the question will appear.')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'FAQ entries',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('published', models.BooleanField(default=True,
                                                  help_text='Uncheck to make draft. Drafts are not visible to public.')),
                ('date',
                 models.DateTimeField(help_text='Date of publication. Will be displayed to public AFTER this date.',
                                      verbose_name='Publication date')),
                ('lang',
                 models.CharField(choices=[('en', 'English (US)'), ('es', 'Español (España)'), ('ru', 'Русский')],
                                  db_index=True, default='en', max_length=7, verbose_name='Content language')),
                ('title', models.CharField(max_length=255)),
                ('slug',
                 models.SlugField(blank=True, help_text='Optional - leave empty to set automatically from Title.',
                                  max_length=255, verbose_name='Canonical title (slug)')),
                ('content', django_quill.fields.QuillField()),
            ],
        ),
        migrations.CreateModel(
            name='PressArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('priority', models.PositiveIntegerField(default=0,
                                                         help_text='Absolute priority of the article relative to other articles. The higher the priority, the earlier the article will appear.')),
                ('publication', models.CharField(help_text='Name of the publication', max_length=255)),
                ('excerpt', models.TextField(help_text='Excerpt or quote from the article to display in the page')),
                ('url', models.URLField(help_text='URL to the news article')),
            ],
        ),
    ]