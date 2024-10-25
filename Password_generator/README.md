I will make an excellent little password generator here. I plan to use this to create passwords for all future and current accounts.

Just set up my code editor to work with Github!

10/24/2024:
I created the file; I've been busy with schoolwork, but I will try to figure out how to use the Tkinter library to have an actual GUI.

I'm adding many inputs to the file. I just spent a little bit of time learning how Tkinter actually works. With some trial and error, I got it to function how I wanted. 
I also completely overlooked the .get() function needed to pull the value from the inputs.

At first, I had an if-else statement to check if at least one character type was selected, but I found that Tkinter has a progress bar, and I want to add that to my file just because. So, I just created an if statement to see if no characters were selected, and if none were, it just returns.
Currently, I'm just printing to the console because I haven't figured out how to get a message to pop up or for a label to change.

importing pyperclip to make it copy straight to clipboard
While testing this, I realized this doesn't guarantee that each checked item will be in the phrase. So, I will have it check the password to see if it contains at least one of each character type selected.

Made a function to validate it, then made a loop that continues until a valid password is generated.

I also found the password was copied without pressing the copy password function.

After some searching, I found that the "command=" actually automatically runs the command because it expects a function, not the result of a function call. So, to counter this, I wrapped it in an anonymous function. 


Added the .geometry() function to change the window size and its position
added some math to center it as well


I'm trying to style the window to be more appealing to the User


I was trying to use the .grid() function but kept getting errors. I found that I can not use both the pack and grid functions on the same widgets. I should read the documentation more.

After an annoying process of making frames, changing packs to grids, and converting some grids back to packs, I think I got it to a decent form. The colors are still a little wacky, but I got it looking more styled than before. Tkinter is new to me, so I'm glad with the progress I've made.

It's technically the next day now, currently 12:50 AM, so I'm calling it a night. I will finish this up tomorrow and possibly add some new features like those listed below:
1. Option for passphrase rather than password
2. some sort of storage or logging of the password for safe keeping
3. encryption of the password if doing the feature above
4. ...more...

10/25/2024:
Finished up some of the color stuff on the application. Gave it a matrix color. Jet Black and Neon Green.

Adding a label below the buttons to change to the Password when its generated so I can see it on the app instead of the terminal or have to paste it somewhere to see.
Got that working!

Now, I want to add a database to this and turn it into my own little password manager.
I'll be using SQLite, which I am also partially new to, but trial and error should help me figure this out. 
I will also be encrypting the data as well!


I'm currently typing a lot of stuff without checking if it's working or not, so I'm either being awesome or about to have to delete a lot of wasted work.

I'm making this SQL database off a quick tutorial and some occasional stack overflow. I'm learning stuff as I go and hoping I'm not breaking anything.

Going to try something called a Treeview from tkinter. Hopefully the program will open a new window to access the saved passwords.

I ACTUALLY GOT THIS TO WORK. I haveen't had something go first try like that in this file for a little so this was nice. I just need to add a prompt when I click the Save password button to enter the website, as well as the username.


I added some prompt to ask for the website name as well as a username. If left blank if asks if they want to keep it blank, if not it goes back. They can then enter everything. It says it has been saved in a info message as well. I love how well this is coming out to be!
