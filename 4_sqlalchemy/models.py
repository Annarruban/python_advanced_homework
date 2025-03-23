from sqlalchemy import (
    create_engine,
    Table, Column, String, Text, Numeric,
    Float,  ForeignKey, Integer, Identity, DateTime, text, Boolean
)
from decimal import Decimal
from sqlalchemy.orm import mapped_column, Mapped, relationship
from common import Base


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    price: Mapped[Decimal] = mapped_column(Numeric(100, 2))

    in_stock: Mapped[bool] = mapped_column(Boolean)

    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("category.id", ondelete="CASCADE")
    )

    category: Mapped['Category'] = relationship('Category', back_populates='products')


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)

    products: Mapped[list['Product']] = relationship(
        'Product',
        uselist=True,
        back_populates='category',
        cascade="all, delete",
        passive_deletes=True,
    )
