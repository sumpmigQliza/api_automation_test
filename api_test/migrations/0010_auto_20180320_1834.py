# Generated by Django 2.0.2 on 2018-03-20 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0009_automationparameterraw'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomationResponseJson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True, verbose_name='JSON参数')),
            ],
            options={
                'verbose_name': '结果JSON参数',
                'verbose_name_plural': '结果JSON参数管理',
            },
        ),
        migrations.AlterModelOptions(
            name='automationparameterraw',
            options={'verbose_name': '源数据参数', 'verbose_name_plural': '源数据参数管理'},
        ),
        migrations.AlterField(
            model_name='automationcaseapi',
            name='examineType',
            field=models.CharField(choices=[('no_check', '不校验'), ('only_check_status', '校验http状态'), ('json', 'JSON校验'), ('entirely_check', '完全校验'), ('Regular_check', '正则校验')], default='no_check', max_length=50, verbose_name='校验方式'),
        ),
        migrations.AlterField(
            model_name='automationparameterraw',
            name='data',
            field=models.TextField(blank=True, null=True, verbose_name='源数据请求参数'),
        ),
        migrations.AddField(
            model_name='automationresponsejson',
            name='automationCaseApi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='api_test.AutomationCaseApi', verbose_name='接口'),
        ),
    ]