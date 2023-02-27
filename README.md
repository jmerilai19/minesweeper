# Minesweeper

A simple Python class that implements a typical Minesweeper game.
Included is also a sample console client for demonstaring the usage. 

### Example
```
import minesweeper

game = minesweeper.Game()

status, board = game.start()
print(board)

status, board = game.play(1, 1, "open")
print(board)
```
