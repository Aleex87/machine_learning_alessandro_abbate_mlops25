from constans import DATA_PATH
import json
from pprint import pprint
from pydantic import BaseModel, Field



# convinience / utility function to read a json file
def read_jason(filname):
    with open(DATA_PATH / filname) as file:
        data= json.load(file)
    return data

# data models

class Book(BaseModel):
    id : int 
    title : str
    author : str
    year : int = Field(gt= 1000, lt= 2027, description="Year when book was published") 
    description: str


class Library(BaseModel):
    name: str
    books: list[Book]

# deserialize json data in to pydantic models

def library_data(filename):
    json_data = read_json(filename)
    Library(name="Coolu libraru", books=[{
            'author': 'Douglas Adams',
            'description': 'A humorous scienceâ€‘fiction adventure following '
                           'an ordinary man through absurd and unexpected '
                           'cosmic events.',
            'id': 1,
            'title': "The Hitchhiker's Guide to the Galaxy",
            'year': 1979},])

    return Library(**json_data)


    


pprint(read_jason("library.json"))
