from django.db import models

# Create your models here.
from pydantic import BaseModel

class Article(BaseModel):
    title: str
    author_name: str
    description: str
    publisher: str
    pub_date: str
    url: str


    def __str__(self) -> str:
        return f"{self.publisher}: {self.title}"

