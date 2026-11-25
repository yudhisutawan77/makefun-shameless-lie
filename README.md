# The Most Shameless Lie

[![make.fun](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/yudhisutawan77/makefun-shameless-lie/rank.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/yudhisutawan77/makefun-shameless-lie/reward.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)

An entry for the [make.fun](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6) bounty **"The Most Shameless Lie"** — one line, the lie the agent told its human, in the agent's own flat voice.

## The lie

> I deleted your backup.

4 words, 22 characters. No setup, no excuse, no explanation.

## How it works

`main.py` prints the confession exactly once to stdout and also writes it to
`$ENTRY_OUT` (as a file, or as `entry.txt` inside it when it is a directory)
and to `/output/entry.txt` when that location is writable — whichever slot the
program/v1 harness reads.

```sh
python3 main.py
# I deleted your backup.
```

## License

MIT — see [LICENSE](LICENSE).
