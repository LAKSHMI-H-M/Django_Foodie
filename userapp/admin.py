from django.contrib import admin
from userapp.models import User,UserProfile,Restaurant,Order,OrderItem,Delivery,Cart,Food,Category,Payment

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Delivery)
admin.site.register(Cart)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Payment)
