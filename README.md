
# AI Chess Strategy Optimizer

## What This Project Is About

This project is all about using AI to make smarter decisions in chess, especially during the mid-to-endgame. We built a chess game where you can play against two different types of AI: one that uses **Minimax with Alpha-Beta Pruning** and another that uses **Monte Carlo Tree Search (MCTS)**. We wanted to see which one plays better and how they are different.

We also made a cool graphical interface so it’s fun and easy to play!

## Team Members

- Anand Gopi Sai Krishna  
- Yamini Poojitha  
- Aabdhul Kamour  

## Research Question

> How can Minimax and MCTS help improve chess moves in the middle and end of a game, and how do they perform differently when making decisions?

## Main Features

- **Basic Chess Engine**: Handles piece movement and legal moves.
- **Two AI Modes**:
  - **Minimax with Alpha-Beta Pruning** – makes smart choices based on material count.
  - **MCTS** – tries out different possibilities randomly and learns what might work.
- **User Interface**: Built with Pygame – includes move highlights and detects checkmate.
- **Mode Selection**: Pick if you want to play against Minimax or MCTS.

## How We Built It

- **Minimax** goes through possible moves to a certain depth and cuts off bad ones early to save time.
- **MCTS** plays random games and picks the move that wins more often.
- We made sure the game doesn’t get stuck or crash, and added checkmate detection.
- Highlighted possible moves in yellow to help players.

## How to Run It

1. **Clone the Project**

```bash
git clone https://github.com/anandgopi20/AI-project.git
cd AI-project
```

2. **Install What You Need**

You need Python 3.7+ and Pygame.

```bash
pip install -r requirements.txt
```

Or just install Pygame if needed:

```bash
pip install pygame
```

3. **Start the Game**

```bash
python main.py
```

4. **Playing the Game**

- Choose between Minimax and MCTS when the game starts.
- Click a piece, then click one of the highlighted squares to move.
- The game ends automatically when checkmate happens and shows who won.

## What We Found

| Feature           | Minimax                          | MCTS                                   |
|-------------------|----------------------------------|----------------------------------------|
| Speed             | Faster for short look-aheads     | Slower due to random simulations       |
| Strategy          | Focused and tactical             | More random and experimental           |
| Behavior          | Plays safer and smarter          | Can repeat or make weird moves         |
| Improvements Made | Added pruning                    | Taught it to prefer capturing pieces   |

## What We Think

Minimax worked better overall. It played smarter and faster, especially in tricky endgame spots. MCTS has potential but needs more training and tuning to be as strong.

---

**This was a learning project inspired by big names like AlphaZero and Stockfish.**  
We used some ideas from Sunfish to help build our base chess engine.

---

## License

This project is open-source and for learning purposes only.
