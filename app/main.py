import os
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .authentication.auth import (
    get_password_hash,
    authenticate_user,
    create_access_token,
    get_current_user,
)
from .schemas.user_schema import UserSchema, UserCreate, TokenSchema, TraductionRequest
from .models.user_model import User
from .db.database import engine, Base, get_db
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from .services.traduction_service import translate
from .models.translation_model import TranslationResult

load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
FRONTEND_URL = os.getenv("FRONTEND_URL")

app = FastAPI()

origins = [FRONTEND_URL]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.post("/auth/register", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username, email=user.email, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@app.post("/auth/login", response_model=TokenSchema)
def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="INcorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=UserSchema)
async def read_users_me(current_user: UserSchema = Depends(get_current_user)):
    return current_user


@app.get("/")
def get_home():
    return {"message": "Hello to our traduction application api!!"}


@app.post("/predict")
async def get_prediction(
    req: TraductionRequest,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    translation_text = translate(req.text, req.language).get("translation_text")

    user_id = user.id
    original_text = req.text
    source_language = req.language.split("-")[0]
    target_language = req.language.split("-")[1]

    new_translation = TranslationResult(
        user_id=user_id,
        original_text=original_text,
        translated_text=translation_text,
        source_language=source_language,
        target_language=target_language,
    )

    db.add(new_translation)
    db.commit()
    db.refresh(new_translation)

    return new_translation
