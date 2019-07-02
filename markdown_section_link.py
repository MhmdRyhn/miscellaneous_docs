# python markdown_section_link.py -t "Write Title or SubTitle Here"
# returns -> - [Write Title or SubTitle Here](#write-title-or-subtitle-here)

# or, to get the link text BOLD
# python markdown_section_link.py -t "Write Title or SubTitle Here" -b
# returns -> - [**Write Title or SubTitle Here**](#write-title-or-subtitle-here)


import argparse


def md_section_link(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--title', 
        '-t', 
        required=True, 
        help='Enter the title / sub-title'
    )

    parser.add_argument(
        '--bold', 
        '-b', 
        action='store_true', 
        help='Make the text bold'
    )

    known_args, unknown = parser.parse_known_args(argv)

    link = ('**' if getattr(known_args, 'bold', None) else '').join(['- [', known_args.title, ']('])
    link += ('#' + known_args.title).lower().replace(' ', '-') + ')'
    
    return link


if __name__ == '__main__':
    print(md_section_link())

