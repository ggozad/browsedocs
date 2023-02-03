import tempfile
from pathlib import Path

import docutils.core
import pycmarkgfm


def get_html(text: str, content_type: str = "text/plain"):
    if content_type == "text/markdown":
        return pycmarkgfm.gfm_to_html(text)
    elif content_type == "text/x-rst":
        return docutils.core.publish_string(text, writer_name="html").decode("utf-8")
    return text


def write_html(html: str):
    tmp_index = Path(tempfile.gettempdir()) / "index.html"
    with open(tmp_index, "w") as f:
        f.write(html)
    return tmp_index
