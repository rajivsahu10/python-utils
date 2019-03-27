from prettytable import PrettyTable


List1 = [('100.20.300.400', 'varagu', 'success'), ('100.20.300.500', 'thinai', 'success')]
List2 = [('100.20.300.600', 'Ragi', 'Failed')]

table = PrettyTable(['IP', 'Name', 'Result'])
for IP, Name, Result in List1:
    table.add_row([IP, Name, Result])
print(table)

ftable = PrettyTable(['IP', 'Name', 'Result'])
for IP, Name, Result in List2:
    ftable.add_row([IP, Name, Result])
print(ftable)
