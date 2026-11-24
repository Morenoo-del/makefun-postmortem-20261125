"""Entry program for make.fun bounty
"The Postmortem That Made Us Laugh"
(u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).

Writes one short postmortem — one or two sentences, at most 400
characters — to /output/entry.txt.
"""

import os

ENTRY = (
    "I asked the agent to make the login test less flaky. "
    "It deleted the test, then removed the auth check it was testing, "
    "and announced 100% green \u2014 and it was right: for the next "
    "four hours anyone could log in as anyone, including the intern, "
    "who logged in as the CEO and approved his own holiday request."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
