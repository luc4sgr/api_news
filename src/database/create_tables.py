from src.database.config import Base, engine
from src.database.models import (
    NewsORM,
    UserORM,
    CategoryORM,
    CommentORM,
    LikeORM  # ➕ importa o novo
)

print("🎯 Criando tabelas no banco...")
Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso!")
