from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str | None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.props = props or {}
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        if self.tag is None:
            return self.value

        props_html = self.props_to_html()
        if props_html:
            props_html = " " + props_html
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag!r}, value={self.value!r}, props={self.props!r})"
