from PIL import Image

# 🔐 HIDE DATA IN IMAGE (LSB STEGANOGRAPHY)
def hide_data(image_path, data, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')

    data += "###END###"  # delimiter to mark end
    binary_data = ''.join(format(ord(c), '08b') for c in data)

    pixels = list(img.getdata())
    new_pixels = []

    data_index = 0
    data_len = len(binary_data)

    for pixel in pixels:
        r, g, b = pixel

        if data_index < data_len:
            r = (r & ~1) | int(binary_data[data_index])
            data_index += 1

        if data_index < data_len:
            g = (g & ~1) | int(binary_data[data_index])
            data_index += 1

        if data_index < data_len:
            b = (b & ~1) | int(binary_data[data_index])
            data_index += 1

        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)

    return output_path


# 🔓 EXTRACT DATA FROM IMAGE
def extract_data(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_data = ""

    for pixel in pixels:
        r, g, b = pixel
        binary_data += str(r & 1)
        binary_data += str(g & 1)
        binary_data += str(b & 1)

    # Convert binary to text
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    decoded_data = ""
    for byte in all_bytes:
        char = chr(int(byte, 2))
        decoded_data += char

        if "###END###" in decoded_data:
            return decoded_data.replace("###END###", "")

    return ""