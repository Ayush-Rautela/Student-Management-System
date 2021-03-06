# Generated by Django 2.1.5 on 2019-05-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Subject', models.CharField(max_length=100)),
                ('Mobile_No', models.IntegerField()),
                ('Body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=255)),
                ('code', models.IntegerField(default=0, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=255)),
                ('phone_no', models.IntegerField(default=0, max_length=14)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('email', models.CharField(default='bknfdvnk', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('subject', models.CharField(max_length=100)),
                ('notice', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=250)),
                ('Body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Block_Name', models.CharField(max_length=255)),
                ('Room_Number', models.IntegerField()),
                ('Bed_Availabel', models.IntegerField()),
                ('Student_Name', models.CharField(max_length=255)),
                ('Floor', models.CharField(max_length=255)),
                ('Registration_Number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='')),
                ('Registration_Number', models.IntegerField()),
                ('Student_Name', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=10)),
                ('Course', models.CharField(max_length=100)),
                ('Blood_Group', models.CharField(max_length=4)),
                ('Date_of_birth', models.DateField()),
                ('Mobile_Number', models.IntegerField()),
                ('Email_id', models.CharField(max_length=255)),
                ('Father_Name', models.CharField(max_length=255)),
                ('Father_Mobile_Number', models.IntegerField()),
                ('Address', models.TextField()),
            ],
        ),
    ]
