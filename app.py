movies = []


def add():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show():
    for movie in movies:
        print(f"Title = {movie['title']}")
        print(f"Director = {movie['director']}")
        print(f"Year = {movie['year']}")


def find():
    search_movie = input("Enter your tittle movie: ")
    for movie in movies:
        if movie['title'] == search_movie:
            print(f"Title = {movie['title']}")
            print(f"Director = {movie['director']}")
            print(f"Year = {movie['year']}")
            break
    else:
        print("Movie is not found")


user_options = {
    "a": add,
    "l": show,
    "f": find
}

selection = \
    input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f to find your movie by title, or 'q' to quit: ")
while selection != 'q':
    if selection in user_options:
        selected_function = user_options[selection]
        selected_function()
    else:
        print("Unknown command, please try again")
    selection = input(
        "\nEnter 'a' to add a movie, 'l' to see your movies, 'f to find your movie by title, or 'q' to quit: ")


