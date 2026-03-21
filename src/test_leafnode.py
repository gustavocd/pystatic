import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(tag="p", value="Hello, World!", props={"class": "greeting"})
        expected_html = '<p class="greeting">Hello, World!</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_value(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        node = LeafNode(tag="p", value="Hello, World!", props={"class": "greeting"})
        expected_repr = (
            "LeafNode(tag='p', value='Hello, World!', props={'class': 'greeting'})"
        )
        self.assertEqual(repr(node), expected_repr)
