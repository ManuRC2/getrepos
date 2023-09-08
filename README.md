# getrepos.py
Simple python script to get info from all Github repos from a specified user.


### Use

```python getrepos.py <user>```

### Example

Input:

```python getrepos.py ManuRC2```

Output:

```
╔══╡ManuRC2
║
╠╦═╡https://github.com/ManuRC2/clickergame
║╚═╡dumb clicker game made in python with tkinter
║
╠╦═╡https://github.com/ManuRC2/getrepos
║╚═╡Simple python script to get info from all Github repos from a specified user
║
╠╦═╡https://github.com/ManuRC2/racket
║╚═╡Practicas de Racket de la LCC
║
╚╦═╡https://github.com/ManuRC2/repositorio-dagos
 ╚═╡ 3 simples commits modificando un archivo.
 ```
 
## Installation
The purpouse of this script is to be built into an executable and placed in the path, so it can be easily used at any time.

On Windows, this can be done by running the `installer` file. 

This will install the project's dependencies and then create an executable file, located in the "dist" folder.
The installer will ask if you want to add the directory to the PATH variable, but it does not always work due to privilege issues, so it's better to just add it manually.

## Sorry
This was developed and made for Windows only. If you want a Linux compatible alternative, be sure to check out [this project](https://github.com/SantiagoCalligari/gitget) made by a friend of mine.
