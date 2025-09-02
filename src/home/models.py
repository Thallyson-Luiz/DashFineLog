from django.db import models
from utils.resize import resize_image_django
from django.contrib.auth.models import User

# Modelo de criptomoeda
class CriptoMoeda(models.Model):
    class Meta:
        verbose_name = "criptomoeda"
        managed = True
        verbose_name_plural = "criptomoedas"

    ticker = models.CharField(max_length=10, 
                              null=False, 
                              unique=True, 
                              blank=False, 
                              help_text="Ticker da criptomoeda, tambem chamado de sigla")

    trading_pair = models.CharField(max_length=10,
                                    null=False,
                                    blank=False,
                                    default="USD", 
                                    editable=False, 
                                    help_text="Par de negociacao da criptomoeda")
    
    img = models.ImageField(upload_to='img/criptomoedas/',
                            null=False, 
                            blank=False, 
                            help_text="Imagem da criptomoeda")
    
    def __str__(self):
        return self.ticker
    
    def save(self, *args, **kwargs):
        # Convertendo ticker para maiusculo
        if self.ticker:
            self.ticker = self.ticker.upper()

        # Redimensionando imagem
        if self.img:
            resize_image_django(self.img, new_width=100)

        # Salvando
        super().save(*args, **kwargs)
    
class Coin(models.Model):
    class Meta:
        verbose_name = "Coin"
        verbose_name_plural = "Coins"

    ticker = models.CharField(max_length=10, 
                              null=False, 
                              unique=True, 
                              blank=False, 
                              help_text="Ticker da criptomoeda, tambem chamado de sigla")

    trading_pair = models.CharField(max_length=10,
                                    null=False,
                                    blank=False,
                                    default="USD",
                                    editable=True,
                                    help_text="Par de negociacao da criptomoeda")
    
    User_person = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='coins')

    def __str__(self):
        return f'{self.ticker} - {self.trading_pair} - {self.User_person}'
    
    def save(self, *args, **kwargs):
        # Convertendo ticker para maiusculo
        if self.ticker:
            self.ticker = self.ticker.upper()

        # Salvando
        super().save(*args, **kwargs)
