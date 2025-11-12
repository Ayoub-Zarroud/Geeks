import time
from collections import Counter
from typing import Iterable, Tuple, Set

Cell = Tuple[int, int]
class GameOfLife:
    def __init__(self, rows: int = 20, cols: int = 40, initial: Iterable[Cell] = None,
                 expandable: bool = False, max_size: int = 10000):
        self.rows = rows
        self.cols = cols
        self.expandable = expandable
        self.max_size = max_size
        self.live: Set[Cell] = set(initial) if initial else set()
        if not self.expandable:
            self.live = set((r, c) for (r, c) in self.live if 0 <= r < rows and 0 <= c < cols)
        self.history = set()
        self.generation = 0

    def _neighbors(self, cell: Cell):
        r, c = cell
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                yield (r + dr, c + dc)

    def step(self):
        """Compute next generation following Conway's rules."""
        counts = Counter()
        for cell in self.live:
            for nb in self._neighbors(cell):
                if not self.expandable:
                    nr, nc = nb
                    if not (0 <= nr < self.rows and 0 <= nc < self.cols):
                        continue
                counts[nb] += 1

        next_live = set()
        for cell, cnt in counts.items():
            if cnt == 3 or (cnt == 2 and cell in self.live):
                
                if not self.expandable:
                    r, c = cell
                    if not (0 <= r < self.rows and 0 <= c < self.cols):
                        continue
                next_live.add(cell)
        if self.expandable:
            minr = min((r for r, _ in next_live), default=0)
            maxr = max((r for r, _ in next_live), default=0)
            minc = min((c for _, c in next_live), default=0)
            maxc = max((c for _, c in next_live), default=0)
            height = maxr - minr + 1
            width = maxc - minc + 1
            if height * width > self.max_size:
                raise MemoryError("Expandable board would exceed max_size limit.")

        self.generation += 1
        self.live = next_live

    def display(self, padding: int = 1):
        """Print grid to terminal."""
        if self.expandable:
            if not self.live:
                print("(no live cells)")
                return
            minr = min(r for r, _ in self.live) - padding
            maxr = max(r for r, _ in self.live) + padding
            minc = min(c for _, c in self.live) - padding
            maxc = max(c for _, c in self.live) + padding
        else:
            minr, maxr = 0, self.rows - 1
            minc, maxc = 0, self.cols - 1
        border = "+" + "-" * (maxc - minc + 1) + "+"
        print(f"Generation {self.generation} | Size: {len(self.live)}")
        print(border)
        for r in range(minr, maxr + 1):
            row_chars = []
            for c in range(minc, maxc + 1):
                row_chars.append("█" if (r, c) in self.live else " ")
            print("|" + "".join(row_chars) + "|")
        print(border)
    def run(self, generations: int = 100, pause: float = 0.2, stop_if_repeat: bool = True):
        self.history = set()
        self.generation = 0
        initial_state = frozenset(self.live)
        self.history.add(initial_state)
        self.display()
        for _ in range(generations):
            self.step()
            self.display()
            if not self.live:
                print("All cells are dead. Simulation ends.")
                break
            state = frozenset(self.live)
            if stop_if_repeat and state in self.history:
                print("Configuration repeated (stable or oscillating). Simulation ends.")
                break
            self.history.add(state)
            if pause > 0:
                time.sleep(pause)

def pattern_block(top=1, left=1):
    return {(top, left), (top, left + 1), (top + 1, left), (top + 1, left + 1)}
def pattern_blinker(center_r=5, center_c=5):
    return {(center_r, center_c - 1), (center_r, center_c), (center_r, center_c + 1)}
def pattern_glider(top=0, left=0):
    coords = {(top, left + 1),
              (top + 1, left + 2),
              (top + 2, left), (top + 2, left + 1), (top + 2, left + 2)}
    return coords
if __name__ == "__main__":
    print("Example 1 — Block (stable) on fixed board")
    g1 = GameOfLife(rows=6, cols=12, initial=pattern_block(1, 1), expandable=False)
    g1.run(generations=5, pause=0.1)

    print("\nExample 2 — Blinker (oscillator) on fixed board")
    g2 = GameOfLife(rows=7, cols=15, initial=pattern_blinker(3, 7), expandable=False)
    g2.run(generations=6, pause=0.2)

    print("\nExample 3 — Glider on fixed board (it will move and eventually exit bounds)")
    g3 = GameOfLife(rows=10, cols=20, initial=pattern_glider(1, 1), expandable=False)
    g3.run(generations=30, pause=0.05)

    print("\nExample 4 — Glider on expandable board (it will keep moving)")
    g4 = GameOfLife(rows=10, cols=20, initial=pattern_glider(0, 0), expandable=True, max_size=5000)
    g4.run(generations=30, pause=0.05)
