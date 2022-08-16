# fonttools WOFF generate scripts
![License: 0BSD](https://img.shields.io/github/license/jonz94/fonttools-woff-generate-scripts)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Generate `woff`/`woff2` fonts from `ttf`/`otf` fonts using [`fonttools`](https://github.com/fonttools/fonttools) python library

## Requirements

- python (version 3+ is recommended)

- fonttools library

```
pip install fonttools
```

- Brotli is needed to generate `woff2` fonts

```
pip install brotli
```

## Usage

- Put `ttf`/`otf` fonts into `inputs` directory

- Run script

```
python main.py
```

- Then `woff`/`woff2` fonts will occur inside `outputs` directory

- Done 🎉
