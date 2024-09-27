# Function for Run-Length Encoding
def rle_encode(data):
    encoded_string = ""
    i = 0

    while i < len(data):
        # Count occurrences of the current character
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1

        # Append the character and its count
        encoded_string += data[i] + str(count)
        i += 1

    return encoded_string


# Function to perform Run-Length Decoding
def rle_decode(encoded_data):
    decoded_string = ""
    i = 0

    while i < len(encoded_data):
        # Get the character
        char = encoded_data[i]
        i += 1

        # Get the count (which might be more than 1 digit)
        count = ""
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count += encoded_data[i]
            i += 1

        # Append the character count times to the result
        decoded_string += char * int(count)

    return decoded_string


# Example usage
if __name__ == "__main__":
    text = "abbcccdddd"

    # Compress the text using RLE
    encoded_text = rle_encode(text)
    print("Encoded text:", encoded_text)

    # Decompress the text back to original
    decoded_text = rle_decode(encoded_text)
    print("Decoded text:", decoded_text)
