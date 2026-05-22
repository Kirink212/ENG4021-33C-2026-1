from django.db import transaction
from ecommerceapp.models import Director, Movie

movies_data = [
    {
        "title": "The Shawshank Redemption",
        "description": "Dois homens presos desenvolvem uma amizade profunda enquanto enfrentam décadas dentro de uma penitenciária.",
        "director": "Frank Darabont",
        "poster_url": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
    },
    {
        "title": "The Godfather",
        "description": "A saga da família Corleone mostra os conflitos de poder, lealdade e crime organizado nos Estados Unidos.",
        "director": "Francis Ford Coppola",
        "poster_url": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
    },
    {
        "title": "The Dark Knight",
        "description": "Batman enfrenta o Coringa, um criminoso imprevisível que coloca Gotham City em completo caos.",
        "director": "Christopher Nolan",
        "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    },
    {
        "title": "Pulp Fiction",
        "description": "Histórias interligadas de crime, violência e humor ácido se cruzam em Los Angeles.",
        "director": "Quentin Tarantino",
        "poster_url": "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
    },
    {
        "title": "Fight Club",
        "description": "Um homem insatisfeito com sua vida conhece Tyler Durden e participa da criação de um clube secreto de luta.",
        "director": "David Fincher",
        "poster_url": "https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",
    },
    {
        "title": "Inception",
        "description": "Um ladrão especializado em invadir sonhos recebe a missão de plantar uma ideia na mente de um empresário.",
        "director": "Christopher Nolan",
        "poster_url": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg",
    },
    {
        "title": "Interstellar",
        "description": "Exploradores viajam através de um buraco de minhoca em busca de um novo lar para a humanidade.",
        "director": "Christopher Nolan",
        "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
    },
    {
        "title": "The Matrix",
        "description": "Um programador descobre que a realidade em que vive é uma simulação criada por máquinas.",
        "director": "The Wachowskis",
        "poster_url": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
    },
    {
        "title": "Forrest Gump",
        "description": "A vida de Forrest Gump atravessa décadas da história americana de forma emocionante e inesperada.",
        "director": "Robert Zemeckis",
        "poster_url": "https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
    },
    {
        "title": "Gladiator",
        "description": "Um general romano traído busca vingança contra o imperador que destruiu sua família e sua honra.",
        "director": "Ridley Scott",
        "poster_url": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
    },
    {
        "title": "Titanic",
        "description": "Um romance nasce a bordo do Titanic, enquanto o navio segue em direção ao seu trágico destino.",
        "director": "James Cameron",
        "poster_url": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
    },
    {
        "title": "Avatar",
        "description": "Em Pandora, um ex-fuzileiro participa de uma missão que o coloca entre humanos e o povo Na'vi.",
        "director": "James Cameron",
        "poster_url": "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg",
    },
    {
        "title": "Jurassic Park",
        "description": "Um parque com dinossauros clonados se transforma em desastre quando o sistema de segurança falha.",
        "director": "Steven Spielberg",
        "poster_url": "https://image.tmdb.org/t/p/w500/oU7Oq2kFAAlGqbU4VoAE36g4hoI.jpg",
    },
    {
        "title": "Back to the Future",
        "description": "Marty McFly viaja acidentalmente para o passado em um carro modificado como máquina do tempo.",
        "director": "Robert Zemeckis",
        "poster_url": "https://image.tmdb.org/t/p/w500/fNOH9f1aA7XRTzl1sAOx9iF553Q.jpg",
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "description": "Frodo inicia uma jornada para destruir um poderoso anel antes que ele caia nas mãos do mal.",
        "director": "Peter Jackson",
        "poster_url": "https://image.tmdb.org/t/p/w500/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg",
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "description": "A batalha final pela Terra-média se aproxima enquanto Frodo tenta concluir sua missão.",
        "director": "Peter Jackson",
        "poster_url": "https://image.tmdb.org/t/p/w500/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
    },
    {
        "title": "Star Wars: A New Hope",
        "description": "Luke Skywalker se junta à Aliança Rebelde para enfrentar o Império Galáctico.",
        "director": "George Lucas",
        "poster_url": "https://image.tmdb.org/t/p/w500/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",
    },
    {
        "title": "Star Wars: The Empire Strikes Back",
        "description": "Os rebeldes enfrentam o Império enquanto Luke Skywalker continua seu treinamento Jedi.",
        "director": "Irvin Kershner",
        "poster_url": "https://image.tmdb.org/t/p/w500/nNAeTmF4CtdSgMDplXTDPOpYzsX.jpg",
    },
    {
        "title": "Spirited Away",
        "description": "Uma menina entra em um mundo mágico de espíritos e precisa encontrar uma forma de salvar seus pais.",
        "director": "Hayao Miyazaki",
        "poster_url": "https://image.tmdb.org/t/p/w500/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
    },
    {
        "title": "Toy Story",
        "description": "Brinquedos ganham vida quando humanos não estão por perto e vivem uma aventura cheia de amizade.",
        "director": "John Lasseter",
        "poster_url": "https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg",
    },
]
created_movies = 0
updated_movies = 0
created_directors = 0

with transaction.atomic():
    for movie_data in movies_data:
        director, director_created = Director.objects.get_or_create(
            name=movie_data["director"]
        )
        if director_created:
            created_directors += 1
        movie, movie_created = Movie.objects.update_or_create(
            title=movie_data["title"],
            defaults={
                "description": movie_data["description"],
                "director": director,
                "poster_url": movie_data["poster_url"],
            }
        )
        if movie_created:
            created_movies += 1
        else:
            updated_movies += 1