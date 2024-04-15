from django.shortcuts import render

# Create your views here.
from ninja import Router
from .models import Article

router = Router()

@router.get("/articles/{article_id}")
def get_podcast(request, article_id: int):
    # Logic to retrieve podcast by ID from database and return as response
    pass

@router.post("/articles/")
def create_podcast(request, articles: Article):
    # Logic to create a new podcast in the database based on input data
    pass

@router.put("/articles/{article_id}")
def update_podcast(request, article_id: int, articles: Article):
    # Logic to update an existing podcast in the database based on input data
    pass

@router.delete("/articles/{article_id}")
def delete_podcast(request, article_id: int):
    # Logic to delete a podcast from the database by ID
    pass

