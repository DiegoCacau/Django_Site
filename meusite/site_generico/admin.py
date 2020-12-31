from django.contrib import admin
from .models import *


admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Sex)
admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(Stock)
admin.site.register(Client)
admin.site.register(PaymentStatus)
admin.site.register(PaymentMethod)
admin.site.register(Invoice)
admin.site.register(InvoiceProduct)
admin.site.register(Rating)