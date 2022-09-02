from fastapi import APIRouter, Depends
from typing import List, Optional
from models.model import Categories
from models.admin_models_dals import CategoriesDAL
from models.db.connections import get_db
from databases import Database


category_router = APIRouter()

@category_router.post("/category")
async def create_category(name: str, description: str, session: Database = Depends(get_db)):
    category_dal = CategoriesDAL(session)
    return await category_dal.create_category(name, description)

@category_router.get("/category")
async def get_all_quizzes(session: Database = Depends(get_db)) -> List[Categories]:
    category_dal = CategoriesDAL(session)
    return await category_dal.get_all_categories()

@category_router.put("/category/{category_id}")
async def update_category(category_id: int, name: Optional[str], description: Optional[str], session: Database = Depends(get_db)):
    category_dal = CategoriesDAL(session)
    return await category_dal.update_category(category_id, name, description)

@category_router.delete("/category/{category_id}")
async def delete_category(category_id: int, name: Optional[str], description: Optional[str], session: Database = Depends(get_db)):
    category_dal = CategoriesDAL(session)
    return await category_dal.delete_category(category_id, name, description)