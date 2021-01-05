from django.db import models


class Contract(models.Model):

    COMPANY_CHOICES = [
        ('ЛЕКОПТ', 'ЛЕКОПТ'),
        ('ЭН-ФАРМ', 'ЭН-ФАРМ'),
    ]

    CONTRACT_ENFORCEMENT_CHOICES = [
        ('ДЕНЬГИ', 'ДЕНЬГИ'),
        ('ГАРАНТИЯ', 'ГАРАНТИЯ'),
        ('НЕТ', 'НЕТ')
    ]

    company_name = models.CharField(
        max_length=7,
        choices=COMPANY_CHOICES,
        blank=True,
        verbose_name='Компания'
    )
    notice_number = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='№ извещения'
    )
    signing_date = models.DateField(
        null=True,
        verbose_name='Дата заключения'
    )
    ending_date = models.DateField(
        null=True,
        verbose_name='Срок действия'
    )
    region = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='Регион'
    )
    client = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Заказчик',
    )
    mnn = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='МНН'
    )
    tn = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='ТН'
    )
    manufacturer = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Производитель'
    )
    vendor = models.CharField(
        max_length=128,
        null=True,
        verbose_name='Поставщик'
    )
    price = models.FloatField(
        default=0,
        verbose_name='Цена за уп.',
        editable=None
    )
    full_price = models.FloatField(
        null=True,
        verbose_name='Цена контракта'
    )
    quantity = models.SmallIntegerField(
        null=True,
        verbose_name='Количество, уп.'
    )
    saled_quantity = models.SmallIntegerField(
        null=True,
        verbose_name='Отгружено, уп.'
    )
    remains_quantity = models.SmallIntegerField(
        default=0,
        verbose_name='Остаток по контракту, уп.',
        editable=None
    )
    completed_percent = models.FloatField(
        default=0,
        verbose_name='Процент завершения',
        editable=None
    )
    next_sale_date = models.DateField(
        null=True,
        verbose_name='Следующая дата поставки'
    )
    on_request = models.BooleanField(
        default=True,
        verbose_name='Поставка по заявкам'
    )
    delivery_period = models.SmallIntegerField(
        null=True,
        verbose_name='Срок поставки, дней'
    )
    contract_enforcement_method = models.CharField(
        max_length=8,
        choices=CONTRACT_ENFORCEMENT_CHOICES,
        blank=True
    )
    comments = models.TextField(
        max_length=256,
        blank=True,
        verbose_name='Комментарии'
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name='Выполнен'
    )

    def __str__(self):
        return self.notice_number

    def save(self):
        self.price = self.full_price / self.quantity
        self.remains_quantity = self.quantity - self.saled_quantity
        self.completed_percent = self.saled_quantity * 100 / self.quantity
        super().save()
