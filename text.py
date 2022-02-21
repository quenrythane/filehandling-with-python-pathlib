from pathlib import Path

# czytanie pliku i pisanie w pliku
old_text = Path('text.txt').read_text(encoding='utf-8')
print(old_text)

text_pl = "to jest tekst który napisałem z path write"
text = '\n'.join((old_text, text_pl))
Path('create_new_text.txt').write_text(text, encoding='utf-8')

bytes = Path("text.txt").read_bytes()
print('bytes:', bytes)



