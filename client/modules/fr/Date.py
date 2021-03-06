# -*- coding: utf-8-*-
import re
import time

WORDS = ["DATE", "JOUR", "JOURS"]


def handle(text, mic, profile):
    date = time.strftime("%A")
    date = date + ' ' + time.strftime("%d")
    date = date + ' ' + time.strftime("%B")
    date = date + ' ' + time.strftime("%Y")
    mic.say("Nous sommes aujourd'hui le %s " % date)


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bdate|dates|jour|jours\b', text, re.IGNORECASE))
