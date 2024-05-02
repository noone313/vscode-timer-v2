## Automatic VSCode Timer Version 2
# Now the Windows Task Manager senses and triggers the counter if VsCode is running, and stops the counter if it senses that VsCode has been closed

The purpose of this program is to automate several tasks upon execution:

1. **Opening Visual Studio Code Editor**: PyAutoGUI library is utilized to automatically open the Visual Studio Code editor upon program startup. This allows users to swiftly access the editor without manually searching for it and opening it.

2. **Displaying a Timer Inside the Editor**: Once the editor is launched, a timer is initiated within the program, displaying the time the user spends inside the editor. This timer is continuously updated to show the actual time the user spends inside the editor.

3. **Stopping the Timer and Printing Final Time**: The program also includes a button to stop the timer when the user finishes using the editor. Clicking on this button stops the timer and prints the final time spent by the user inside the editor.

By implementing this functionality, users can conveniently start using the text editor directly without the need to manually open it. Additionally, they can monitor the time they spend inside the editor accurately and stop the timer when they finish.

