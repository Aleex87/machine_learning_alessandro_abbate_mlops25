from constans import DATA_PATH
import json
from pprint import pprint
from pydantic import BaseModel, Field


# convenience/utility function to read a json file
def read_json(filename):
    with open(DATA_PATH / filename) as file:
        data = json.load(file)

    return data


# data models


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int = Field(gt=1000, lt=2027, description="Year when book was published")
    description: str

    model_config = {
    "json_schema_extra": {
        "example": {
            "id": 11,
            "title": "Fluent Python",
            "author": "Luciano Ramalho",
            "year": 2022,
            "description": "Deep dive into Python"
            }
        }
    }

class Library(BaseModel):
    name: str
    books: list[Book]


# deserialize json data into pydantic models
def library_data(filename):
    json_data = read_json(filename)

    # json data unpacks
    # Library(name="Coolu library", books = [...])
    return Library(**json_data)

if __name__ == "__main__":
    # pydantic model
    pprint(library_data("library.json").books)