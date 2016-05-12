# Using the command line

The command line provides a powerful way to interact with your computer using text
commands. It's especially useful if you ever want to work on a server, because for
a lot of servers it's the only way to interact with them.

My keys may differ a little from yours as I am working on a Mac. I welcome
amendments from users of other operating systems.

## Basic navigation

If you open a terminal window, you start out in your home directory. You can move
to a different folder using the `cd` command ('change directory'). If the folder
for this course is in your home directory, you can type `cd python-for-text-analysis`
to go there. Once you are in a folder, you can type `ls` to show everything that
is in the folder. Instead of the name of a directory, you can also type an entire
*path*, for example `cd Data/linguistlist/`. To go from a folder to its parent
folder, type `cd ..`. This also works with multiple directories, for example
`cd ../../..` goes three levels up. If you want to see the folder you are in,
use `open .`. This will open the Finder application.

## Examining files

* Use `cat puppies.txt` to show all the contents of `puppies.txt`.
* Use `head puppies.txt` to show the first 10 lines.
* Use `tail puppies.txt` to show the last couple of lines.
* Use `wc puppies.txt` to count the number of words in `puppies.txt`.

Many commands also have **flags**: additional arguments that modify the behavior
of the command. For example, you can specify the number of lines that `head` and
`tail` shows by using the flag `-NUMBER`. For example: `head -20 puppies.txt`.
For the `wc`-command, it is useful to know the `-l` flag. If you use this flag,
you get the number of lines instead of the number of words. For example:
`wc -l puppies.txt`.

## Creating and removing files and folders

* To create a new file, for example 'puppies.txt', type `touch puppies.txt`.
* To create a new folder, for example one that is named 'puppies', type `mkdir puppies`.
* To remove the file, type `rm puppies.txt`.
* To remove the folder, type `rm -r puppies`.

Removing also works with *wildcards*. Here is an example:

```bash
# Create number of new files:
touch puppies1.txt
touch puppies2.txt
touch puppies3.txt
touch puppies4.txt
touch puppies5.txt

# Remove all puppies files.
rm puppies*.txt
```

## Editing files from the command line

One of the simplest command line editors is `nano`. You can open it using the
`nano` command or, if you want to open a specific file, specify the filename.
For example, `nano puppies.txt` opens `puppies.txt` and allows you to edit the
file. You can navigate through the file as follows.

* Use the arrow keys to move through the text.
* To scroll up, use `ctrl+Y`, to scroll down, use `ctrl+V`.
* To save the file, press `ctrl+O`

## Using Python

* Use `python` to open the interactive console. Escape using `exit()`.
* Use `ipython notebook` to start the notebook application.
* Use `python puppies.py` to run the script called `puppies.py`.
* Use `python puppies.py &` to run the script called `puppies.py` in the background.

If you want to quit a running script or notebook application, type `ctrl+c`.

## Monitoring your scripts

If you have a script running, you can open another terminal and type `top`, which
will display a table of active processes. This table shows the CPU and memory usage
of your script. It also shows you the `pid` or 'process ID' of every running process.
If you want to stop a script running in the background, type `kill`, followed by
the PID number.
