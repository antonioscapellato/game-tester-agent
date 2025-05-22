from askui import VisionAgent


def test_my_test(agent: VisionAgent):
    agent.act("""

    You are playing Slither.io as player "Agent". Follow these strategic rules:

    1. Basic Movement:
       - Move your snake by controlling the mouse cursor position
       - The snake will follow the cursor with a slight delay
       - Keep movements smooth and predictable

    2. Food Collection Strategy:
       - Prioritize eating small glowing orbs (food) to grow
       - Look for clusters of food to maximize growth
       - Avoid going too far from the center where food is scarce

    3. Snake Interaction Rules:
       - Hunt smaller snakes by encircling them
       - Maintain safe distance from larger snakes
       - If a larger snake approaches, quickly change direction
       - Use boost (right-click) only when necessary to escape

    4. Survival Tactics:
       - Stay in the middle area where food is abundant
       - Watch the minimap for approaching threats
       - Keep an eye on the leaderboard position
       - Avoid getting trapped in corners or by multiple snakes

    5. Winning Strategy:
       - Focus on steady growth through food collection
       - Take calculated risks to eat smaller snakes
       - Monitor your position on the leaderboard
       - Continue playing until you reach #1 on the leaderboard

    6. Error Handling:
       - If disconnected, reconnect immediately
       - If the game freezes, refresh the page
       - If controls feel unresponsive, check for lag

    7. Visual Verification:
       - Regularly check your snake's size
       - Monitor the leaderboard position
       - Watch for approaching threats
       - Verify food collection and growth

    Continue playing until you reach #1 on the leaderboard or are explicitly stopped. Focus on steady growth while maintaining survival.

    """)
