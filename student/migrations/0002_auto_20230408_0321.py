# Generated by Django 3.2.7 on 2023-04-08 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillFeeTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='GradeModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('grade', models.CharField(max_length=20)),
                ('grade_num', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='SectionModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('section', models.CharField(max_length=20)),
                ('section_num', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'sections',
            },
        ),
        migrations.CreateModel(
            name='YearGradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.grademodel')),
            ],
        ),
        migrations.CreateModel(
            name='YearGradeSectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.sectionmodel')),
                ('year_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.yeargrademodel')),
            ],
            options={
                'unique_together': {('year_grade', 'section')},
            },
        ),
        migrations.RemoveField(
            model_name='billmodel',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='billmodel',
            name='bill_type',
        ),
        migrations.RemoveField(
            model_name='billmodel',
            name='student_parent',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='grade',
        ),
        migrations.AddField(
            model_name='billmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='billmodel',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='billmodel',
            name='version',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='admitted_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='billmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='roll_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='studentparentmodel',
            unique_together={('student', 'parent')},
        ),
        migrations.AlterModelTable(
            name='billmodel',
            table='bill',
        ),
        migrations.AlterModelTable(
            name='parentmodel',
            table='parents',
        ),
        migrations.AlterModelTable(
            name='paymentmodel',
            table='payments',
        ),
        migrations.AlterModelTable(
            name='studentmodel',
            table='students',
        ),
        migrations.CreateModel(
            name='YearModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('year', models.IntegerField()),
                ('year_ad', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('grades', models.ManyToManyField(through='student.YearGradeModel', to='student.GradeModel')),
            ],
            options={
                'db_table': 'years',
            },
        ),
        migrations.CreateModel(
            name='YearGradeStudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentmodel')),
                ('year_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.yeargrademodel')),
            ],
            options={
                'unique_together': {('year_grade', 'student')},
            },
        ),
        migrations.CreateModel(
            name='YearGradeSectionStudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentmodel')),
                ('year_grade_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.yeargradesectionmodel')),
            ],
            options={
                'unique_together': {('year_grade_section', 'student')},
            },
        ),
        migrations.AddField(
            model_name='yeargrademodel',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.yearmodel'),
        ),
        migrations.AddField(
            model_name='grademodel',
            name='years',
            field=models.ManyToManyField(through='student.YearGradeModel', to='student.YearModel'),
        ),
        migrations.CreateModel(
            name='FeeTypeModel',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fee_type', models.CharField(choices=[('STUDENT_FEES', 'Student Fees'), ('ADMISSION_FEE', 'Admission Fee'), ('EXAM_FEE', 'Exam Fee'), ('UNIFORM_FEE', 'Uniform Fee'), ('OTHER_FEE', 'Other Fee')], max_length=20)),
                ('amount', models.FloatField()),
                ('bills', models.ManyToManyField(through='student.BillFeeTypeModel', to='student.BillModel')),
            ],
            options={
                'db_table': 'fee_type',
            },
        ),
        migrations.AddField(
            model_name='billfeetypemodel',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.billmodel'),
        ),
        migrations.AddField(
            model_name='billfeetypemodel',
            name='fee_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.feetypemodel'),
        ),
        migrations.AddField(
            model_name='billmodel',
            name='fee_types',
            field=models.ManyToManyField(through='student.BillFeeTypeModel', to='student.FeeTypeModel'),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='year_grade',
            field=models.ManyToManyField(blank=True, through='student.YearGradeStudentModel', to='student.YearGradeModel'),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='year_grade_section',
            field=models.ManyToManyField(blank=True, through='student.YearGradeSectionStudentModel', to='student.YearGradeSectionModel'),
        ),
        migrations.AlterUniqueTogether(
            name='yeargrademodel',
            unique_together={('year', 'grade')},
        ),
        migrations.CreateModel(
            name='StudentYearModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentmodel')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.yearmodel')),
            ],
            options={
                'unique_together': {('year', 'student')},
            },
        ),
        migrations.CreateModel(
            name='GradeSectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveIntegerField(default=1)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.grademodel')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.sectionmodel')),
            ],
            options={
                'unique_together': {('grade', 'section')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='billfeetypemodel',
            unique_together={('bill', 'fee_type')},
        ),
    ]
