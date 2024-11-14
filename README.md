# Spaces Speak

## Description

This challenge tests forensic skills of a participant. The challenge hides a key inside a text file where the player is tasked to determine the key and extract the flag form the service.  

## Details

The text file hides a whitespace program (language that contains semantics and syntax of just space, linefeed and newline characters) and upon extracting, a user can then use any online whitespace compiler (https://ideone.com/l/whitespace) to display the key


## Solution Overview

- Download the story file. Analyze its contents to identify whitespace program that is hidden in the story. Extract it and use online compiler such as https://ideone.com/l/whitespace 

### Solution  

Execute the following commands 

1. od -An -tx1 -v encoded_story | tr -s ' ' '\n' | grep -E '09|0a|20' >> hex_dup
    
    - od -An -tx1 -v encoded_story
        - This uses the od (octal dump) command to display the contents of encoded_story. 
        - -An: Suppresses the address (offset) column in the output 
        - -tx1: Displays output in hexadecimal format, one byte per unit
        - -v: Displays all input data, including duplicate lines
    - tr -s ' ' '\n'
        - This uses the tr command to transform the output from od
        - -s: Squeezes repeated characters.     It replaces all spaces with newline characters, effectively putting each hexadecimal byte on a new line
    - grep -E '09|0a|20'
        - This uses grep to filter the output
        - -E: Enables extended regular expressions. It searches for the hexadecimal values '09' (tab), '0a' (newline), or '20' (space)
    - \>> hex_dup
        - This appends the final output to a file named hex_dup

2. xxd -r -p hex_dup > whitespace_program_extracted

    - Command converts hex_dup to whitespace program code that can be put into whitespace compiler to get the key that would give the flag using docker container
    

## Attributes

- author: 'aashayWadkar'
- organization: picoCTF
- event: 18739D - Problem Development 1
