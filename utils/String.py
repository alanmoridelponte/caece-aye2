from models.Post import Post

def get_username_tags(text: str) -> set:
    tags = set()
    for word in text.split():
        if word.startswith('@'):
            username = word[1:].rstrip('.,!?;')
            tags.add(username)
    return tags

def generate_post_ascii(post_title, post_text, likes):
    border = '+' + '-'*28 + '+'
    post_header = '| {:<26} |'.format(post_title)
    padding = '| {:<26} |'.format('')
    
    post_lines = post_text.split('\n')
    formatted_lines = []
    
    for line in post_lines:
        while len(line) > 26:
            formatted_lines.append('| {:<26} |'.format(line[:26]))
            line = line[26:]
        formatted_lines.append('| {:<26} |'.format(line))

    post_body = '\n'.join(formatted_lines)
    
    likes_line = '| Likes: {:<19} |'.format(likes)
    return f"{border}\n{post_header}\n{padding}\n{post_body}\n{padding}\n{likes_line}\n{border}"