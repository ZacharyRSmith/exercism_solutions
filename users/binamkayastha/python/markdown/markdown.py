import re


def _is_list_item(md_line):
    list_item_regex = r'^\* (.*)'
    return re.match(list_item_regex, md_line)


def _get_ul_tag(is_prev_line_a_list_item, is_curr_line_a_list_item):
    if is_curr_line_a_list_item is None:
        if is_prev_line_a_list_item:
            return '</ul>'
        return ''
    elif is_prev_line_a_list_item and not is_curr_line_a_list_item:
        return '</ul>'
    elif not is_prev_line_a_list_item and is_curr_line_a_list_item:
        return '<ul>'
    return ''


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    is_prev_line_a_list_item = False
    for line in lines:
        res += _get_ul_tag(is_prev_line_a_list_item, _is_list_item(line))

        parsed_line = parse_line(line)
        res += parsed_line

        is_prev_line_a_list_item = _is_list_item(line)
    res += _get_ul_tag(is_prev_line_a_list_item, is_curr_line_a_list_item=None)
    return res


def parse_line(original_line: str) -> tuple[str, bool]:
    line = original_line

    line = header_parser(line)
    list_item_regex = r'^\* (.*)'
    line = text_style_parser(list_item_regex, 'li', line)
    line = text_style_parser('__(.*)__', 'strong', line)
    line = text_style_parser('_(.*)_', 'em', line)

    # Order Matters! This has to happen after text_style_parser calls (to
    # detect new tags) but before prepend item (so that the closing </ul>
    # happens before <p> tags)
    if not re.match('<h|<ul|<p|<li', line):
        line = wrap('p', line)

    return line


def header_parser(line: str):
    for i in range(1, 7):
        if line.startswith('#'*i + ' '):
            line = wrap(f'h{i}', line[i+1:])
            break
    return line


def text_style_parser(regex: str, tag: str, line: str) -> str:
    """Replaces regex with html tag. Assumes regex has 1 groups"""
    return re.sub(regex, wrap(tag, r'\g<1>'), line)


def wrap(tag: str, line: str) -> str:
    return f'<{tag}>{line}</{tag}>'

