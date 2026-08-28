from django.db import models

class User(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(unique=True)
  mobile = models.PositiveBigIntegerField()
  password = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name

class UserProfile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField(help_text="Enter Bio")
  landmark = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  pincode = models.CharField(max_length=50)
  address = models.TextField(help_text="Enter address")
  latitude = models.DecimalField(max_digits=10, decimal_places=7)
  longitude = models.DecimalField(max_digits=10, decimal_places=7)
  profilepic = models.ImageField(upload_to="users/")
  
  def __str__(self):
    return f"Profile of {self.user.name}"
  
class Restaurant(models.Model):
  name = models.CharField(max_length=200)
  ownername = models.CharField(max_length=200)
  mobile = models.PositiveBigIntegerField()
  email = models.EmailField(unique=True)
  address = models.TextField(help_text="Enter address")
  latitude = models.DecimalField(max_digits=10,decimal_places=7)
  longitude = models.DecimalField(max_digits=10, decimal_places=7)
  restaurantpic = models.ImageField(upload_to="restaurants/")
  is_active = models.BooleanField(default=True)
  
  def __str__(self):
    return self.name
  
class Category(models.Model):
  name = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name
  
class Food(models.Model):
  restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=8,decimal_places=2)
  foodimage = models.ImageField(upload_to="foods/")
  isavailable = models.BooleanField(default=True)
  
  def __str__(self):
    return self.name


class Restaurant(models.Model):
  name=models.CharField(max_length=200)
  ownername=models.CharField(max_length=200)
  mobile=models.PositiveBigIntegerField()
  email=models.EmailField(unique=True)
  address=models.TextField(help_text="Enter Address")
  latitude=models.DecimalField(max_digits=10,decimal_places=7)
  longitude=models.DecimalField(max_digits=10,decimal_places=7)
  restaurantpic=models.ImageField(upload_to="restaurants/")
  is_active=models.BooleanField(default=True)

  def __str__(self):
    return self.name


class Category(models.Model):
  name=models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Food(models.Model):
  restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  name=models.CharField(max_length=200)
  description=models.TextField()
  price=models.DecimalField(max_digits=8,decimal_places=2)
  foodimage=models.ImageField(upload_to="foods/")
  isavailable=models.BooleanField(default=True)

  def __str__(self):
    return self.name


class Cart(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  food = models.ForeignKey(Food,on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  added_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.user.name
  
class Order(models.Model):
  STATUS = (
    ("Pending","Pending"),
    ("Preparing","Preparing"),
    ("Out of Delivery","Out of Delivery"),
    ("Delivered","Delivered")
  )
  
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  total_amount = models.DecimalField(max_digits=10,decimal_places=2)
  delivery_address = models.TextField()
  latitude = models.DecimalField(max_digits=10, decimal_places=7)
  longitude = models.DecimalField(max_digits=10, decimal_places=7) 
  status = models.CharField(max_length=50,choices=STATUS, default="Pending")
  orderedat = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.user.name
  
  
class OrderItem(models.Model):
  order = models.ForeignKey(Order,on_delete=models.CASCADE)
  food = models.ForeignKey(Food,on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()
  price = models.DecimalField(max_digits=8,decimal_places=2)
  
  def __str__(self):
    return self.food.name
  
class Payment(models.Model):
  METHOD = (
    ("UPI","UPI"),
    ("Card","Card"),
    ("Cash","Cash")
  )
  
  STATUS = (
    ("Pending","Pending"),
    ("Success","Success"),
    ("Failed","Failed")
  )
  
  order = models.OneToOneField(Order, on_delete=models.CASCADE)
  paymentmethod = models.CharField(max_length=30,choices=METHOD)
  amount = models.DecimalField(max_digits=10,decimal_places=2)
  paymentstatus = models.CharField(max_length=20,choices=STATUS)
  
  def __str__(self):
    return self.order.user.name
  
class Delivery(models.Model):
  order = models.OneToOneField(Order,on_delete=models.CASCADE)
  ridername = models.CharField(max_length=200)
  riderphone = models.PositiveBigIntegerField()
  currentlatitude = models.DecimalField(max_digits=10, decimal_places=7)
  currentlongitude = models.DecimalField(max_digits=10, decimal_places=7)
  estimatedtime = models.IntegerField()
  delivered  = models.BooleanField(default=False)
  
  def __str__(self):
    return self.order.user.name
  