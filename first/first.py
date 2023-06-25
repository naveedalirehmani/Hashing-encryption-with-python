from printHash import printHash

name = input("Input your name: ")

print('')
print('_____________________________________________________')
print('')
printHash(name)
print('')
print('_____________________________________________________')
print('')

print("concanating just 1 to your name will result in hash fingerprint to be completely different hence")
print("representing a avalanch effect")

print('')
print('_____________________________________________________')
print('')
printHash(name + "1")
print('')
print('_____________________________________________________')
print('')




