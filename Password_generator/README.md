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
