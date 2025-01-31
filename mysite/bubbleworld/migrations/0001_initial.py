# Generated by Django 3.0.6 on 2020-05-27 12:43

import bubbleworld.models
import ckeditor.fields
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.CharField(default='/static/open-iconic/png/person-3x.png', max_length=200, verbose_name='头像')),
                ('privilege', models.IntegerField(default=0, verbose_name='权限')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
                'ordering': ['-date_joined'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('type_comment', models.IntegerField(default=0)),
                ('star', bubbleworld.models.IntegerRangeField(default=3, verbose_name='评分')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
                ('like_number', models.IntegerField(default=0)),
                ('dislike_number', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('dislike_user', models.ManyToManyField(blank=True, related_name='dislike_user', to=settings.AUTH_USER_MODEL)),
                ('like_user', models.ManyToManyField(blank=True, related_name='like_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='导航')),
                ('url', models.CharField(max_length=250, verbose_name='地址')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '导航',
                'verbose_name_plural': '导航',
                'db_table': 'navigation',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('type_post', models.IntegerField(default=0)),
                ('view_times', models.IntegerField(default=0)),
                ('content_number', models.IntegerField(default=0)),
                ('upper_placed', models.BooleanField(default=False)),
                ('essence', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL)),
                ('last_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_last_responce', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '主题帖',
                'verbose_name_plural': '主题帖',
                'db_table': 'post',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PostPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
                ('type_postpart', models.IntegerField(default=0)),
                ('content_number', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postpart_author', to=settings.AUTH_USER_MODEL)),
                ('last_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postpart_last_responce', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='bubbleworld.Post')),
            ],
            options={
                'verbose_name': '间贴',
                'verbose_name_plural': '间贴',
                'db_table': 'postpart',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('author', models.CharField(default='', max_length=50, verbose_name='作者')),
                ('section_type', models.IntegerField(default=0)),
                ('director', models.CharField(default='', max_length=50, verbose_name='导演')),
                ('actor', models.CharField(default='', max_length=100, verbose_name='演员')),
                ('author_description', models.CharField(max_length=2000, verbose_name='作者描述')),
                ('description', models.CharField(max_length=2000, verbose_name='描述')),
                ('img', models.ImageField(upload_to='img/')),
                ('content_number', models.IntegerField(default=0)),
                ('star', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('admins', models.ManyToManyField(blank=True, related_name='admins', to=settings.AUTH_USER_MODEL, verbose_name='管理员')),
                ('parent_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_parent_section', to='bubbleworld.Section')),
                ('users', models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '区块',
                'verbose_name_plural': '区块',
                'db_table': 'section',
                'ordering': ['-content_number'],
            },
        ),
        migrations.CreateModel(
            name='PostPartComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_postpartcomment', models.IntegerField(default=0)),
                ('content', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postpartcomment_author', to=settings.AUTH_USER_MODEL)),
                ('postpart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postpart', to='bubbleworld.PostPart')),
            ],
            options={
                'verbose_name': '间贴评论',
                'verbose_name_plural': '间贴评论',
                'db_table': 'postpartcomment',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_section', to='bubbleworld.Section'),
        ),
        migrations.CreateModel(
            name='CommentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=40, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentreport_author', to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentreport_comment', to='bubbleworld.Comment')),
            ],
            options={
                'verbose_name': '评论举报',
                'verbose_name_plural': '评论举报',
                'db_table': 'commentreport',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_section', to='bubbleworld.Section'),
        ),
        migrations.CreateModel(
            name='AdminApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminapply_section', to='bubbleworld.Section')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminapply_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '管理员申请',
                'verbose_name_plural': '管理员申请',
                'db_table': 'adminapply',
                'ordering': ['-created_at'],
            },
        ),
    ]
