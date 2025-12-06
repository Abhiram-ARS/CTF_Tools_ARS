def run():
    def simple_base64_decode(encoded_string):
        import base64

        try:
            encoded_bytes = encoded_string.encode('utf-8')
            decoded_bytes = base64.b64decode(encoded_bytes)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
            
        except Exception as e:
            return f"Error decoding: {e}"

    encoded_data = input("\nBase64_Decode >")
    decoded_result = simple_base64_decode(encoded_data)
    print(f"Decoded Result: {decoded_result}")
