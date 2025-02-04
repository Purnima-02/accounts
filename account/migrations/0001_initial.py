# Generated by Django 5.0.7 on 2024-11-11 09:20

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisbursementData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.CharField(max_length=100)),
                ('fran_code', models.CharField(blank=True, max_length=100, null=True)),
                ('dsa_code', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(default='', max_length=1000)),
                ('refid', models.CharField(blank=True, max_length=500, null=True)),
                ('franchrefid', models.CharField(blank=True, max_length=400, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisbursementDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_nbfc_name', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_loginid', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('loan_amount', models.CharField(blank=True, max_length=20, null=True)),
                ('disbursement_date', models.DateField(default=datetime.date.today)),
                ('tenure', models.CharField(blank=True, max_length=50, null=True)),
                ('roi', models.CharField(blank=True, max_length=50, null=True)),
                ('insurance', models.CharField(blank=True, max_length=50, null=True)),
                ('net_disbursement', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_person_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=10, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('disbursement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='account.disbursementdata')),
            ],
        ),
        migrations.CreateModel(
            name='InputWindow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payout_slab_amount_or_percentage', models.CharField(max_length=10)),
                ('payout_input_date', models.DateTimeField(blank=True, null=True)),
                ('UTR_number', models.CharField(max_length=30)),
                ('credited_bank_name', models.CharField(max_length=50)),
                ('credited_bank_ac_number', models.CharField(max_length=20)),
                ('TDS', models.CharField(max_length=50)),
                ('net_loan_amount', models.DecimalField(decimal_places=0, default=0.0, max_digits=10)),
                ('net_amount_received', models.CharField(max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('disbursement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_windows', to='account.disbursementdata')),
            ],
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_payout_slab_in_Rs', models.CharField(blank=True, max_length=20, null=True)),
                ('dsa_payout_slab_in_Rs', models.CharField(blank=True, max_length=50, null=True)),
                ('refCode', models.CharField(blank=True, max_length=1000, null=True)),
                ('franchCode', models.CharField(blank=True, max_length=1000, null=True)),
                ('application_id', models.CharField(max_length=1000, null=True)),
                ('dsaIsClaim', models.BooleanField(blank=True, default=False, null=True)),
                ('franchiseIsClaim', models.BooleanField(blank=True, default=False, null=True)),
                ('dateClaimed', models.DateField(auto_now_add=True)),
                ('loan_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('disbursedAmount', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('appliCreatedAt', models.DateField(blank=True, null=True)),
                ('disbursement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='output_windows', to='account.disbursementdata')),
                ('disbursement_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='output_windows', to='account.disbursementdetail')),
                ('input_window', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='output_windows', to='account.inputwindow')),
            ],
        ),
        migrations.CreateModel(
            name='SettlementWindow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.CharField(max_length=1000)),
                ('refCode', models.CharField(blank=True, max_length=1000, null=True)),
                ('franchCode', models.CharField(blank=True, max_length=1000, null=True)),
                ('Settlement_Date', models.DateField(default=datetime.date.today)),
                ('UTR_Number', models.CharField(max_length=30)),
                ('dsa_Amount_in_Rs', models.PositiveIntegerField(blank=True, null=True)),
                ('franch_Amount_in_Rs', models.PositiveIntegerField(blank=True, null=True)),
                ('DR_From_Bank', models.CharField(max_length=100)),
                ('Settlement_By', models.CharField(max_length=100)),
                ('DR_Bank_Account_Number', models.CharField(max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('disbursement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settle_windows', to='account.disbursementdata')),
                ('output_window', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settle_windows', to='account.disbursement')),
            ],
        ),
    ]
