from pathlib import Path

file = Path('text_to_move.txt')
not_file = Path('Moving and files.py')
file_path = file.cwd() / file
path = file.cwd()
print('file_path:', file_path)
print('file.exists():', file.exists())
print('file_path.exists():', file_path.exists())
print('not_file.exists():', not_file.exists())
print('\n\n')

# Path('do usuniecia').rmdir()  # -> remove dir 'do usuniecia'
# Path('text_to_move.txt').unlink()  # -> remove files 'text_to_move.txt'


Path('text_to_move.txt').replace(path / 'files')
# source.replace(destination)
