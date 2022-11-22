import os
from fontTools.ttLib import TTFont
from pathlib import Path


def generate_font(inputsDir, outputsDir, filename, inputFormat, outputFormat):
    inputPath = Path.joinpath(inputsDir, filename)
    outputFilename = filename.replace(inputFormat, outputFormat)
    outputPath = Path.joinpath(outputsDir, outputFilename)

    print(f"generating {outputFilename}...")

    font = TTFont(inputPath)
    font.flavor = outputFormat
    font.save(outputPath)
    font.close()


def main():
    projectRoot = Path(__file__).parent

    inputsDir = Path.joinpath(projectRoot, "inputs")
    outputsDir = Path.joinpath(projectRoot, "outputs")

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
