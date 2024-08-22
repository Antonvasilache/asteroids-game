# Asteroids game

## Description

This is a rendition of the classic Asteroids game implemented using Pygame. Players control a spaceship, navigating through a field of asteroids, while avoiding collisions and shooting them down. The game features:

- **Score Tracking:** Keep track of your current score and compete against yourself and others
- **Multiple lives:** Start with multiple lives and continue playing even after being hit by an asteroid
- **Accelerated movement:** Your movement speed ramps up and winds down as you press the forward key
- **Collectable power-ups:** Collect power-ups to enhance your capabilities, like increasing your speed or protecting yourself against collisions.

## How to play

1. **Clone the repository:**
   ```
   git clone github.com/Antonvasilache/asteroids-game
   ```

2. **Install dependencies:** Ensure you have Pygame installed, if not, use:
   ```
   pip install game
   ```

3. **Run the game:** Navigate to the project directory and run the main file:
   ```
   python3 main.py
   ```

### Controls:

- **Movement:** Use the WASD keys to control the spaceship.
- **Shooting:** Press the space bar to fire your weapon

### Game mechanics:

- **Asteroids:** Asteroids will randomly appear on the screen, floating in random directions
- **Collisions:** Colliding with asteroids will consume one life
- **Screen wrapping:** Navigating to the edge of the screen will take you to the opposite side
- **Power-ups:** Collect power-ups that appear throughout the game to gain temporary advantadges
- **Scoring:** Destroy asteroids to earn points. Your score will be displayed on screen.
