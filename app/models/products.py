from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.categories import Category


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(500))
    price: Mapped[float]
    image_url: Mapped[str | None] = mapped_column(String(200))
    stock: Mapped[int]
    is_active: Mapped[bool] = mapped_column(default=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    category: Mapped['Category'] = relationship(back_populates='products')
