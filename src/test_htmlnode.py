import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_neq(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "my-class"})
        node2 = HTMLNode(tag="div", value="Hello", props={"class": "different-class"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "my-class"})
        expected_repr = "HTMLNode(tag='div', value='Hello', children=[], props={'class': 'my-class'})"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_with_children(self):
        child_node = HTMLNode(tag="span", value="Child", props={"style": "color: red;"})
        node = HTMLNode(
            tag="div", value="Hello", children=[child_node], props={"class": "my-class"}
        )
        expected_repr = "HTMLNode(tag='div', value='Hello', children=[HTMLNode(tag='span', value='Child', children=[], props={'style': 'color: red;'})], props={'class': 'my-class'})"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HTMLNode(
            tag="div", value="Hello", props={"class": "my-class", "id": "my-id"}
        )
        expected_props_html = 'class="my-class" id="my-id"'
        self.assertEqual(node.props_to_html(), expected_props_html)

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="div", value="Hello")
        expected_props_html = ""
        self.assertEqual(node.props_to_html(), expected_props_html)
