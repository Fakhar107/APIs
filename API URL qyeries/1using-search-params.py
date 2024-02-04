import requests
from rich import print

baseurl = 'https://rickandmortyapi.com/api/character/'

def get_character_one_param(char_id):
    resp = requests.get(baseurl + str(char_id))
    print(resp.json())

def search_character(search):
    resp = requests.get(baseurl, params=search)
    print(resp.json()['info'])  # to just get info only from the page

def main():
    search = {
        'name':'rick',
        'status':'dead',
        'page' : 2
    }
    search_character(search=search)


if __name__ == '__main__':
    main()