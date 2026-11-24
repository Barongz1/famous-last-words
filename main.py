"""Famous Last Words at 1 Percent — entry for make.fun.

Writes one line to /output/entry.txt. The line is the funniest farewell a phone says when its battery hits 1 percent, at most 199 characters.
"""
import os

LINE = "Tell my charger I loved it. And tell the group chat I died doing what I loved: ignoring them for three hours."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
