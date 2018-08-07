# Generated by Django 2.0.7 on 2018-08-07 04:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the Address', primary_key=True, serialize=False)),
                ('key', models.CharField(help_text='Wallet number max length is 100 chars', max_length=100)),
                ('addrstatus', models.CharField(blank=True, choices=[('a', 'Approved'), ('w', 'Wait approval'), ('u', 'Unassigned'), ('r', 'Reserved')], default='u', help_text='Address current status', max_length=1)),
            ],
            options={
                'ordering': ['key'],
            },
        ),
        migrations.CreateModel(
            name='Blockchain',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this Object across whole app', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Blochchain name', max_length=100)),
                ('connection', models.CharField(help_text='Blochchain connectoin', max_length=100)),
                ('interval', models.IntegerField(help_text='Blochchain refresh interval')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this Customer across whole app', primary_key=True, serialize=False)),
                ('externalID', models.CharField(help_text='Customer ID is uniq identifier', max_length=100)),
                ('lastname', models.CharField(help_text='Customer Last Name', max_length=200)),
                ('firstname', models.CharField(help_text='Customer First Name', max_length=200)),
                ('regdate', models.DateField(blank=True, null=True)),
                ('updatedate', models.DateField(blank=True, null=True)),
                ('kyc', models.CharField(help_text='KYC Data', max_length=200)),
                ('comment', models.CharField(help_text='Customer comments', max_length=1000)),
            ],
            options={
                'ordering': ['lastname'],
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Log', primary_key=True, serialize=False)),
                ('createdate', models.DateField(blank=True, null=True)),
                ('msg', models.CharField(help_text='Message', max_length=100)),
                ('userlogin', models.CharField(help_text='UserLogin', max_length=100)),
                ('objectname', models.CharField(help_text='ObjectName', max_length=100)),
                ('fieldname', models.CharField(help_text='FieldName', max_length=100)),
                ('oldvalue', models.CharField(help_text='OldValue', max_length=250)),
                ('newvalue', models.CharField(help_text='NewValue', max_length=250)),
            ],
            options={
                'ordering': ['createdate'],
            },
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Operations', primary_key=True, serialize=False)),
                ('createdate', models.DateField(blank=True, null=True)),
                ('completedate', models.DateField(blank=True, null=True)),
                ('action', models.CharField(help_text='Action', max_length=250)),
                ('parameter', models.CharField(help_text='FieldName', max_length=250)),
                ('result', models.CharField(help_text='Result', max_length=250)),
            ],
            options={
                'ordering': ['createdate'],
            },
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the WatchList', primary_key=True, serialize=False)),
                ('createdate', models.DateField(blank=True, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('completedate', models.DateField(blank=True, null=True)),
                ('result', models.CharField(help_text='Result', max_length=100)),
                ('status', models.CharField(blank=True, choices=[('a', 'Active'), ('i', 'Inactive'), ('r', 'Reserved')], default='a', help_text='Watch list record status', max_length=1)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reposrv.Address')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='blockchain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reposrv.Blockchain'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reposrv.Customer'),
        ),
    ]