import PIL.Image

# ASCII Characters
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

# Resizing
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)

# Convert image to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


# Converting pixels to ASCII
def pixels_to_ascii(image):
    pixels = image.getdata()
    # Creating string of ASCII
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=100):
    path = input("Give me path please thanks.")

    # Error handling 
    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print("Error: ", e)
        return
    
    if image is None:
        print("Failed to load the image.")
        return 
    
    # Use the methods to grab our string
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # Formatting the data
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range (0, pixel_count, new_width))

    print(ascii_image)

    # Write to text file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()