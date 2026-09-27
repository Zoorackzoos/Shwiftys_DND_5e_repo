Here's the PyInstaller command targeting that output folder:

```powershell
cd "C:\Users\dunca\Desktop\code_files\0 perssonal\python_projects\shwifty_dnd_repo\src"
pyinstaller --onefile --distpath "C:\Users\dunca\Desktop\code_files\0 perssonal\python_projects\shwifty_dnd_repo\built_programs" A_GUI_programs/computer_minigames/technodrome_elevator/technodrome_elevator.py
```

The key addition is `--distpath` — that's the flag that tells PyInstaller where to drop the finished `.exe`, instead of its default `dist/` subfolder wherever you ran the command from.

---

## How to write your own "compile this" command

Every PyInstaller command you'll write follows the same skeleton:

```powershell
cd "<path to src, so imports resolve correctly>"
pyinstaller --onefile --distpath "<where you want the .exe to end up>" <relative/path/to/the_target_file.py>
```

Breaking down each piece so you can swap parts out yourself:

1. **`cd` into `src` first.** Same reasoning as the `python -m` issue from before — PyInstaller traces your file's imports starting from wherever your terminal's current directory is. If you don't `cd` into `src`, it won't correctly resolve `from A_GUI_programs...` style imports inside your file, and the build will either fail or produce a broken `.exe`.

2. **`pyinstaller`** — the command itself. Always the same.

3. **`--onefile`** — bundles everything (your code + all dependencies) into a single `.exe`, instead of PyInstaller's default of dumping a folder full of loose support files. Always want this for a "just double-click it" minigame.

4. **`--distpath "..."`** — where the finished `.exe` goes. Point this at your `built_programs` folder every time, so all your compiled games end up in one place instead of scattered `dist/` folders next to each source file.

5. **The path to the target `.py` file** — this is the *only* thing that changes between different minigames. It's written relative to wherever you `cd`'d to (which is `src`), using forward slashes, ending in the actual filename.

So to compile a *different* minigame, you only ever change that last piece:

```powershell
cd "C:\Users\dunca\Desktop\code_files\0 perssonal\python_projects\shwifty_dnd_repo\src"
pyinstaller --onefile --distpath "C:\Users\dunca\Desktop\code_files\0 perssonal\python_projects\shwifty_dnd_repo\built_programs" A_GUI_programs/computer_minigames/some_other_game/some_other_game.py
```

**Two extra flags worth knowing about, if you hit them:**

- `--name "CustomName"` — controls the `.exe`'s filename, if you don't want it to just match the source file's name.
- `--console` vs `--windowed` — PyInstaller defaults to `--console` (keeps a terminal window open, which you want for your keyboard/`msvcrt`-driven games so you can see output). `--windowed` hides the console entirely — don't use that one for these, since your minigames rely on visible terminal text.

**One more thing to watch for once you actually test-run this:** PyInstaller also generates a `build/` folder and a `.spec` file alongside wherever you ran the command — those are intermediate/config files, not something you need to keep or distribute, only the `.exe` in `built_programs` matters. Safe to `.gitignore` `build/` and `*.spec` if you don't want them cluttering your repo.