# Textify
Python module for a text based graphical engine. 

# Rendering
The rendering can be done on an average console, this module does not need helping modules/packages.

# Why should you use this

It may be to decrease processing - power for simulations, style your game as console based game giving it a distinguished look, or give a console based software/tool a beautiful ascii look rather than boring text, or just because it is so easy to use and the many possibilities that can be done with these simple functions that would teach a beginner at programming or teach how programming works for simulations/games.

There are wild possibilities that can be done with this compared to other rendering modules of python. This module has ease of use, compatibility with most computers and is extremely efficient in its processing.

The only limit to this engine is imagination

# How do I download this?

Download through this command - 
`git clone https://github.com/null-Exception1/Textify.git`
Or simply click on CODE on homepage, and click on DOWNLOAD ZIP

No extra modules are required (advantage) so you should be up and running!

# Use?
Import the module by putting the python file in the same directory as your project : 

```from textify import Canvas```

Create a canvas object by doing the following. This will create your canvas as a grid of a character/symbol given in the 3rd arg.

First 2 args stand for width and height respectively.

```canvas = Canvas(10,10,'#')```

We recommend adding a space behind the character for most cases. Like this - 

```canvas = Canvas(10,10,' #')```


The entire grid can be accessed by `canvas.display` which return a 1D array consisting of the grid characters, But we don't need this.

Display a rectangle :

```



