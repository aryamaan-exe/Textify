# Textify
Python module for a text based graphical engine. 

## Rendering
The rendering can be done on a console; this module does not need helper modules/packages.

## Why Textify?

Textify is great for decreasing processing-power for simulations. You can style your game as console based game by giving it a unique look, or give a console-based software/tool a beautiful ascii look rather than text. It is also easy to use. There are endless possibilities for this module and it is also a great introduction to concepts in Pygame, Processing, Pyglet etc. such as canvases and shape functions.

Compared to other rendering modules in Python, there are many things you can do with this library. This module is incredibly bare-bones, holds compatibility with all computers and is extremely efficient in its processing.

The only limit to this engine is your imagination!

## Installation

Textify can be installed using [Git](https://git-scm.com/)  
`git clone https://github.com/null-Exception1/Textify.git`

Or simply click on `Code` on this repository, and click on `Download ZIP`.

No extra modules are required, so you should be up and running!

## Usage

Import the module by putting the Python file in the same directory as your project: 

```from textify import Canvas```

Create a canvas object by doing the following. This will create your canvas as a grid of a characters/symbols given in the 3rd arg.

First 2 args stand for width and height respectively.

```py
canvas = Canvas(10,10,'#')
```

We recommend adding a space behind the character for most cases. Like this - 

```py
canvas = Canvas(width,height,' #')
canvas.render()
```

You can see `examples.py` for more examples.

**NOTE:** We recommend you do `os.system('cls')` to clear the console, or if you are rendering the canvas at a constant framerate we recommend you do `sys.stdout.write('\n'*50+canvas.render_val())`

## Discord Bot Implementation

This library is also available in the form of a Discord bot (@Textify#0494, ID 864771090593349632).

### Running an instance of the Discord bot

It is assumed that you have installed Python.  
- Run `git clone https://github.com/aryamaan-exe/textify-bot.git`
- Run `pip install discord.py`
- Run `pip install dnspython` and `pip install pymongo`
- Create a bot application on Discord ([how?](https://www.wikihow.com/Create-a-Bot-in-Discord#Creating-the-Bot-on-Discord) section 2)
- Copy the token and paste it into `tokens.json` in the `bot` section.
- Create a MongoDB cluster ([how?](https://docs.atlas.mongodb.com/tutorial/create-new-cluster/)) and paste the connection string into `tokens.json` in the `mongo` section.
- Run `python main.py`.
- In case of any errors, please open an issue on the [bot repo](https://github.com/aryamaan-exe/textify-bot).

