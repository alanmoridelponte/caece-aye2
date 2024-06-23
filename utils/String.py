
def get_username_tags(text: str) -> set:
    tags = set()
    for word in text.split():
        if word.startswith('@'):
            username = word[1:].rstrip('.,!?;')
            tags.add(username)
    return tags