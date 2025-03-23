from decimal import Decimal
from common import session_factory, Base, engine
from models import Product, Category


session = session_factory()
Base.metadata.create_all(engine)


category1 = Category(name="Toys", description="Electronic devices and gadgets")
category2 = Category(name="Cats", description="Various books and literature")

session.add_all([category1, category2])
session.commit()


product1 = Product(name="Barbie", price=Decimal("1200.50"), in_stock=True, category_id=category1.id)
product2 = Product(name="Baseball bat", price=Decimal("800.99"), in_stock=True, category_id=category1.id)
product3 = Product(name="Pushok", price=Decimal("15.99"), in_stock=True, category_id=category2.id)

session.add_all([product1, product2, product3])
session.commit()



all_products = session.query(Product).all()
for product in all_products:
    print(f"Product: {product.name}, Price: {product.price}, In Stock: {product.in_stock}")

categories = session.query(Category).all()
for category in categories:
    print(f"Category: {category.name}, Products: {[p.name for p in category.products]}")


available_products = session.query(Product).filter(Product.in_stock == True).all()
for product in available_products:
    print(f"Available Product: {product.name} - ${product.price}")


toys = session.query(Product).join(Category).filter(Category.name == "toys").all()
for toy in toys:
    print(f"Toys: {product.name} - ${product.price}")