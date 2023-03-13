# # Python
# from typing import Any

# # Other
# import requests
# from requests.models import Response

# # Flask
# from flask import (
#     Flask, 
#     render_template,
# )
# from flask.app import Flask as FlaskApp

# # Local
# from models.pokemon import (
#     Pokemon,
#     Name,
#     Base
# )

# app: FlaskApp = Flask(__name__)
# pokemons: list[Pokemon] = []

# @app.route("/home")
# def home_page() -> str:
#     return "Welcome to my first page!"

# @app.route("/")
# def main_page() -> str:
#     return render_template(
#         'index.html',
#         ctx_lst=pokemons
#     )

# @app.route("/num")
# def get_nubmers() -> str:
#     result: str = ""
#     for i in range(1, 2001):
#         result += f"<h2>{i}</h2>"

#     return result

# @app.route('/search', methods=['GET'])
# def search() -> Any:
#     query = requests.get('query')
#     if not query:
#         return render_template('search.html', ctx_lst=[])
#     filtered = [p for p in pokemons if query.lower() in p.name.english.lower() or query.lower() in p.type]
#     return render_template('search.html', ctx_lst=filtered)



# if __name__ == '__main__':
#     URL: str = (
#         'https://raw.githubusercontent.'
#         'com/fanzeyi/pokemon.json/'
#         'master/pokedex.json'
#     )
#     response: Response =\
#         requests.get(URL)
#     data: list[dict] = response.json()

#     pokemon: dict[str, Any]
#     for pokemon in data:
#         base = Base(
#             *list(pokemon.get('base').values())
#         )
#         name = Name(
#             *list(pokemon.get('name').values())
#         )
#         pkm = Pokemon(
#             id=pokemon.get('id'),
#             name=name,
#             type=pokemon.get('type'),
#             base=base
#         )
#         pokemons.append(pkm)

#     app.run(
#         port=8080,
#         debug=True
#     )

# Python
from typing import Any

# Other
import requests
from requests.models import Response

# Flask
from flask import (
    Flask, 
    render_template,
    request
)
from flask.app import Flask as FlaskApp

# Local
from models.pokemon import (
    Pokemon,
    Name,
    Base
)

app: FlaskApp = Flask(__name__)
pokemons: list[Pokemon] = []

@app.route("/home")
def home_page() -> str:
    return "Welcome to my first page!"

@app.route("/")
def main_page() -> str:
    return render_template(
        'index.html',
        ctx_lst=pokemons
    )

@app.route('/search', methods=['GET'])
def search() -> Any:
    query = request.args.get('query')
    if not query:
        return render_template('search.html', ctx_lst=[])
    filtered = [p for p in pokemons if query.lower() in p.name.english.lower() or query.lower() in p.type]
    return render_template('search.html', ctx_lst=filtered)

if __name__ == '__main__':
    URL: str = (
        'https://raw.githubusercontent.'
        'com/fanzeyi/pokemon.json/'
        'master/pokedex.json'
    )
    response: Response =\
        requests.get(URL)
    data: list[dict] = response.json()

    pokemon: dict[str, Any]
    for pokemon in data:
        base = Base(
            *list(pokemon.get('base').values())
        )
        name = Name(
            *list(pokemon.get('name').values())
        )
        pkm = Pokemon(
            id=pokemon.get('id'),
            name=name,
            type=pokemon.get('type'),
            base=base
        )
        pokemons.append(pkm)

    app.run(
        port=8080,
        debug=True
    )
