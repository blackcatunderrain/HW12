def save_picture(picture) -> str:
    file = picture.filename
    picture.save(f'./uploads/images/{file}')
    return f'./uploads/images/{file}'
