from fastapi import APIRouter
from schema.schemas import list_of_indi_serial
from config.database import collection_name
from models.todos import database_pattern

router=APIRouter()

@router.get("/")
async def get_todos():
    todos=list_of_indi_serial(collection_name.find())
    return todos
@router.post("/post")
async def post_data(data:database_pattern):
    collection_name.insert_one(dict(data))
@router.put("/{id}")
async def update(id:str,data:database_pattern):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(data)})

@router.delete("/{id}")
async def delete_data(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})


