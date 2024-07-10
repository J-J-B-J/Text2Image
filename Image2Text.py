"""Convert an image into some text"""
from PIL import Image


def load_image_from_file() -> Image.Image:
    try:
        with Image.open("image.png", "r") as f:
            return f.copy()
    except OSError:
        print("No file found. Please create a file called 'image.png'.")
        exit(1)


def image_to_text(image: Image.Image) -> str:
    text = ""
    for y in range(image.height):
        for x in range(image.width):
            colour = list(image.getpixel((x, y)))
            while 0 in colour:
                colour.pop(-1)
            for value in colour:
                try:
                    text += value.to_bytes().decode()
                except UnicodeDecodeError:
                    pass

    return text


def main() -> None:
    """The main function"""
    image = load_image_from_file()
    text = image_to_text(image)
    print(text)


if __name__ == "__main__":
    main()
