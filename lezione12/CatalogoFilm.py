# Classe:
# - MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.
class MovieCatalog:

    def __init__(self) -> None:

        self.movies_by_director: dict[str:list[str]] = dict()
        


#     Metodi:
#     - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
#         Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    def add_movie(self, director_name, movies):

        if director_name in self.movies_by_director:
            for movie in movies:
                if movie not in self.movies_by_director[director_name]:
                    self.movies_by_director[director_name].append(movie)
        
        else:
            self.movies_by_director[director_name] = movies.copy()


#     - remove_movie(director_name, movie_name): 
#         Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.
    
    def remove_movie(self, director_name, movie_name):

        if director_name in self.movies_by_director:
            if movie_name in self.movies_by_director[director_name]:
                self.movies_by_director[director_name].remove(movie_name)
        
            if not bool(self.movies_by_director[director_name]):
                del self.movies_by_director[director_name]


#     - list_directors(): Elenca tutti i registi presenti nel catalogo.

    def list_directors(self) -> str:
        
        ret = [key for key in self.movies_by_director]
        return ret
        

#     - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    def get_movies_by_director(self, director_name):
        if director_name in self.movies_by_director:
            return self.movies_by_director[director_name]


#     - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
#         Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata 
#         o un messaggio di errore se nessun film contiene la parola cercata nel titolo.

    def search_movies_by_title(self, title):

        searched_movies: dict[str:list[str]] = dict()
        for key, value in self.movies_by_director.items():
            for title1 in value:
                if title in title1:
                    if key in searched_movies:
                        searched_movies[key].append(title1)
                    else:
                        searched_movies[key] = [title1]

        if bool(searched_movies):
            ret = ""
            for key, value in searched_movies.items():
                ret += f"{key}: {value}" 
            return ret
        
        print("Title not present in movies")


    def __str__(self) -> str:

        ret = ""
        for key, value in self.movies_by_director.items():
            ret += f"{key}: {value}\n" 
        return ret


moovie = MovieCatalog()
print(moovie)
moovie.add_movie("Ciro", ["aa","ab","bc"])
moovie.add_movie("Scem", ["dd"])
print(moovie)
print(moovie.get_movies_by_director("Giacomo"))
print(moovie.get_movies_by_director("Ciro"))
moovie.remove_movie("Giacomo","m")
moovie.remove_movie("Ciro","ab")
print(moovie.list_directors())
moovie.add_movie("Ciro", ["ad"])
print(moovie.get_movies_by_director("Giacomo"))
print(moovie.get_movies_by_director("Ciro"))
print(moovie.search_movies_by_title("a"))


