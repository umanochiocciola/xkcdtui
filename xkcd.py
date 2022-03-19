#! /bin/python3

from bs4 import BeautifulSoup
import os
from sys import argv
from random import randint

INTERVAL_RANGE = 5
IMAGE_VIEWER = "feh" # change to any image viewer that accepts url inputs such as xviewer


def main():
	try: preselected = int(argv[1])
	except: preselected = ''

	comics   = getComics()


	if preselected.lower() == 'r':
		preselected = randint(0, len(comics))
		print("comic number\33[1m", preselected, "\33[0;37mhas been selected for you!")


	if preselected != '':
		display(comics[preselected]["url"])
		return

	while 1:
		selected = selection(comics)
		display(selected)
		os.system("clear")


def getComics():

	debug("retireving archive")
	with os.popen("curl -s https://xkcd.com/archive/") as output:
		html = output.read()

	place("OK")


	soup = BeautifulSoup(html, 'html.parser')


	debug("parsing comics list")
	comics = []
	for i in soup.find_all('a'):
		if i.get('title') == None: # not a comic
			continue

		comics.append({"url": i.get("href")})
		comics[-1]["text"] = f"({i.get('title')})   \33[1;37m{i.get_text()}\33[0;37m"
	place("OK")

	return comics



def selection(comics):
	interval = [0, INTERVAL_RANGE]

	print("\33[1;33m+== XKCD ==+")
	print("|Q to quit\n|ENTER to list more\n|number to select\n|\n|use \33[32mxkcd <num>\33[37m to skip selection phase\n|use \33[32mxkcd r\33[37m to display a random chosen comic\n+==------==+\33[0;37m")
	while 1:
		for i in range(interval[0], interval[1]):
			print(f"[{i}]", comics[i]["text"])

		cmd = input()
		if cmd == "":
			interval = [interval[1], interval[1]+INTERVAL_RANGE]

		elif cmd.lower() == "q":
			quit()

		else:
			try: return comics[int(cmd)]["url"]
			except: print("invalid input")



def display(url):
	#print(url)

	debug("retireving page")
	with os.popen("curl -s https://xkcd.com"+url) as output:
		html = output.read()
	place("OK")

	soup = BeautifulSoup(html, 'html.parser')

	url = 'https:' + soup.find_all('img')[2].get('src')

	debug("displaying comic")
	os.system(IMAGE_VIEWER+" "+url)
	place("OK")





def place(status):
    print('\33[1;32m'+status+'\33[0;37m]')

def debug(task):
    print('\33[0;37m[ ]', task, end='\r[')



if __name__ == '__main__':
	main()
