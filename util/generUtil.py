import random
from datetime import datetime
BINS = {
    "Смешанный BIN": "RND",
    "VISA": "400000",
    "MASTERCARD": "510000",
    "AMERICAN EXPRESS": "340000",
    "DISCOVER": "601100",
}

def luhn(n):
    t = 0
    rev = n[::-1]
    for i, d in enumerate(rev):
        x = int(d)
        if i % 2 == 0:
            x *= 2
            if x > 9: x -= 9
        t += x
    return (10 - (t % 10)) % 10

def genOne(b_key):
    bn = BINS[b_key]
    if bn == "RND":
        bn = random.choice([v for k, v in BINS.items() if v != "RND"])
    ln = 15 if bn.startswith(('34', '37')) else 16
    body = ln - 1 - len(bn)
    rnd = ''.join([str(random.randint(0, 9)) for _ in range(body)])
    pre = bn + rnd
    chk = luhn(pre)
    fn = pre + str(chk)
    y = random.randint(datetime.now().year, datetime.now().year + 5)
    m = random.randint(1, 12)
    exp = f"{m:02d}/{str(y)[-2:]}"
    clen = 4 if bn.startswith(('34', '37')) else 3
    cvv = ''.join([str(random.randint(0, 9)) for _ in range(clen)])
    typ = "Unknown"
    if fn.startswith("4"): typ = "VISA"
    elif fn.startswith("5"): typ = "MASTERCARD"
    elif fn.startswith("3"): typ = "AMERICAN EXPRESS"
    elif fn.startswith("6"): typ = "DISCOVER"
    fmt = f"{fn[:4]} {fn[4:10]} {fn[10:]}" if ln == 15 else ' '.join([fn[i:i+4] for i in range(0, len(fn), 4)])
    return {"n": fn, "f": fmt, "e": exp, "c": cvv, "t": typ}