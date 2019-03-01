1.Project Description:
Name: Game of Othello
Author: Mutian Xu, Jing Liao, Qiqi Pan
Version:1.0


2.Project Function:
Initially, the input is a vector of 64 symbols {0,W,B} defining the starting board;
The computer moves first;
Output after each computers move is a pair (i,j) that defines the computers move on the 8x8 board;
After computers move, it should expect as input a pair (x,y) that defines opposing players move until the game is over (current player cannot move).


3.Running Method: 
Follow the "Python Download and Intallation Instructions" to download Python;
Follow the "Environment variables" to create the running environment for Python;
Copy the file ¡°UCI_AI_Chaser¡±to the project file (shown in your IDE) of your Python IDE (suggestion: PyCharm;click the"download PyCharm" to get the download link); 
Open Python IDE;
Open the project file ¡°UCI_AI_Chaser¡±;
You will see several python files;

If you want to check the Result 1 in the report, you should use right mouse to click othello.py  and click ¡®run¡¯ firstly. The Othello.py is a game between two AIplayers;

The check method: Change the last number of sentence48 and sentence 51 in player.py to respectively fit the number of the first 2 columns in the result graph of the report.

If you want to check the Result 2 in the report, you should right mouse click othello_2.py  and click ¡®run¡¯ firstly. 

The check method:
a. Play the game with AI according to the instruction of the game: input e3 and then e2.
b. Change the last number of sentence48 in player_2.py to 5, which fits the number of the second depth in the Result 2 of the report.
c. Play the game with AI according to the instruction of the game: input is same as step a.


4.For the developer:
You can follow the explanation of the code to know how the code work.

Split into four files: board.py, player.py, ai.py, othello.py. Make the whole structure clearer, more versatile and easier to maintain.

The Board class is used for creating rules such as get_legal_actions() and define some basic method such as move() so that the other class can directly inherit the methods of this class to run. In this way, it will be easier to maintain and develop. 

The level of AI is related to the recursion depth of minimax and the evaluation function. Based on this, I put the minimax and evaluation functions in the AI class.

AIPlayer uses multiple inheritance, inheriting two classes of Player and AI.

In the Game class, the part of the original run function that generates two players is proposed and written as a function make_two_players, which makes the run function structure clearer.

Every class and object are named intuitively so that you can easily understand the function of them.


5. Acknowledgement:
Thanks to Dr. Kalev Kask for the instruction of the course, CS271: Introduction to Artificial Intelligence, in Fall 2018;
Thanks to all the people who give our team suggestions for the project.

