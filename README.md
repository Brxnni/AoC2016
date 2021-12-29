# AoC2016

Advent of Code 2016. There's not much more to know.

* Every day has its own folder.
* In every folder there is a:
  * `main.py`, which contains the code for the solution (two functions: `part1` and `part2`).
  * `puzzle.md`, which contains the puzzle description.
  * `sample.txt`, which contains the sample input.
  * `input.txt`, which contains the whole puzzle input.
  * (if the `.txt` files are not included, that means the input is just a single string, like in day 5.)
* There is also the `playsound.py` file, which can play sounds (the sound can be found [here](https://www.youtube.com/watch?v=DfUvUEUPNnc)), because the computation of day 5 took like half an hour and I didn't want to miss it.
  You can use

  ```python
  import os
  import sys
  # I can't figure out how to import files from the same directory, so this is the solution.
  fullPath = "\\".join(os.path.realpath(__file__).split("\\")[:-2])
  sys.path.append(fullPath)
  import playsound
  # Actually play the sound after 5 lines
  playsound.play(f"{fullPath}\\done.mp3")
  ```

  to play the sound.
