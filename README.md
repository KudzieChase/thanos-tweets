# Thanos my tweets.

This script is inspired by this [repository](https://github.com/koenrh/delete-tweets) 

# What you will need!

  - Your twitter history archive. Can be found [here](https://twitter.com/settings/account) 
  - Twitter developer api access - for client secret keys and tokens. Can be found by creating an [app](https://developer.twitter.com/en/apps)
  - Python 3 installed in your machine.
  - A little imagination.

# How to run it.
Well:
  - Clone this repository to your local machine.
  - Create a virtual environment.
  ```sh
$ cd thanos-tweets
$ python3 -m venv venv
$ source venv/bin/acivate
```
  - Install the requirements.
 ```sh
(venv)$ pip install -r requirements.txt
```
 
 - Be sure to paste your twitter API credentials inside the script.. Then,
 - Just Run it if you don't have specific changes you need to make
 
 ```sh
(venv)$ python3 thanos.py -snap all -r reply
```

> I am not responsible for tweets lost due to this script,
> I made it custom to my specific use case.


> Live Long and Prosper!
