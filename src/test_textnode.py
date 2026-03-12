import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_repr = "TextNode(text='This is a text node', text_type=<TextType.BOLD: 'bold'>, url=None)"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_with_url(self):
        node = TextNode("This is a link", TextType.LINK, url="https://example.com")
        expected_repr = "TextNode(text='This is a link', text_type=<TextType.LINK: 'link'>, url='https://example.com')"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
