from mal import *
try:
	inp = input("Enter Anime name:\n")
	search = AnimeSearch(inp)
	name = search.results[0].title
	scor = search.results[0].score
	image = search.results[0].image_url
	link = search.results[0].url
	epi = search.results[0].episodes
	typ = search.results[0].type
	brief = search.results[0].synopsis
	print(name)
	print(scor)
	print("Image: ",image)
	print("Url: ",link)
	print("Episodes: ",epi)
	print("Type: ",typ)
	print("Synopsis: ",brief)
except ValueError:
	print("Invalid Search!!")


