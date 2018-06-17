from django.db import models


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
        ('U', '未知'),
    )
    birth_date = models.DateField(verbose_name='生年月日')
    last_name = models.CharField(verbose_name='姓', max_length=20, null=True, blank=True)
    first_name = models.CharField(verbose_name='名', max_length=20, null=True, blank=True)
    gender = models.CharField(verbose_name='性別', max_length=1, default='U', choices=GENDER_CHOICES)
    hire_date = models.DateField(verbose_name='雇用日')

    class Meta:
        verbose_name = '社員'
        verbose_name_plural = '社員'
        db_table = 'yo_employees'

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='出勤时间')
    end_time = models.DateTimeField(verbose_name='退勤时间')
    rest_time = models.SmallIntegerField(verbose_name='休息时间')

    class Meta:
        verbose_name = '考勤'
        verbose_name_plural = '考勤'
        db_table = 'yo_attendances'

    def __str__(self):
        return "{} {}".format(self.employee, self.start_time.date())


class Salary(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.BigIntegerField(verbose_name='工资', null=True, blank=True)
    present_flg = models.CharField(verbose_name='现在适用', max_length=1, default='0')
    start_date = models.DateField(verbose_name='适用开始日', null=True, blank=True)
    end_date = models.DateField(verbose_name='适用终了日', null=True, blank=True)

    class Meta:
        verbose_name = '社員工资'
        verbose_name_plural = '社員工资'
        db_table = 'yo_employee_salary'

    def __str__(self):
        return "{} 工资".format(self.employee)

