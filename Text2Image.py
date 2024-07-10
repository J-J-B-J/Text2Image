"""Convert some text into an image"""
from PIL import Image
from math import sqrt, ceil


def load_text_from_file() -> str:
    try:
        with open("text.txt", "r") as f:
            return "".join(f.readlines())
    except OSError:
        print("No file found. Please create a file called 'text.txt'.")
        exit(1)


def text_to_colour_codes(hex_text: str) -> list[tuple[int]]:
    # Convert the integers into RGB colour codes
    colour_codes = []
    for num, char in enumerate(hex_text):
        if num % 3 == 0:
            colour_codes.append((int(char.encode().hex(), 16),))
        else:
            colour_codes[-1] += (int(char.encode().hex(), 16),)

    # Make sure the last colour code is complete
    while len(colour_codes[-1]) < 3:
        colour_codes[-1] += (0,)

    return colour_codes


def create_image(pixels: list[tuple[int]]) -> Image:
    # Calculate the image size required for a square image
    width = ceil(sqrt(len(pixels)))
    # Calculate the required height of the image
    height = ceil(len(pixels) / width)
    # Create the image
    img = Image.new("RGB", (width, height))

    # Set the pixels of the image
    for number, colour in enumerate(pixels):
        img.putpixel((number % width, number // width), colour)
    return img


def main() -> None:
    """The main function"""
    text = load_text_from_file()
    pixels = text_to_colour_codes(text)
    image = create_image(pixels)
    image.show()


if __name__ == "__main__":
    main()
