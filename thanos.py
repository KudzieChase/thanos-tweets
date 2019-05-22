#!/usr/bin/env python

import argparse
import csv
import sys
import time
import os
import re
from datetime import date
import twitter
from dateutil.parser import parse

__author__ = "Kudzai Chasinda"

"""This script will be used to delete almost all tweets from your TL"""

opening_message = "You could not live with your own failure. Where did that bring you? Back to me.\n"

pattern_android = r"Android|android|ANDROID"
pattern_retrofit = r"retrofit|Retrofit"
pattern_kotlin = r"kotlin|Kotlin"


def find_match(pattern, text_string):
    res = re.findall(pattern, text_string)
    return len(res) > 0


def does_match(pattern, text_string):
    p = re.compile(pattern, re.IGNORECASE)
    res = p.match(text_string)
    return res is not None


def delete(api, r):
    today = date.today().strftime("%Y-%m-%d")
    with open("tweets.csv") as file:
        count = 0

        for row in csv.DictReader(file):
            tweet_id = int(row["tweet_id"])
            tweet_date = parse(row["timestamp"], ignoretz=True).date()
            tweet_content = row["text"]

            if today != "" and tweet_date >= parse(today).date():
                continue

            if find_match(pattern_android, tweet_content) \
                    or find_match(pattern_retrofit, tweet_content) \
                    or find_match(pattern_kotlin, tweet_content):
                continue

            if (r == "retweet" and row["retweeted_status_id"] == "" or
                    r == "reply" and row["in_reply_to_status_id"] == ""):
                continue

            try:
                print("Snapped tweet #{0} tweeted on ({1})".format(
                    tweet_id, tweet_date))

                api.DestroyStatus(tweet_id)
                count += 1
                time.sleep(0.5)

            except twitter.TwitterError as err:
                print("Exception: %s\n" % err.message)

    print("I am innevitable! \n")

    print(
        "Aaaah, deleted {0} tweets. Balance! As all things should be!".format(count))


def error(msg, exit_code=1):
    sys.stderr.write("Error: %s\n" % msg)
    exit(exit_code)


def main():
    parser = argparse.ArgumentParser(description="Thanos snappin' old tweets.")
    parser.add_argument("-snap", dest="snap", choices=["all"], required=True,
                        help="Snap away all tweets from today till the beginning")  # TODO add choices for half
    parser.add_argument("-r", dest="restrict", choices=["reply", "retweet"],
                        help="Restrict to either replies or retweets")

    args = parser.parse_args()

    # Add your twitter keyes here
    api = twitter.Api(consumer_key="enter_your_own_key_here",
                      consumer_secret="enter_your_own_secret_here",
                      access_token_key="enter_your_own_key_here",
                      access_token_secret="enter_your_own_secret_here")

    print(opening_message)

    delete(api, args.restrict)


if __name__ == "__main__":
    main()
