import os
import os.path
import re
from dataclasses import dataclass

import hyperpython as h
import markdown

SRC_URL = "https://github.com/RoGryza/python-exercises"


@dataclass
class Category:
    name: str
    display_name: str


def main():
    out = "build"
    os.makedirs("build", exist_ok=True)
    categories = []

    with os.scandir("ex") as it:
        for entry in it:
            if not entry.is_file() or not entry.name.endswith(".md"):
                print(f"WARNING: skipping file {entry.path}")
                continue

            with open(entry.path) as f:
                category = Category(
                    name=entry.name.split(".")[0],
                    display_name=f.readline()[2:].strip(),
                )
                categories.append(category)
            with open(os.path.join(out, category.name + ".html"), "w") as f:
                dom = category_page(category, entry.path)
                f.write(str(dom))

    with os.scandir("static") as it:
        for entry in it:
            with open(os.path.join(out, entry.name), "w") as f:
                f.write(open(entry.path).read())

    with open(os.path.join(out, "index.html"), "w") as f:
        dom = index(categories)
        f.write(str(dom))


def standard_page(title, body):
    return h.h("html")[
        h.head()[
            h.meta(charset="UTF-8"),
            h.meta(name="viewport", content="width=device-width, initial-scale=1"),
            h.title(title),
            h.link(rel="stylesheet", href="style.css"),
            h.link(rel="stylesheet", href="pygments.css"),
        ],
        h.body()[
            body,
            h.footer()[
                h.safe(
                    r'<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />Esta obra está licenciada sob uma <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Licença Internacional Creative Commons Attribution-ShareAlike 4.0</a>.'
                ),
                h.p(h.a("View Source", href=SRC_URL)),
            ],
        ],
    ]


def index(categories):
    def render_category(cat):
        return h.li(h.a(href=cat.name + ".html")[cat.display_name])

    return standard_page(
        "Exercícios de Python",
        h.ul(
            children=[
                render_category(cat) for cat in sorted(categories, key=lambda c: c.name)
            ]
        ),
    )


PYTHON_LINK_RE = re.compile(r"https://docs\.python\.org/3/library/functions.html#(\S+)")


def category_page(category, filepath):
    raw = PYTHON_LINK_RE.sub(
        lambda match: "[{}]({})".format(match.group(1), match.group(0)),
        open(filepath).read(),
    )
    rendered = markdown.markdown(
        raw,
        output_format="html5",
        extensions=["admonition", "codehilite", "fenced_code", "sane_lists"],
        extension_configs={"codehilite": {"guess_lang": False}},
    )
    return standard_page(
        f"Exercícios de Python - {category.display_name}", h.safe(rendered)
    )


if __name__ == "__main__":
    main()
