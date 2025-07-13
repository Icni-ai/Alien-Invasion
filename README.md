# 👽 Alien Invasion

**Alien Invasion** is a 2D arcade shooter inspired by classic alien defense games.  
Control your ship, shoot down the invaders, and survive as long as possible!
<img width="1920" height="1080" alt="alien_invasion_screen" src="https://github.com/user-attachments/assets/d7c441c9-db41-4a4b-9f06-ac458ccaa502" />

## 🎮 Controls

| Key      | Action              |
|----------|---------------------|
| `A`      | Move left           |
| `D`      | Move right          |
| `SPACE`  | Shoot               |
| `ESC`    | Exit the game       |

## 📁 Project Structure

- `alien_invasion.py` — Main entry point of the game
- `ship.py` — Handles player ship movement
- `alien.py` — Controls alien behavior
- `bullet.py` — Bullet creation and movement
- `button.py` — Play button logic
- `mode.py` — Difficulty selection (3 buttons: Easy, Medium, Hard)
- `game_stat.py` — Tracks game statistics
- `scoreboard.py` — Displays score and lives
- `settings.py` — Game settings and constants
- `sounds.py` — Sound effects
- `fonts/`, `images/`, `sounds/` — Game assets (fonts, images, audio)

## 🚀 How to Run

1. Make sure you have **Python 3.8+** installed  
   [Download Python](https://www.python.org/downloads/)

2. Install the required dependency:
   ```bash
   pip install pygame

3. Run the game
   ```bash
   python alien_invasion.py
