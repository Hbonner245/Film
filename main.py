#############################
## This demo will ues:
## *Sequence
## *Selection
## *Iteration
## *I/O - text files
## February 2022
## Written by: Helena Bonner
###########################


import time

# A while loop will keep running until the condition has changed in this intance false 
while True:	
  time.sleep(2)
  user_choice = input("""\nPlease select from the following options:"
1. - Display all films
2. - Display all (and only) comedy films
3. - Display all (and only )action films
4. - Display all (and only) films with a duration of more than an hour
5. - Display all words containing a keyword
6. - Add film
7. - Exit                      
""")
  
  print("")
  if user_choice == "1":
		#opens film_file in read mode
    film_file = open("films.txt", "r")
		#reds the data stored in the film file 
    films = film_file.read()
		#outputs the content of the film file
    print(f"{films}")
		#closes the connection between the film file which results in RAM being freed up
    film_file.close()
    
  elif user_choice == "2":
    film_file = open("films.txt", "r")
    for row in film_file:
      # will split each element eveything it sees a comma and assigns it to a variable. 
        field = row.split(",")
        film_id = field[0]
        title = field[1]
        year_of_release = field[2]
        rating = field[3]
        duration = int(field[4])
        genre = field[5]
				# gets rid of the invisible \n which will normally put it on a new lines
        last_char = len(genre) - 1
        genre = genre[0:last_char]
        if genre == "Comedy":
            print(film_id, title, year_of_release, rating, genre, duration)
		# closes the connection between the main file and the text file which frees up RAM
    film_file.close()
		
  #if the user has input option 3 then the code below will run. 
  elif user_choice == "3":
		#opens the connection between the main program and the file
    film_file = open("films.txt", "r")
    for row in film_file:
			#will split each row where ever it sees a comma
        field = row.split(",")
				#each element in the list is given an index and a list in python is 0 based indexed
        film_id = field[0]
        title = field[1]
        year_of_release = field[2]
        rating = field[3]
        duration = int(field[4])
        genre = field[5]
				#gets rid of \n
        last_char = len(genre) - 1
        genre = genre[0:last_char]
				#will look for action in each line of thee file then will output it so the user can see what films have the genre action
        if genre == "Action":
            print(film_id, title, year_of_release, rating, genre, duration)
						#closes connection toRAM
    film_file.close()

  elif user_choice == "4":
    # Makes connection to films file in read mode meaning nothing can be changed in the file
    film_file = open("films.txt", "r")
    for row in film_file:
        field = row.split(",")
        film_id = field[0]
        title = field[1]
        year_of_release = field[2]
        rating = field[3]
        duration = int(field[4])
        genre = field[5]
				#line 74 and 75 get rid of the invisible /n which we dont see so it is put on one line. 
        last_char = len(genre) - 1
        genre = genre[0:last_char]
        if duration > 60: 
            print(film_id, title, year_of_release, rating, genre, duration)
    # Closes connection to RAM, freeing it up. 
    film_file.close()
    
#the statement will allow the user to to search for films that have the keyword in
  elif user_choice == "5":
		# asks user to enter keyword
    keyword = input("Please enter a keyword")
		#opens the connection to the file but it will only open it in read mode
    film_file = open("films.txt", "r")
    for row in film_file:
        field = row.split(",")
        film_id = field[0]
        title = field[1]
        year_of_release = field[2]
        rating = field[3]
        duration = int(field[4])
        genre = field[5]
        last_char = len(genre) - 1
        genre = genre[0:last_char]
				#checks if the keyword that the user has entered is in title and will output it
        if keyword in title:
				#output to the screen for the user to see
          print(film_id, title, year_of_release, rating, genre, duration)
						#will close the connection between the file and the main program which will free up RAM
    film_file.close()

  #allows for user to add to film
  elif user_choice == "6":
    #opens the film file in append mode so the user can add a film without overwriting the text which is already in there
    film_file = open("film.txt", "a")
    film_id = input("please enter film id")
    title =  input("Please enter film title")
    year_of_release = input("Please enter the year the film was released")
    rating = input("Please enter film rating")
    duration = input("Pelase enter duration of film")
    genre = input("Please enter genre of film")
    film_file.write(f"{film_id}, {title}, {year_of_release}, {rating}, {genre}, {duration}")
    film_file.close()

  elif user_choice == "7":
    print("you are all finished")
    # Break out of loop 
    break
  