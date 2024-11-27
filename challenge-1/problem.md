# Coupon Mishap

- Namespace: picoctf/18739f24
- ID: coupon_mishap
- Type: custom
- Category: Web Exploitation
- Points: 100
- Templatable: yes
- MaxUsers: 1

## Description

We have a coupon checkout system implemented where each coupon can be used only once. Can you be greedy and see if you can apply the coupon TWICE?

## Details

The website is running {{link_as('/', 'here')}}


## Hints

- Hmmm, its weird that checkout takes a long time when valid coupon is applied.
- Seems like there is a lot of time difference between check and usage

## Solution Overview

1. The solution involves writing a script to obtain a coupon and send multiple requests at the same time to use that coupon.
2. As the server takes time processing and applying a valid coupon, there is high chance multiple requests bypass the check of coupon validity and allow to be utilized twice giving the flag
 

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

- Building Web Exploits, understand what it takes to create the vulnerability.
- TOCTOU vulnerability

## Tags

- python

## Attributes

- author: Aashay Wadkar
- organization: 18739
- event: 18739 Problem Development 2