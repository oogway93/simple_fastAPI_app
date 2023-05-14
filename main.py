import uvicorn
from fastapi import FastAPI
from database import session, engine, Base
from routers import book as BookRouters

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(BookRouters.router, prefix='/book')  # connect routers

if __name__ == '__main__':  # useless code for someone (you can write it in a terminal 'uvicorn main:app --reload'. It's the same)
    uvicorn.run("main:app", reload=True)
