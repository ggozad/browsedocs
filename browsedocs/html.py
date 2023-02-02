from pathlib import Path
import tempfile
import markdown


def get_html(text: str):
    return markdown.markdown(text)


def write_html(html: str):
    tmp_index = Path(tempfile.gettempdir()) / "index.html"
    with open(tmp_index, "w") as f:
        f.write(html)
    return tmp_index
