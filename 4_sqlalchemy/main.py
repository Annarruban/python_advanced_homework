from decimal import Decimal
from common import session_factory, Base, engine
from models import Product, Category


session = session_factory()
Base.metadata.create_all(engine)


category1 = Category(name="Электроника", description="Гаджеты и устройства.")
category2 = Category(name="Книги", description="Печатные книги и электронные книги.")
category3 = Category(name="Одежда", description="Одежда для мужчин и женщин.")

session.add_all([category1, category2, category3])
session.commit()


product1 = Product(name="Смартфон", price=Decimal("299.99"), in_stock=True, category_id=category1.id)
product2 = Product(name="Ноутбук", price=Decimal("499.99"), in_stock=True, category_id=category1.id)
product3 = Product(name="Научно-фантастический роман", price=Decimal("15.99"), in_stock=True, category_id=category2.id)
product4 = Product(name="Джинсы", price=Decimal("40.50"), in_stock=True, category_id=category3.id)
product5 = Product(name="Футболка", price=Decimal("20.00"), in_stock=True, category_id=category3.id)

session.add_all([product1, product2, product3, product4, product5])
session.commit()



all_products = session.query(Product).all()
for product in all_products:
    print(f"Product: {product.name}, Price: {product.price}, In Stock: {product.in_stock}")

categories = session.query(Category).all()
for category in categories:
    print(f"Category: {category.name}, Products: {[p.name for p in category.products]}")


available_products = session.query(Product).filter(Product.in_stock == True).all()
for product in available_products:
    print(f"Available Product: {product.name} - ${product.price}, {product.category.name}")

