def run():
    def caesar_encrypt(text, key):

        result = ""

        for char in text:
            if char.isalpha():
                start_val = ord('a') if char.islower() else ord('A')           
                shifted_char_index = (ord(char) - start_val + key) % 26
                new_char = chr(start_val + shifted_char_index)
                
            else:
                new_char = char

            result += new_char
            
        return result



    text = input("\nCaesar_Cipher_Bruteforce >")
    print("\n")
    shift_key = 3
    for key in range(27):
        cipher = caesar_encrypt(text, key)
        print(str(key)+"\t:\t"+cipher)
    print("\n")

