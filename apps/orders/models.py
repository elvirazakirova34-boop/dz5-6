from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = [ 
        ('new', 'Новый'),
        ('accepted', 'Принят'),
        ('closed', 'Закрыт'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    coffee_type = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new' )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.coffee_type}-{self.customer.username }"
    
    

