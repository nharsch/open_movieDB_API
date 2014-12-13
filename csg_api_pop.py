
import requests
import csv

s = requests.session()

csv_name = "test_sked.csv"

# params = {"t" : "The Dark Knight"}
# r = s.get("http://www.omdbapi.com/", params=params)
# r.status_code

# r.json()
# r_dict = r.json()
# print r_dict


def title_exact_search(title):
    params = {"t" : title}
    r = s.get("http://www.omdbapi.com/", params=params)
    return r.json()


with open(csv_name, 'rU') as csv_file:
    csv_reader = csv.reader(csv_file)
    movie_list = [row[0] for row in csv_reader] #make a list of the first elements of the CSV



dicter = [{'Title' : movie, 'Actors' : title_exact_search(movie).get('Actors', "not found")} for movie in movie_list]

print dicter

with open(csv_name[:-4]+"_output.csv", 'w') as csvfile:
	fieldnames = ['Title', 'Actors']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for row in dicter:
		writer.writerow(row)





