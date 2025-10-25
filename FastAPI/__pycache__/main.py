from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

# # FastAPIのインスタンス化、APIの様々な設定を追加
# app = FastAPI()

# # アプリケーションのルートの一番メインのURLにアクセスがあった場合、以下の関数を実行する
# # asyncは非同期処理を実行する
# @app.get("/countries/")
# async def country(country_name: str, country_no: Optional[int] = None):
#     # レスポンスの内容
#     return {'country_name': country_name,
#             'country_no': country_no}

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    item: List[Item]

app = FastAPI()
    
@app.post("/")
async def index(data: Data):
    return {'data': data}