from pathlib import Path
import collections

counted = collections.Counter(p.suffix for p in Path.cwd().iterdir())
print(counted)  # -> Counter({'.py': 6, '.txt': 4, '': 3, '.md': 1})


