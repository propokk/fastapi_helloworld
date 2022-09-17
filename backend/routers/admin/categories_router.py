from http.client import HTTPException
from fastapi import APIRouter, Depends
from typing import List, Optional
from backend.models.admin_schemas import SetCategoriesBody, SetCategoryDB
from backend.models.model import Categories
from backend.models.admin_models_dals import CategoriesDAL
from backend.models.db.connections import get_db
from databases import Database


category_router = APIRouter()

@category_router.post("/category", response_model=SetCategoryDB)
async def create_category(payload: SetCategoriesBody, session: Database = Depends(get_db)):
    #category_dal = CategoriesDAL(session)
    category_id = await CategoriesDAL.create_category(payload)
    
    response_obj = {
        "id": category_id,
        "name": payload.name,
        "description": payload.description,
    }
    return response_obj

@category_router.get("/category", response_model=SetCategoryDB)
async def get_all_categories(session: Database = Depends(get_db)):
    # category_dal = CategoriesDAL(session)
    category = await CategoriesDAL.get_all_categories()
    if not category:
        raise HTTPException(status_code=404, detail="No categories was found")
    return category

@category_router.put("/category/{id}", response_model=SetCategoryDB)
async def update_category(id: int, payload: SetCategoriesBody, session: Database = Depends(get_db)):
    #category_dal = CategoriesDAL(session)
    category_id = await CategoriesDAL.update_category(id, payload)

    response_obj = {
        "id": category_id,
        "name": payload.name,
        "description": payload.description,
    }
    return response_obj

@category_router.delete("/category/{id}")
async def delete_category(id: int, session: Database = Depends(get_db)):
    #category_dal = CategoriesDAL(session)
    return await CategoriesDAL.delete_category(id)