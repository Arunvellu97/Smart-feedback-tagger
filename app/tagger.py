from typing import List

KEYWORDS = {
    "bug": ["error", "crash", "failed", "exception", "bug", "wrong", "not working"],
    "feature_request": ["please add", "please include", "feature", "would like", "add support", "can you add"],
    "praise": ["love", "great", "awesome", "good", "excellent", "nice", "thanks", "thank you"]
    
}

def keyword_tagger(message: str) -> List[str]:
    msg = message.lower()
    tags = set()
    # simple contains checks (can be improved with tokenization)
    for tag, keywords in KEYWORDS.items():
        for kw in keywords:
            if kw in msg:
                tags.add(tag)
                break
    if not tags:
        tags.add("other")
    return list(tags)