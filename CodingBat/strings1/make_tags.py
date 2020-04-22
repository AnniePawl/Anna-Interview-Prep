# Given tag and word strings, create HTML string with tags around it


def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"


print(make_tags('p', 'Hello, World'))  # <p>Hello World</p>
print(make_tags('h1', 'Breaking News!'))  # <h1>Breaking News</p>
