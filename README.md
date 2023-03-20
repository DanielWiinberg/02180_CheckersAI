To install:

1. create virtual environment
2. start the virtual environment then: pip install -r requirements.txt

Set the conditions to play the game:

1. White will be always an AI agent, but Red can be configure as IA or as Human:

		RED_PLAYER = <'AI'/'HUMAN'>  Line 21 main.py

2. Set the algorithms used by the AI agents

		WHITE_PLAYER_ALGORITHM = <'minimax'/'minimax_graph'/'alpha_beta'> Line 25 main.py
		RED_PLAYER_ALGORITHM = <'minimax'/'minimax_graph'/'alpha_beta'>  Line 26 main.py

3. configure the depht limit for each player:

		RECURSION_LIMIT_WHITE = <0-5+>  Line 29 main.py
		RECURSION_LIMIT_RED = <0-5+>  Line 30 main.py

Execute: 

	main.py