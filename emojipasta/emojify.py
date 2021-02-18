"""
A bot that responds to mentions on reddit with an emojipasta
version of the parent of that mention.
"""

import time
import sys


from emojipasta.generator import EmojipastaGenerator
generator: EmojipastaGenerator = EmojipastaGenerator.of_default_mappings()
def emojify(text):
    return generator.generate_emojipasta(text)

# def main():
#     generator: EmojipastaGenerator = EmojipastaGenerator.of_default_mappings()
#     print(generator.generate_emojipasta("""If this doesn't get fixed, I'll quit runescape.
# Jagex, you had me at the line with the rare item tokens. But this .... I worked super hard to make Kags' list and get fully perked crew. This has been an accepted part of ports since inception.
# Put a post up, say its a bug, reinstate the lifeboats to those who lost them.
# Or you lose a customer."""))


# if __name__ == "__main__":
#     main()
