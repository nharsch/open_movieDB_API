
import requests
import csv
from sys import argv

s = requests.session() #create a requests session

if __name__ == '__main__':
	script, csv_name = argv #takes csv_name as command line arg

# params = {"t" : "The Dark Knight"}
# r = s.get("http://www.omdbapi.com/", params=params)
# r.status_code

# r.json()
# r_dict = r.json()
# print r_dict


def title_exact_search(title):
	'''
	return the OPENDB metadata for title 
	finds exact title match (case insensitive)
	'''
    params = {"t" : title} #t parameter finds exact match
    r = s.get("http://www.omdbapi.com/", params=params) #send a request to OPENDB api
    return r.json() #return the JSON response


#create a python list of movies from the CSV, 
#assumes movies are at 1st column of every row
with open(csv_name, 'rU') as csv_file:
    csv_reader = csv.reader(csv_file)
    movie_list = [row[0] for row in csv_reader] #make a list of the first elements of the CSV

def list_processor(movie_list):
	'''
	performs lookup on list of movies
	returns list of dicts as response
	'''
	dicter = []
	for movie in movie_list:
		metadata = title_exact_search(movie)
		dicter.append({'Title' : movie, 
						'Year' : metadata.get('Year', "not found"),
						'Actors' : metadata.get('Actors', "not found"),
						'Director' : metadata.get('Director', "not found"),
						})
	return dicter

dicter = list_processor(movie_list) #create a dicter of responses for writing
# print dicter

with open(csv_name[:-4]+"_OPENDB_metadata.csv", 'w') as csvfile: #prep output file
	fieldnames = ['Title', 'Year', 'Actors', 'Director'] #explicitly declare headers
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #init writer
	writer.writeheader() #write header row
	#write all response rows
	for row in dicter:
		writer.writerow(row)





