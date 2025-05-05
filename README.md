# Chess AI: Human vs Minimax and MCTS

This project explores two classic AI algorithms—**Minimax with Alpha-Beta Pruning** and **Monte Carlo Tree Search (MCTS)**—to enhance **mid-to-endgame chess strategies**. The final version includes a Pygame-based GUI to play against both algorithms.

---

## 🔍 Research Question

**Can Monte Carlo Tree Search improve mid-to-endgame move decisions in chess compared to the traditional Minimax algorithm with alpha-beta pruning?**

---

## 📌 Features

- Text-based and GUI-based chess engine
- Minimax with alpha-beta pruning (depth-based)
- Monte Carlo Tree Search (simulation-based)
- Smart move selection (prioritize captures)
- Undo move support (for Minimax logic)
- Highlighting possible moves when selecting a piece
- Checkmate and game-over detection
- Evaluation function based on material balance

---

## 🧠 AI Algorithms

### ✅ Minimax with Alpha-Beta Pruning
- Evaluates board positions up to a fixed depth.
- Relies on a static evaluation function (material count).
- Smart move ordering to prioritize captures first.

### ✅ Monte Carlo Tree Search (MCTS)
- Simulates multiple playouts to evaluate moves.
- Encourages captures in simulations.
- Adaptive decision-making under uncertainty.

---

## 🖥️ GUI

- Built with **Pygame**
- Click to select a piece → Highlights all possible legal moves (yellow squares)
- After each move, the evaluation score is shown in console output
- Displays winner and game status (Checkmate/Stalemate)

---


