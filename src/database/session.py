from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession



engine = create_async_engine()
session = sessionmaker(
    bind = engine,
    autoflush = False,
    autocommit = False,
    class_ = AsyncSession
)


async def get_db() -> AsyncSession:
    async with session() as db:
        try:
            yield db
        except:
            db.close()
