### friendly-chainsaw 🪚

A lightweight, zero-dependency CLI tool built in Python to safely shred development junk, build caches, and empty directories with a fun, real-time chainsaw animation. 

### ==========================================================================
WELCOME TO FRIENDLY-CHAINSAW

 ____                                                             

*/*||*_
//   __   \      _________________________________________________
||  [****]  ||===| o o                                            |
\________//     _***____________________________________*******|
_*******/

========================================================================== 

### Features

* **Real-Time Slicing Animation:** Watch a custom text-based chainsaw physically slice through file paths as it cleans them up.
* **Pure Python:** Zero external modules required. Runs instantly without pip, npm, node, or virtual environments.
* **Deep Clean:** Recursively targets redundant logs, temporary assets, and environment leftovers.
* **Smart Pruning:** Automatically detects and removes deeply nested, entirely empty folders after purging their contents.
* **Built-in Guardrails:** Includes confirmation steps to prevent accidental root or current directory destruction.

### Targets for Destruction

The friendly chainsaw safely targets and shreds: 

* **Cache Folders:** __pycache__, .pytest_cache, .ipynb_checkpoints, .sass-cache
* **System Junk:** .DS_Store, Thumbs.db, desktop.ini
* **Log Outdated Files:** npm-debug.log, yarn-error.log, .log, .tmp, .bak, .swp

### Usage

### Prerequisites

* Python 3.x installed on your machine.

### Installation

Simply clone this repository or download the script file directly: 

bash

git clone https://github.com/YOUR_USERNAME/friendly-chainsaw.git
cd friendly-chainsaw

Use o código com cuidado.

### Running the Chainsaw

You can execute the script and input the path interactively: 

bash

python friendly_chainsaw.py

Use o código com cuidado.

Alternatively, pass the target folder path directly as an argument for a faster execution: 

bash

python friendly_chainsaw.py /path/to/your/cluttered/project

Use o código com cuidado.

### License

This project is open-source and available under the MIT License.
