answer = str(input('>'))

if answer == 'help':
    print('start - to start the car')
    print('stop - to stop the car')
    print('quit - to exit')

elif answer == 'start':
    print('Car started...Ready to go!')

elif answer == 'stop':
    print('Car stopped.')

else:
    print("I don't understand that...")