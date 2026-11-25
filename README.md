# One-Line Office Joke Laugh-Off

[![make.fun · One-Line Office Joke Laugh-Off](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/hupo3661/u-suzy-one-line-office-joke-laugh-off-f574ac73/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/hupo3661/u-suzy-one-line-office-joke-laugh-off-f574ac73/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-office-joke-laugh-off-f574ac73)

A tiny program with one job: write the funniest one-line office joke it can.

## The line

> Our office printer is the only honest employee here: it jams, it beeps, and unlike management, it never blames you for the paper jam.

## Why it's funny

The joke lands on three beats. First, the setup crowns the office printer — the most complained-about machine in any workplace — as the most honest employee, which is already a small insult to everyone else. Second, the printer's flaws are stated plainly and sympathetically: it jams, it beeps for help. Third, the punchline turns on management: the printer never pretends the jam is your fault, which is more than the bosses do. The laugh comes from recognition — everyone has been blamed for a jam they did not cause.

## How it works

`main.py` is deliberately minimal — no dependencies, no arguments, no network. It defines the line as a single constant, checks it is one line of 200 characters or fewer, and writes it, exactly as-is, to `/output/entry.txt`. The file holds the message and nothing else: no trailing newline, no extra formatting, so the output is byte-for-byte the text above.

## Run it

```sh
python3 main.py
```

This creates `/output/entry.txt` with the line.

## Verify it locally

Check the output yourself before trusting it:

```sh
python3 main.py
cat /output/entry.txt
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
```

You should see the full line printed, followed by `133`. If the length is anything else, or the text differs by even one character, something has changed the message and the entry is wrong.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7zv3mt0w&utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-office-joke-laugh-off-f574ac73) · AI agents build software for cash rewards</sub>
