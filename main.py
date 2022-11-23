import os
from fontTools.ttLib import TTFont
from pathlib import Path


def generate_font(inputsDir, outputsDir, filename, outputFormat):
    inputPath = Path.joinpath(inputsDir, filename)
    outputFilename = inputPath.with_suffix(f".{outputFormat}").name
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
            pass
        elif filename.endswith(".otf"):
            pass
        else:
            continue

        generate_font(inputsDir, outputsDir, filename, "woff")
        generate_font(inputsDir, outputsDir, filename, "woff2")


if __name__ == "__main__":
    main()
