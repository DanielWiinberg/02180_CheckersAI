# 02180_CheckersAI

To install:
    1. create virtual environment
    3. start the virtual environment then: pip install -r requirements.txt


Set the conditions to play the game:
    1. White will be always an AI agent, but Red can be configure as IA or as Human:  
        RED_PLAYER = <b>'AI'/'HUMAN'</b> <i>Line 21 main.py</i>
    2. Set the algorithms used by the AI agents 
        WHITE_PLAYER_ALGORITHM = <b>'minimax'/'minimax_graph'/'alpha_beta'</b> <i>Line 25 main.py</i>
        RED_PLAYER_ALGORITHM = <b>'minimax'/'minimax_graph'/'alpha_beta'</b> <i>Line 26 main.py</i>
    3. configure the depht limit for each player: 
        RECURSION_LIMIT_WHITE = <b>0-5+</b> <i>Line 29 main.py</i>
        RECURSION_LIMIT_RED = <b>0-5+</b> <i>Line 30 main.py</i>

Execute: <i>main.py</i>