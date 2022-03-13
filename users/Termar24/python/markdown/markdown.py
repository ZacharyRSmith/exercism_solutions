
def _does_start_with_header(line):
    for i in range(1, 7):
        if line.startswith(("#" * i) + " "):
            return True
    return False


def parse(markdown):
    """Parses a markdown text and returns the associated HTML text

        :param markdown: str The Markdown text to convert
        :return: str HTML text after translation is done

    A function that takes a given string with Markdown syntax, translate headers, 
    unordered lists, paragraphs, italics and bold text to HTML syntax and returns it as a string.
    """
    
    lines = markdown.splitlines()   # lines to convert
    html_lines = ""                 # converted lines
    list_in_progress = False        # checks if an unordered list is in progress

    
    for line in lines:
        # Reset flag for list after a list is done
        if not line.startswith("* ") and list_in_progress:
            list_in_progress = False
            
        # Headers
        if _does_start_with_header(line):
            header, line = line.split(" ", maxsplit=1)
            line = f"<h{len(header)}>{line}</h{len(header)}>"

        # Unordered Lists
        elif line.startswith("* "):
            line = line.removeprefix("* ")
            line = f"<li>{line}</li>"
            if not list_in_progress:
                # Start unordered list
                line = f"<ul>{line}</ul>"
                list_in_progress = True
        
            else:
                # Cut old end of unordered list "</ul>"
                html_lines = html_lines.removesuffix("</ul>")
                line = f"{line}</ul>"

        # Paragraphs
        else:
            line = f"<p>{line}</p>"

        # Bold
        while line.count("__") >= 2:
            (start, __, tail) = line.partition("__")
            (middle, __, tail) = tail.partition("__")
            line = f"{start}<strong>{middle}</strong>{tail}"

        # Italic
        while line.count("_") >= 2:
            if line.count("__") == 1:
                # False positive
                break
            
            (start, __, tail) = line.partition("_")
            (middle, __, tail) = tail.partition("_")
            line = f"{start}<em>{middle}</em>{tail}"
    
        html_lines += line

    return html_lines
