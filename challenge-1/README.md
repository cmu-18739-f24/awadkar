# coupon-mishap
Second CTF Problem for Hacking and Offensive Security Course

## Keywords
- Web Exploitation
- TOCTOU Vulnerability


## Set up steps

1) git clone this repository

2) cd into the repo and run the following command to set-up the docker
```
docker build -t coupon-mishap .
```

3) To start the server, run the following command
```
docker run -it coupon-mishap
```

4) You should now have access to the server on
```
http://<Docker ip>:5000
```


## Solution Approach

- Finding the vulnerability : Applying valid coupon takes processing time. Possible TOCTOU Vulnerability.
- Write python script to obtain coupon, and process coupon multiple times by requesting /process endpoint
- Will find flag in the error message.    