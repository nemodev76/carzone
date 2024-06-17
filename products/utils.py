
import bleach

ALLOWED_TAGS = [
    'p', 'b', 'i', 'u', 'a', 'ul', 'ol', 'li', 'strong', 'em', 'br', 'blockquote', 'pre', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
]

ALLOWED_ATTRIBUTES = {
    'a': ['title'],
    # 'img': ['src', 'alt', 'title'],
}

def sanitize_html(description):
    return bleach.clean(description, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, strip=True)
