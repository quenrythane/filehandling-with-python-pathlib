from pathlib import Path

path = Path('write 1000 same lines.txt')
line = 'to jest linijka do napisania 1000 razy'

text_to_write = '\n'.join(f"{i} {line}." for i in range(1, 1001))
path.write_text(text_to_write, 'utf-8')
