from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.products import Product


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(String(50))
    parent_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id'))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    products: Mapped[list['Product']] = relationship(
        back_populates='category',
        cascade='all, delete-orphan'
    )

    parent: Mapped['Category' | None] = relationship(
        back_populates='children',
        remote_side="Category.id"
    )
    children: Mapped[list['Category']] = relationship(
        back_populates='parent',
        cascade='all, delete-orphan'
    )
