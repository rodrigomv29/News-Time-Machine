from django.db import models

# Create your models here.
from pydantic import BaseModel

class Article(BaseModel):
    title: str
    description: str
    publisher: str
    publish_date: str
    url: str

