<<<<<<< HEAD
# Generated by Django 2.0.7 on 2018-07-25 20:27
=======
# Generated by Django 2.0.7 on 2018-07-25 20:28
>>>>>>> 5ee157a6e9963abee9a232eee44533f9f70ae90a

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comp_Name', models.CharField(max_length=350)),
                ('Commission_Date', models.CharField(max_length=350)),
                ('Decommission_Date', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Cust_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_Date', models.CharField(max_length=350)),
                ('Ship_Date', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept_Name', models.CharField(max_length=350)),
                ('Remaining_Budget', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=350)),
                ('Last_Name', models.CharField(max_length=350)),
                ('Employee_Is_Active', models.BooleanField()),
                ('Comp_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Computer')),
                ('Dept_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Completed', models.BooleanField()),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employment_Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hire_Date', models.CharField(max_length=350)),
                ('Term_Date', models.CharField(max_length=350)),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Ordered_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Order_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Cust_Order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Num', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_Type_Name', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=350)),
                ('Price', models.IntegerField()),
                ('Description', models.CharField(max_length=350)),
                ('Quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_Name', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Training_Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Program_Name', models.CharField(max_length=350)),
                ('Program_Description', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Training_Program_Sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Program_Start_Date', models.CharField(max_length=350)),
                ('Program_End_Date', models.CharField(max_length=350)),
                ('Max_Students', models.IntegerField()),
                ('Program_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Training_Program')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=350)),
                ('Last_Name', models.CharField(max_length=350)),
                ('Street', models.CharField(max_length=350)),
                ('City', models.CharField(max_length=350)),
                ('State', models.CharField(max_length=350)),
                ('Zip', models.IntegerField()),
                ('Phone', models.CharField(max_length=350)),
                ('Email', models.CharField(max_length=350)),
                ('Date_Created', models.CharField(max_length=350)),
                ('Last_Signon', models.CharField(max_length=350)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Seller_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.User'),
        ),
        migrations.AddField(
            model_name='product',
            name='Type_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Product_Type'),
        ),
        migrations.AddField(
            model_name='payment_options',
            name='Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.User'),
        ),
        migrations.AddField(
            model_name='payment_options',
            name='Payment_Type_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Payment_Type'),
        ),
        migrations.AddField(
            model_name='ordered_products',
            name='Product_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Product'),
        ),
        migrations.AddField(
            model_name='employee_training',
            name='Session_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Training_Program'),
        ),
        migrations.AddField(
            model_name='department',
            name='Supervisor_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Employee'),
        ),
        migrations.AddField(
            model_name='cust_order',
            name='Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.User'),
        ),
        migrations.AddField(
            model_name='cust_order',
            name='Payment_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Payment_Options'),
        ),
    ]
