# EP002 — Free Prediction Market Data with the Polymarket API

**As seen in:** [Deploy or Die — Episode 2](https://www.youtube.com/@deployordie)

Hedge funds pay thousands per month for prediction market data. Polymarket publishes the same signal free via a public REST API. No auth. No account. 20 lines of Python.

---

## What It Does

Queries the Polymarket Gamma API for active markets matching your keywords, sorts by 24-hour volume, and prints current odds + activity.

```
=================================================================
  POLYMARKET SIGNAL — 2026-03-14 16:24
=================================================================

  YES: 49%  |  $  18,268/24h
  Will bitcoin hit $1m before GTA VI?

  YES: 1%   |  $   2,958/24h
  Will OpenAI launch a new consumer hardware product by March 31?

=================================================================
  2 markets matched | Polymarket Gamma API | no key needed
=================================================================
```

---

## Setup

```bash
pip install requests
python3 polymarket_tracker.py
```

No API key. No account. No configuration required.

---

## Customize Your Keywords

Edit the `KEYWORDS` list at the top of the script:

```python
KEYWORDS = [
    r"\bfed\b", r"\bregulation\b", r"\bnvidia\b",
    # Add whatever you want to track
]
```

Whole-word regex matching — no false positives from substrings.

---

## Automate It

Add to crontab to run daily at 7 AM:

```bash
crontab -e
# Add this line:
0 7 * * * /usr/bin/python3 /path/to/polymarket_tracker.py >> /var/log/polymarket.log 2>&1
```

Or deploy free on [Railway](https://railway.com?referralCode=deployordie).

---

## Add Email Alerts

To email yourself when a relevant market is active, add this to `main()`:

```python
import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "you@example.com"
    msg["To"] = "you@example.com"
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login("you@example.com", "your-app-password")
        s.send_message(msg)

# In main(), after building hits:
if hits:
    body = "\n".join(f"{m['question']} — YES: {parse_yes_prob(m):.0%}" for m in hits)
    send_alert("Polymarket Signal", body)
```

---

## More Episodes

→ [deployordie.io](https://deployordie.io)
→ [x.com/deployordie_ai](https://x.com/deployordie_ai)
→ [linkedin.com/company/deployordie](https://www.linkedin.com/company/deployordie/)
