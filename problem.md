# Spaces Speak

- Namespace: picoctf/18739f24
- ID: spaces-speak
- Type: custom
- Category: Forensics
- Points: 1
- Templatable: no
- MaxUsers: 1

## Description

We have vault to crack, but the key is hidden in a story. Can you do anything to crack this key?

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

The story code can be downloaded {{url_for("encoded_story", "here")}}.

## Hints

- Why does the story file look weird? Maybe there is some clues in the spaces. 
- Is there some weird programming language that exists for this?

## Solution Overview

Download the story file. Analyze its contents to identify whitespace program that is hidden in the story. Extract it and use online compiler such as https://ideone.com/l/whitespace 

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Examining files to extract hidden information

## Tags

- python

## Attributes

- author: 'aashayWadkar'
- organization: picoCTF
- event: 18739D - Problem Development 1
