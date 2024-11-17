Speed Typing Test
Test your typing speed and accuracy with this Speed Typing Test! This program allows you to measure your typing skills while providing real-time feedback on your typing speed in Words Per Minute (WPM).

Features
Real-Time WPM Calculation: See your WPM updated as you type.
Error Highlighting: Correctly typed characters are shown in green, while incorrect characters are displayed in red.
Backspace Support: Fix mistakes as you type with backspace.
Customizable Text: Use your own text file to test your typing skills.
Restart or Quit: Easily retry the test or exit with a single key press.
Tech Stack
Python 3.6+
Curses Library: For terminal-based UI.
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/speed-typing-test.git
cd speed-typing-test
2. Install Python
Make sure you have Python 3.6 or above installed. You can download it here.

3. Run the Program
Run the program directly using Python:

bash
Copy code
python typing_test.py
How to Use
Run the program to see the welcome screen.
Press any key to begin the typing test.
Start typing the displayed text.
Correct characters will appear in green.
Incorrect characters will appear in red.
Press Backspace to delete any incorrect characters.
Press ESC to quit at any point.
Customizing the Test
Changing the Text
You can customize the text used in the test:

Open the text.txt file in the project directory.
Add, edit, or replace the lines of text.
Each line represents a potential typing test.
The program will randomly select one line from the file during the test.
Example text.txt:

csharp
Copy code
This is a sample typing test line.
Customize this file with your own content.
Improve your typing skills with this speed test.
How It Works
The program displays a random line of text from text.txt.
As you type:
Your WPM is calculated in real time.
Errors are highlighted immediately for correction.
After completing the text:
Your final WPM is displayed.
You can choose to retry or quit the program.
Keyboard Controls
Typing: Type the displayed text to proceed.
Backspace: Delete the last character to fix mistakes.
ESC: Exit the program at any time.
