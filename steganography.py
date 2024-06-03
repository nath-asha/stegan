from PIL import Image

def encode_text(image, text):
    binary_text = ''.join([format(ord(char), '08b') for char in text])
    binary_text += '1111111111111110'  # End of text delimiter

    encoded_image = image.copy()
    width, height = image.size
    pixels = encoded_image.load()
    
    idx = 0
    for i in range(width):
        for j in range(height):
            if idx < len(binary_text):
                r, g, b = pixels[i, j]
                r = (r & ~1) | int(binary_text[idx])
                pixels[i, j] = (r, g, b)
                idx += 1
            else:
                break
        if idx >= len(binary_text):
            break

    return encoded_image

def decode_text(image):
    binary_text = ''
    width, height = image.size
    pixels = image.load()
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            binary_text += str(r & 1)
    
    bytes_text = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    decoded_text = ''
    for byte in bytes_text:
        if byte == '1111111111111110':  # End of text delimiter
            break
        decoded_text += chr(int(byte, 2))
    
    return decoded_text
