# 🎮 Goblin Pygame

> A Python implementation of the classic goblin pursuit problem

## 📖 About

Inspired by [Goblin Escape](https://mirangod.itch.io/goblin-escape), this is my implementation in Python. The goblin pursuit problem is a classic mathematical challenge. This is a purely skill-based game with no random elements.

## ⚡ Quick Start

### Prerequisites

- Python 3.7+
- pip

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd goblin-pygame

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python game/main.py
```

## 🎮 Controls

- **Arrow Keys** or **WASD** - Move your character

## 🏗️ Project Structure

```
goblin-pygame/
├── game/
│   ├── main.py           # Entry point
│   ├── ai/
│   │   └── pursuit.py    # AI pursuit algorithms
│   ├── core/
│   │   ├── constants.py  # Game constants
│   │   └── game.py       # Main game loop
│   ├── entities/
│   │   ├── entity.py     # Base entity class
│   │   ├── goblin.py     # Goblin entity
│   │   └── player.py     # Player entity
│   ├── states/
│   │   └── play.py       # Game state management
│   └── world/
│       └── world.py      # Circular world
└── requirements.txt      # Dependencies
```

## 🧮 The Math Behind It

The goblin pursuit problem is based on pursuit curves - mathematical paths where a pursuer follows an optimal strategy to catch a target. In this game, goblins calculate the shortest angular path around the circle to intercept the player.

- Inspired by [Goblin Escape](https://mirangod.itch.io/goblin-escape)
---
