list_names = ['Irsyad', 'Hasan', 'Elia', 'Erni']

for name in list_names:
    print(name)

# What if you want the index too like

index = 0
for name in list_names:
    print(index, name)
    index += 1

# use Enumerate()

for index, name in enumerate(list_names):
    print(index, name)

# use Zip
# CASE

names = ['new', 'names', 'here']
matches = ['baru', 'nama', 'disini']

for index, nama, in enumerate(names):
    match = matches[index]
    print(f'the match for {nama} is {match}')

# dont use enumerate use ZIP

for nama, match in zip(names, matches):
    print(f'the match for {nama} is {match} with zip')
