with open('哈工大5.jpg', 'rb') as src_file:
    with open('copy哈工大5.jpg', 'wb') as target_file:
        target_file.write(src_file.read())
