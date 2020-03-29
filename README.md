# Social Network Generator
Creates random social network accounts and status updates in two CSV files

## What it does

Takes five source files in text format and generates two CSV (comma-separated) files with randomly-generated user accounts and status updates for those accounts.

For accounts, each entry includes:

* User ID.
* Email.
* Name.
* Last name.

For status updates, each entry includes:

* Status ID.
* User ID (all existing accounts).
* Status text.

## Usage

```
$ python source_data_generator.py
```

## Source files
The program requires five source files in text format:

* Names (default *names.txt*).
* Last names (default *last_names.txt*).
* Nouns (default *nouns.txt*).
* Verbs (default *verbs.txt*).
* Adjectives (default *adjectives.txt*).

The rules for the source file are simple: One word per line, no punctuation.

## Command line options

All arguments are optional and will use a default value if not included in the command line.

```
optional arguments:
  -h, --help                show this help message and exit
  -nf, --names_file         list of names
  -ln, --last_names_file    list of last names
  -n, --nouns_file          list of nouns
  -a, --adjectives_file     list of adjectives
  -v, --verbs_file          list of verbs
  -af, --accounts_file      user account file
  -sf, --status_file        status file
  -na, --number_of_accounts number of accounts to create
  -ns, --number_of_status   number of status to create
```

## Where to get source files

I found a very extensive collection of nouns, verbs and adjectives here: https://github.com/aaronbassett/Pass-phrase

This repository is an excellent source for names and last names: https://github.com/dominictarr/random-name
