![HEIC to JPG](assets/hero.png)

# HEIC to JPG

*HEIC that Windows apps can actually open.*

## Overview

**HEIC to JPG** runs on your own PC. Convert iPhone HEIC photos to JPEG and keep a copy of the original.

Mail and older editors still choke on HEIC.

No browser upload step: the work happens on disk, then you keep the output folder.

## How to get it

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Features

- Folder convert
- JPEG quality
- Keeps HEIC sources
- Reports failures per file

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/adamhayes254/heic-to-jpg

MIT license. See `LICENSE`.
