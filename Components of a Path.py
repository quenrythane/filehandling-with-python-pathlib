from pathlib import Path

# .cwd() -> (Current Working Directory)
current_path = Path.cwd()
print('current_path:', current_path)  # C:\Users\Thane Art\PycharmProjects\Szturm xD\filehandling with Path

# .home() ->  (your user’s home directory) (user)
home = Path.home()
print('home:', home)  # C:\Users\Thane Art
dir = home / 'PycharmProjects' / 'Szturm xD'
print("dir:", dir)  # C:\Users\Thane Art\PycharmProjects\Szturm xD


resolve = Path('files/text1.txt').resolve()  # show full directory to file
print("resolve:", resolve)  # C:\Users\Thane Art\PycharmProjects\Szturm xD\filehandling with Path\files\text1.txt

print(resolve.parent.parent == current_path)  # -> parent return directory with one dir upper (work like cd..)
# as you can see we could use .parent many times

file = Path('archive files.py')
path = file.cwd() / file
print('path:', path)  # -> C:\Users\Thane Art\PycharmProjects\Szturm xD\filehandling with Path\archive files.py
print('name:', path.name)  # -> archive files.py
print('stem:', path.stem)  # -> archive files
print('suffix:', path.suffix)  # -> .py
print('anchor:', path.anchor)  # -> C:/
print('parent:', path.parent)  # -> C:\Users\Thane Art\PycharmProjects\Szturm xD\filehandling with Path
print('parent.parent:', path.parent.parent)  # -> parent: C:\Users\Thane Art\PycharmProjects\Szturm xD
