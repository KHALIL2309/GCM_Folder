# Generated by Django 3.2.9 on 2022-01-12 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet_medical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyseMedical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateAnalyse', models.DateTimeField(null=True)),
                ('LibelleAnalyse', models.CharField(max_length=200, null=True)),
                ('DateCreation', models.DateTimeField(auto_now_add=True, null=True)),
                ('DateModification', models.DateTimeField(auto_now_add=True, null=True)),
                ('IDConsultation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='Antecedent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Antecedent', models.CharField(max_length=500, null=True)),
                ('Observation', models.CharField(max_length=500, null=True)),
                ('CodeAntecedent', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Laboratoire', models.CharField(max_length=50, null=True)),
                ('Adresse', models.CharField(max_length=200, null=True)),
                ('Ville', models.CharField(max_length=100, null=True)),
                ('Pays', models.CharField(max_length=100, null=True)),
                ('CodePostal', models.CharField(max_length=50, null=True)),
                ('Tel1', models.CharField(max_length=50, null=True)),
                ('Tel2', models.CharField(max_length=50, null=True)),
                ('Fax', models.CharField(max_length=50, null=True)),
                ('Email', models.CharField(max_length=200, null=True)),
                ('NomContact', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=200, null=True)),
                ('CodeBarre', models.CharField(max_length=50, null=True)),
                ('Tableau', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DatePrescription', models.DateTimeField(null=True)),
                ('Observation', models.CharField(max_length=500, null=True)),
                ('DateCreation', models.DateTimeField(auto_now_add=True, null=True)),
                ('DateModification', models.DateTimeField(auto_now_add=True, null=True)),
                ('IDConsultation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='TypeActe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeActe', models.CharField(max_length=500, null=True)),
                ('CodeActe', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAnalyse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeAnalyse', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeDocumentFourni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeDocumentFourni', models.CharField(max_length=200, null=True)),
                ('Contenue', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='rdv',
            name='DateDebut',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='rdv',
            name='DateFin',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='PrescriptionMedicament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Posologie', models.CharField(max_length=200, null=True)),
                ('IDMedicament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.medicament')),
                ('IDPrescription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentFourni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contenue', models.CharField(max_length=500, null=True)),
                ('DateDocument', models.DateTimeField(auto_now_add=True, null=True)),
                ('IDPatient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.patient')),
                ('IDTypeDocumentFourni', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.typedocumentfourni')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LibelleDocument', models.CharField(max_length=200, null=True)),
                ('Document', models.CharField(max_length=200, null=True)),
                ('IDPatient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.patient')),
            ],
        ),
        migrations.CreateModel(
            name='DetailAnalyseMedical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResultatAnalyse', models.CharField(max_length=200, null=True)),
                ('Positif', models.BooleanField()),
                ('IDAnalyseMedical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.analysemedical')),
                ('IDTypeAnalyse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='AntecedentPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Observation', models.CharField(max_length=500, null=True)),
                ('IDAntecedent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.antecedent')),
                ('IDPatient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.patient')),
            ],
        ),
        migrations.AddField(
            model_name='analysemedical',
            name='IDLaboratoire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.laboratoire'),
        ),
        migrations.CreateModel(
            name='Acte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateActe', models.CharField(max_length=500, null=True)),
                ('CodeActe', models.CharField(max_length=50, null=True)),
                ('RapportActe', models.CharField(max_length=500, null=True)),
                ('MontantActe', models.FloatField(max_length=500, null=True)),
                ('Gratuit', models.BooleanField()),
                ('DateCreation', models.DateTimeField(auto_now_add=True, null=True)),
                ('DateModification', models.DateTimeField(auto_now_add=True, null=True)),
                ('IDMedecin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.medecin')),
                ('IDPatient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.patient')),
                ('IDTypeActe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet_medical.typeacte')),
            ],
        ),
    ]
