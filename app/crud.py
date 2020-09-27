from sqlalchemy.orm import Session

import models

def get_user(db: Session):
    return db.query(models.User).first()

