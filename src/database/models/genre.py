from sqlalchemy import Column, ForeignKey, Table, Text
from sqlalchemy.orm import mapped_column, relationship, Mapped

from .base import Base

movie_genre = Table(
    'movie_genre',
    Base.metadata,
    Column("movie_id", Text, ForeignKey('movies.id', ondelete="CASCADE"), primary_key=True),
    Column("genre_id", Text, ForeignKey('genres.id', ondelete="CASCADE"), primary_key=True)
)

class GenreSchema(Base):
    __tablename__ = "genres"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    
    movies: Mapped[set["MovieSchema"]] = relationship( # type: ignore
        secondary=movie_genre,
        back_populates="genres",
        lazy="selectin"
    )
