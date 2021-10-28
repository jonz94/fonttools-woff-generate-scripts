import os
from fontTools.ttLib import TTFont


def generate_font(inputsDir, outputsDir, filename, inputFormat, outputFormat):
    print(f"generating {filename.replace(inputFormat, outputFormat)}...")

    font = TTFont(inputsDir + filename)
    font.flavor = outputFormat
    font.save(outputsDir + filename.replace(inputFormat, outputFormat))
    font.close()


def main():
    workspace = os.path.abspath(__file__).replace("/main.py", "")

    inputsDir = f"{workspace}/inputs/"
    outputsDir = f"{workspace}/outputs/"

    for file in os.listdir(os.fsencode(inputsDir)):
        filename = os.fsdecode(file)

        if filename.endswith(".ttf"):
            inputFormat = "ttf"
        elif filename.endswith(".otf"):
            inputFormat = "otf"
        else:
            continue

        generate_font(inputsDir, outputsDir, filename, inputFormat, "woff")
        generate_font(inputsDir, outputsDir, filename, inputFormat, "woff2")


if __name__ == "__main__":
    main()
