# getrepos.py
Simple python script to get info from all Github repos from a specified user.


### Use

```python getrepos.py <user>```

### Example

Input:

```python getrepos.py ManuRC2```

Output:

```
https://github.com/ManuRC2/cuatroenlinea
 None

https://github.com/ManuRC2/getrepos
 Simple python script to get info from all Github repos from a specified user

https://github.com/ManuRC2/manurc2.github.io
 Landing page
 ```
 
## Recomendation
The purpouse of this script is to be built into an executable and placed in the path, so it can be easily usad at all times.

To do this on Windows, you can install [PyInstaller](https://pyinstaller.org/en/stable/) by running `pip install pyinstaller` and then `pyinstaller getrepos.py`. 

This will create a single executable file from your script, along with any necessary dependencies. The executable will be placed in a directory called "dist" in the same directory as your script. You can then add the path of the executable to the Path variable.
