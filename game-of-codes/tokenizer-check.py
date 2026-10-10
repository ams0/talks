#!/usr/bin/env python3
"""Reproduce every token count on slides 5, 6, 8, 9 and 36 of Life of a token.

The deck serves Llama 3.3 70B, so the counts are measured on Llama 3's own
tokenizer rather than OpenAI's. Meta's tokenizer is a tiktoken BPE with a
128,256-entry vocabulary; meta-llama/* on Hugging Face is gated, so this pulls
the identical vocabulary from an ungated mirror and rebuilds it as a tiktoken
Encoding, checking the vocabulary size and a round-trip before trusting it.

    pip install tiktoken && python3 tokenizer-check.py
"""
import json, sys, urllib.request
import tiktoken

MIRROR = ("https://huggingface.co/NousResearch/Meta-Llama-3-8B-Instruct"
          "/resolve/main/tokenizer.json")

# Meta's pre-tokenizer split pattern, from the llama3 reference implementation.
PAT = (r"(?i:'s|'t|'re|'ve|'m|'ll|'d)"
       r"|[^\r\n\p{L}\p{N}]?\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]+[\r\n]*"
       r"|\s*[\r\n]+|\s+(?!\S)|\s+")


def bytes_to_unicode():
    """The GPT-2 byte-to-printable-character map the vocabulary is stored in."""
    bs = list(range(33, 127)) + list(range(161, 173)) + list(range(174, 256))
    cs, n = bs[:], 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return dict(zip(bs, (chr(c) for c in cs)))


def load_llama3():
    print(f"fetching vocabulary … {MIRROR.split('/resolve')[0].split('/')[-1]}")
    with urllib.request.urlopen(MIRROR) as r:
        tok = json.load(r)
    u2b = {v: k for k, v in bytes_to_unicode().items()}
    ranks = {}
    for s, i in tok["model"]["vocab"].items():
        try:
            ranks[bytes(u2b[ch] for ch in s)] = i
        except KeyError:
            pass  # special tokens, added below
    special = {a["content"]: a["id"] for a in tok.get("added_tokens", [])}

    enc = tiktoken.Encoding("llama3", pat_str=PAT,
                            mergeable_ranks=ranks, special_tokens=special)

    total = len(ranks) + len(special)
    assert total == 128_256, f"expected 128,256 entries, rebuilt {total:,}"
    for probe in ("The nightly ETL job failed.", "Сваки позив", "🎲 Niš"):
        assert enc.decode(enc.encode(probe)) == probe, f"round-trip failed: {probe!r}"
    print(f"rebuilt and verified: {total:,} entries, round-trip clean\n")
    return enc


def split(enc, text):
    return [enc.decode([i]) for i in enc.encode(text)]


def main():
    enc = load_llama3()

    print("SLIDE 5 — the question you actually type")
    q = "why did the nightly ETL job fail on deserialization?"
    ids = enc.encode(q)
    print(f"  {q!r}")
    print(f"  {len(q.split())} words · {len(ids)} tokens")
    print("  " + " | ".join(split(enc, q)))
    wrapped = ("<|start_header_id|>user<|end_header_id|>\n\n" + q +
               "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n")
    n_w = len(enc.encode(wrapped, allowed_special="all"))
    print(f"  wrapped in the chat template: {n_w} tokens "
          f"({n_w - len(ids)} of template)")
    print(f"  slide 13's ratio: 31,212 / {len(ids)} ≈{round(31212 / len(ids)):,}x\n")

    print("SLIDE 6 — a token is not a word")
    s = "The nightly ETL job failed on a deserialization error."
    print(f"  {len(s)} characters · {len(s.split())} words · {len(enc.encode(s))} tokens")
    print("  " + " | ".join(split(enc, s)) + "\n")

    print("SLIDE 8 — what earned an entry")
    for w in ("GPU", "agentgateway", "Kubernetes", "vLLM"):
        ids = enc.encode(w)
        print(f"  {w:14} {len(ids)}  " + " | ".join(split(enc, w)))
    print()

    print("SLIDE 9 — your alphabet sets the price")
    rows = {
        "English":          "Every agent call ends up as tokens on a GPU somewhere.",
        "Srpski (latinica)": "Svaki poziv agenta završava kao tokeni na nekom GPU-u.",
        "Српски (ћирилица)": "Сваки позив агента завршава као токени на неком GPU-у.",
    }
    base = None
    for name, text in rows.items():
        n = len(enc.encode(text))
        base = base or n
        print(f"  {name:20} {len(text)} chars → {n:3} tokens  ({n / base:.2f}×)")
    print()

    print("SLIDE 36 — the die is not one character to the detokenizer")
    ids = enc.encode("🎲")
    print(f"  🎲 is {len(ids)} tokens:")
    for i in ids:
        b = enc.decode_single_token_bytes(i)
        try:
            b.decode("utf-8")
            print(f"    {b!r:22} valid UTF-8")
        except UnicodeDecodeError:
            print(f"    {b!r:22} NOT valid on its own — the server must buffer")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        sys.exit(f"verification failed: {e}")
