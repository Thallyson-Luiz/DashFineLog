from django.db import models
from utils.resize import resize_image_django
from modules.coins import get_coin_today
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
    
    # Validando ticker e trading pair
    def clean(self) -> None:
        if not (self.ticker and self.trading_pair):
            raise ValidationError("Ticker e Trading Pair devem ser preenchidos")
        
        coin_verify = get_coin_today(self.ticker, self.trading_pair)

        if not coin_verify:
            raise ValidationError("Ticker e Trading Pair não aceitos")

        if not self.User_person:
            raise ValidationError("User deve ser preenchido")
            
        return super().clean()
    
    def save(self, *args, **kwargs):
        # Convertendo ticker para maiusculo
        if self.ticker:
            self.ticker = self.ticker.upper()

        self.full_clean()

        # Salvando
        super().save(*args, **kwargs)
