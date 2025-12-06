import base64_decoder
import ceaserCipher

while True:
    command = input("CTF_Tool_Engine >")
    match(command):
        case 'exit':
            break
        case 'base64':
            base64_decoder.run()
        case 'base64':
            ceaserCipher.run()
        
        case _:
            print("Error : Invalied Choice")
    print('')
