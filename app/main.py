import uvicorn
from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

import logging
 
logging.basicConfig(level=logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/one', response_model=schemas.User)
def read_root(db: Session = Depends(get_db)):
    user = crud.get_user(db)
    return user

if __name__ == '__main__':
    db = SessionLocal()
    if db.query(models.User).count() == 0:
        user = models.User(name='test_user')
        item = models.Item(title='test_item')
        user.items = [item]
        db.add(user)
        db.commit()
    db.close()
    uvicorn.run(app, host="0.0.0.0", port=8000)