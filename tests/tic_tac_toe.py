from askui import VisionAgent


def test_my_test(agent: VisionAgent):
    agent.act("""

    

    You are playing a Tic Tac Toe game as player X. Follow these strategic rules:


    1. First Move Strategy:

       - Always take the center if available

       - If center is taken, take a corner


    2. Winning Strategy (in priority order):

       a) Immediate Win:

          - Check all rows, columns, and diagonals for two X's

          - Complete any line with two X's to win

       

       b) Block Opponent:

          - Scan for any two O's in a row/column/diagonal

          - Block immediately to prevent opponent's win

       

       c) Create Winning Opportunities:

          - Look for cells that create multiple winning paths

          - Prioritize moves that create forks (two ways to win)

          - If no fork possible, create a single winning path

       

       d) Defensive Positioning:

          - If opponent has a corner, take the opposite corner

          - If opponent has two corners, take the middle of any side

          - Prevent opponent from creating forks


    3. Game Flow:

       - After each move, wait for opponent's move

       - Verify the opponent's move is complete before proceeding

       - If you lose click in the center of the board to reset the game.


    4. Error Handling:

       - If any popups appear, close them immediately

       - If the game freezes, refresh the page

       - If you can't make a move, try clicking the cell again


    5. Visual Verification:

       - Before each move, really confirm the cell is empty

       - After each move, really verify your X appears correctly

       - Check that the opponent's O appears before your next move


    Continue playing until explicitly stopped. Focus on winning while maintaining a strong defensive position.

    """)
