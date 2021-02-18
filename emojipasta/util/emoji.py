"""
Common emoji code.
"""

import emoji
EMOJIS = emoji.UNICODE_EMOJI.values()

def is_emoji(c):
    return c in EMOJIS
