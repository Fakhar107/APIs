import requests
from rich import print
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class CharFilter:
    name: Optional[str] =None 
    status: Optional[str] =None 
    gender: Optional[str] = None
    species: Optional[str] =None
    page: Optional[int] = None

baseurl = 'https://rickandmortyapi.com/api/character/'

def get_character_one_param(char_id):
    resp = requests.get(baseurl + str(char_id))
    print(resp.json())

def search_character(search):
    resp = requests.get(baseurl, params=search)
    print(resp.json()['info'])  # to just get info only from the page

def main():
    search = CharFilter(
        name="rick",
        status="dead"
    )
    print(search)
    print(asdict(search))
    search_character(search=asdict(search))


if __name__ == '__main__':
    main()