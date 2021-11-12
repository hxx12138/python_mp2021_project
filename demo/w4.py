import math

dt = {'k1': 1, 'k2': 2, 'k3': 3}
print('k1: {0[k1]}; k2: {0[k2]}; k3: {0[k3]}'.format(dt))
print('k1: {k1}; k2: {k2}; k3: {k3}'.format(**dt))

print(dt)
print('{!a}'.format('天津tianjin'))
print('{!s}'.format(dt))
print('{!r}'.format(dt))


year = 2016
event = 'Ceremony'
print(f'Results of the {year} {event}')
print(f'The value of pi is approximately {math.pi:.15f}.')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print(f'{yes_votes:-9} YES votes  {percentage:2.2%}')

animals='eels'
print(f'My hovercraft is full of {animals!s}.')
print(f'My hovercraft is full of {animals!r}.')
