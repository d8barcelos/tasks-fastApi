from fastapi import APIRouter, Depends, HTTPException
from crud.crud import get_users
from schemas import UserCreate, User
from crud import create_user, get_user_by_email
from database import get_db
from sqlalchemy.orm import Session
from auth.auth_handler import signJWT

router = APIRouter()

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if user and user.password == password:
        return signJWT(user.id)
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.get("/", response_model=list[User])
def read_users_route(db: Session = Depends(get_db)):
    return get_users(db)
