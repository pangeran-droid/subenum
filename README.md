# Subenum

Simple Passive Subdomain Enumerator written in Python.

```text
               __                             
   _______  __/ /_  ___  ____  __  ______ ___ 
  / ___/ / / / __ \/ _ \/ __ \/ / / / __ `__ \
 (__  ) /_/ / /_/ /  __/ / / / /_/ / / / / / /
/____/\__,_/_.___/\___/_/ /_/\__,_/_/ /_/ /_/ 
                                              
Simple Subdomain Enumerator


usage: subenum.py [-h] -d DOMAIN [--status]

```

## Overview

Subenum is a lightweight passive subdomain enumeration tool inspired by tools like `subfinder`.

It collects subdomains from public sources and optionally checks HTTP status codes.

Designed for:
- Bug bounty recon
- OSINT
- Red team reconnaissance
- Learning passive enumeration techniques

---

## Features

- Passive subdomain enumeration
- Multiple data sources:
  - crt.sh
  - dns.bufferover.run
  - hackertarget
- DNS resolution validation
- Optional HTTP status check
- Threaded performance
- Clean CLI output
- Pipe-friendly

---

## Installation

Clone the repository:

```bash
git clone https://github.com/pangeran-droid/subenum.git
cd subenum
pip install requests
```

## Usage

Basic usage:

```bash
python3 subenum.py -d example.com
```

## Output:

```bash
api.example.com
dev.example.com
mail.example.com
```

## Show HTTP status codes:

```bash
python3 subenum.py -d example.com --status
```

## Output:

```css
api.example.com [200]
dev.example.com [403]
mail.example.com [301]
```

## Pipeline Example

Pipe into other tools:

```bash
python3 subenum.py -d example.com | tee subs.txt
```
```bash
python3 subenum.py -d example.com | httpx
```
```bash
python3 subenum.py -d example.com | nuclei -t templates/
```

## Requirements

- Python 3.8+
- requests

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Do not use against systems without proper permission.

## License

MIT License
