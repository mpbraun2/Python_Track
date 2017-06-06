from django.shortcuts import render
from .models import Product

def index(request):
    Product.objects.create(product_name="Ball", product_type="Toy", description="It's an old family favorite! The ball!")
    Product.objects.create(product_name="Cards", product_type="Toy", description="It's an old family favorite! A deck of cards!")
    Product.objects.create(product_name="Pogs", product_type="Toy", description="Hailing from the 90's, its Pog!")
    product = Product.objects.all()
    print (product)
    return render(request, 'firstapp/index.html')
