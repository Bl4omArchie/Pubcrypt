from pubcrypt.scheme import pss



if __name__ == "__main__":
    # Example usage:
    message = b"Hello, World!"
    nBits = 128            # Adjust as needed
    encoded_message = pss.signature_generation(message, (101, 17), nBits)
    print(encoded_message)