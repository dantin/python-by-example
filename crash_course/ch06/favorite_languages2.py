
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# default through key
# for name, language in favorite_languages:
for name, language in favorite_languages.items():
    print(name.title() + '\'s favorite language is ' +
          language.title() + '.')
