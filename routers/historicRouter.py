from fastapi import APIRouter, Depends, status, Response, UploadFile, File, HTTPException
from databases import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas import historicSchema
from repositories import historicRepository