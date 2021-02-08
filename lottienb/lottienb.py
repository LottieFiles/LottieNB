from IPython.display import display, HTML
from IPython.core.magic import register_line_magic
from html import escape


def __loadjs__():
    display(HTML('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>'))


@register_line_magic
def render_json(data, width=300, height=300):
    __loadjs__()
    js = f'<lottie-player ' \
         f'src="{escape(data)}" ' \
         f'background="transparent" ' \
         f'speed="1" ' \
         f'style="width: {width}px; height: {height}px;" ' \
         f'loop controls autoplay>' \
         f'</lottie-player>'

    display(HTML(js))


@register_line_magic
def render_file(filepath, width=300, height=300):
    with open(filepath, "r") as f:
        s = f.read()
        render_json(s, width=width, height=height)


@register_line_magic
def render_url(url, width=300, height=300):
    render_json(url, width=width, height=height)
