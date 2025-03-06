from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text


class Item(Base):
    __tablename__='Items'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)
    on_offer=Column(Boolean,default=False)
    price=Column(Integer)

    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"
    
    