

ignore_list = [
        'http://www.varzesh3.com/{{Url}}: 404',
        'http://www.facebook.com/varzesh3: 404',
        'http://taktix.varzesh3.com/: 404',
        'http://www.varzesh3.com/{{ VideoUrl }}: 404',
        'http://www.varzesh3.com/{{ SummaryUrl }}: 404',
        'http://www.varzesh3.com/{{{ Widget.StandingsUrl }}}: 404',
        'http://www.varzesh3.com/{{FilePath}}: 404',
        'http://www.varzesh3.com/{{Path}}: 404',
        'http://www.varzesh3.com/{{Thumb}}: 404',
]


def normalize(message):
    normalized = message
    for ignore in ignore_list:
        if ignore in message:
            normalized = normalized.replace(ignore, ' ')
    return normalized


if __name__ == '__main__':
    print(normalize(        'http://www.varzesh3.com/{{Path}}: 404 http://www.varzesh3.com/{{Thumb}}: 404'))