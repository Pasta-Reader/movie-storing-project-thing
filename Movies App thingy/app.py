#movie storing project thing (v1.1) (spelling mistakes and ui later versions)

'''
note: project problems:
1. doesnt save the movies after closing and opening.(maybe technical stuff)
2. file is there but it over writes it need to find a way to save it.
3. FIXED IT!!!!! LETSS GOOOO!!!! PUTTING IT IN A SEPREATE DATABASE WAS THE RIGHT CALL!!
4. UI IS THE NEXT STEP!!


'''
import tkinter

from movie_database import MoviesAnimeDatabase #the living legend thank you mr. coddy.tech!!!

db = MoviesAnimeDatabase()


#collects name and checks status of movie, also returns it
movies = db.load() #feel like saying womp womp to the old code if it works.
#gives movie key-value pairs
def all_movie_and_status(movie_dict):
    if not movie_dict:  # Cleaner way to check if dictionary is empty
        print("Movie dictionary is empty!")
        return
    
    for i, (key, value) in enumerate(movie_dict.items(), start=1):
        print(f"{i}. Movie name: {key} Status: {value}")
    
    return ""

#adds movies and sets status
def add_movie_and_status(movie_dict, movie, status=False):
    if movie in movie_dict.keys():
        return f"Movie already there! Movie: {movie} Status: {status}"
    else:
        movie_dict[movie] = status
        return "Movie added successfully!"

#updates the status of the movie
def movie_status_updater(movie_dict, movie, status=False):
    movie_dict[movie] = status
    return f"Status updated successfully to {status} for movie/series {movie}"

#deletes a key-value pair from the dictionary
def delete_movie(movie_dict, movie):
    if movie in movie_dict:
        del movie_dict[movie]
        return f"{movie} successfly deleted from the dictionary!"
    else:
        return f"{movie} not found!"

#for finding a perticular movie and status
def specific_movie(movie_dict, movie):
    if movie in movie_dict:
        return f"{movie} in the dictionary, movie status: {movie_dict[movie]}"
    else:
        return f"{movie} not found!"

#while loop/ main ui
while True:
    #prints all the boring stuff for usablility bruh
    print()
    print("1. Veiw all movie and their status")
    print("2. Add movie and movie status")
    print("3. Remove movie and movie status")
    print("4. Find a specific movie")
    print("5. Update movie status")
    print("6. Quit")
    print()
    user_input = int(input("Choose your option: "))
    if user_input == 1:
        all_movie_and_status(movies)
    elif user_input == 2:
        movie_name = input("Enter the movie name: ").strip().lower()
        user_status = input("Have you watched the movie (y/n): ").strip().lower()
        if user_status == 'y':
            movie_status = True
            print(add_movie_and_status(movies, movie_name, movie_status))
        elif user_status == 'n':
            movie_status = False
            print(add_movie_and_status(movies, movie_name, movie_status))
        else:
            print(add_movie_and_status(movies, movie_name))
        #json part
        db.save(movies)
    elif user_input == 3:
        movie_name_2b_deleted = input("Enter the movie name which you want to delete: ").strip().lower()
        print(delete_movie(movies, movie_name_2b_deleted))
        #json part
        db.save(movies)
    elif user_input == 4:
        searching_movie = input("Enter the movie which you are searching for: ").strip().lower()
        print(specific_movie(movies, searching_movie))
    elif user_input == 5:
        movie_status_name = input("Enter the movie name whose status needs to be updated: ").strip().lower()
        user_updated_status = input("Enter the updated status of the movie. (y/n): ").strip().lower()
        if movie_status_name in movies:
            if user_updated_status == "y":
                new_movie_status = True
                print(movie_status_updater(movies, movie_status_name, new_movie_status))
            elif user_updated_status == "n":
                new_movie_status = False
                print(movie_status_updater(movies, movie_status_name, new_movie_status))
            else:
                print(movie_status_updater(movies, movie_status_name))
        else:
            print("Movie not found")
        #json part
        db.save(movies)
    elif user_input == 6:
        break
    else:
        continue
