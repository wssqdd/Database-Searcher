# Database-Searcher

Search for a name or email in different databases stored as files within a folder.

## Description

Database-Searcher is a simple Python tool that scans through multiple text files in a specified folder to find occurrences of a given name or email. It supports case-insensitive search and shows which file and line contains the match.

## Features

- Search across multiple files in a folder.
- Case-insensitive matching.
- Displays filename, line number, and the matching line.
- Easy to use via command line.

## Requirements

- Python 3.x

## Usage

```bash
python database_searcher.py --folder path/to/folder --search "search_term"
