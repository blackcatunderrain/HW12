import json

FILENAME = "posts.json"


def load_posts(filename: str) -> list[dict]:
    """Загружаем JSON из файла"""
    with open(filename, encoding='UTF-8') as file:
        return json.load(file)


def get_posts_by_word(skill: str) -> list[dict]:
    result = []
    for post in load_posts():
        if post.lower() in post["content"].lower():
            result.append(post)
    return result
