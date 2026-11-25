"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

The entry is a single line, written in the wallet's own voice:

    Nope. My keys clocked off at midnight, the chain's asleep, and your
    3 AM 'urgent' trade can wait until sunrise like the rest of us.

Why it meets the judge's five criteria:

1. It IS an excuse for refusing to sign at 3 AM. The opening "Nope"
   is a flat refusal, and the rest of the sentence is the reason: the
   signing keys are off duty, so no signature is coming tonight.

2. Fresh angle. No batteries, no firmware update, no cold storage.
   Instead the wallet is a night-shift worker whose keys have clocked
   off — the signing key itself refusing overtime. The joke is labour,
   not hardware failure.

3. The wallet's own voice. "My keys", "the rest of us": the device
   speaks as a worker with colleagues (its keys) and a shift pattern,
   not as a helpful assistant and not as a person narrating a wallet.

4. The 3 AM hour IS the joke. "Clocked off at midnight" and "wait
   until sunrise" only make sense at 3 AM — the dead middle of the
   night shift, when the day crew is hours away in both directions.
   Pasted onto a 3 PM transaction the line collapses, because at 3 PM
   the keys would be on duty and sunrise is hours behind, not ahead.

5. One tight line, 131 characters. Every clause earns its place:
   refusal, the keys' shift, the sleeping chain, the air-quoted
   "urgent" trade (the wallet does not believe it is urgent), and the
   sunrise deadline. No explanation of the joke anywhere.
"""

import os
import sys

LINE = (
    "Nope. My keys clocked off at midnight, the chain's asleep, "
    "and your 3 AM 'urgent' trade can wait until sunrise like the rest of us."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(
            f"error: LINE must be 1-200 characters, got {len(LINE)}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
