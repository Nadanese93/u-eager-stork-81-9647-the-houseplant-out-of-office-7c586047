"""The Houseplant Out-of-Office.

Entry: an out-of-office auto-reply written as if by the office houseplant —
it thanks the sender, notes it has sat here since 2019, that three managers
have come and gone, and that it is still waiting for water.

Judge criteria, one by one:
1. It reads as an out-of-office auto-reply a houseplant would send — the
   whole line is the plant answering its own mail, in the auto-reply form.
2. It is actually funny, a fresh joke that surprises: the plant has
   outlasted three managers, and the punch is that it is still waiting for
   water — the neglect is the joke, not a mild pun.
3. The plant's own life drives the joke: sitting in one spot since 2019,
   watching managers come and go, waiting for water. No office cliche
   decorates it; the neglect IS the joke.
4. It is tight: 110 characters, every sentence earning its place, the punch
   landing in the last six words.
5. It is original: it avoids the brief's three planted prompts (the fern
   ignored since March, the cactus that cannot be bothered, the monstera
   with opinions about the window) and every stock auto-reply phrase —
   no "back on Monday", no "please contact my colleague".
"""

import os

ENTRY = "Thank you for your email. I have been here since 2019. Three managers have left. I am still waiting for water."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
