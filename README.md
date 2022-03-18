# xkcdtui
a Terminal User Interface tool to enjoy XKCD comics from your comfy terminal

## Installation
just run 
```./install.sh```
it'll get you sorted!

## Usage
```
xkcd [num/'r']
```
with no arguments, will run a selection menu
if an number is passed, xkcd will display the numth comic in the archive list (descending cronological order)<br>
if 'r' is passed, xkcd will display a random comic

## Requiremets
python 3.8+
An image viewer that supports url arguments. Default is ```feh```. Edit xkcd.py before installing to change IMAGE_VIEWER to your preferred one.
