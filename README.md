# friendly-chainsaw 🪚

A lightweight, zero-dependency CLI tool built in Python to safely shred development junk, build caches, and empty directories with a fun, real-time chainsaw animation.

<img width="1115" height="492" alt="image" src="https://github.com/user-attachments/assets/ba2de49f-f795-4016-af54-3b16eab10bfd" />

## NOTE: this repo can damage your PC if you start destroying your entire files.

## Features

- **Real-Time Slicing Animation:** Watch a custom text-based chainsaw physically slice through file paths as it cleans them up.
- **Pure Python:** Zero external modules required. Runs instantly without `pip`, `npm`, `node`, or virtual environments.
- **Deep Clean:** Recursively targets redundant logs, temporary assets, and environment leftovers.
- **Smart Pruning:** Automatically detects and removes deeply nested, entirely empty folders after purging their contents.
- **Built-in Guardrails:** Includes confirmation steps to prevent accidental root or current directory destruction.

## Targets for Destruction

The friendly chainsaw safely targets and shreds:
- **Cache Folders:** `__pycache__`, `.pytest_cache`, `.ipynb_checkpoints`, `.sass-cache`
- **System Junk:** `.DS_Store`, `Thumbs.db`, `desktop.ini`
- **Log Outdated Files:** `npm-debug.log`, `yarn-error.log`, `.log`, `.tmp`, `.bak`, `.swp`

## Usage

### Prerequisites
- Python 3.x installed on your machine.

### Installation
Simply clone this repository or download the script file directly:
```bash
git clone https://github.com
cd friendly-chainsaw
```

### Running the Chainsaw
You can execute the script and input the path interactively:
```bash
python friendly_chainsaw.py
```

Alternatively, pass the target folder path directly as an argument for a faster execution:
```bash
python friendly_chainsaw.py /path/to/your/cluttered/project
```

## License
This project is open-source and available under the MIT License.
