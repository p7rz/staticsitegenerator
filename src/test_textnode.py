import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_links(self):
        node = TextNode("This is text node", TextType.LINK, "https://www.postimees.ee")
        node2 = TextNode("This is text node", TextType.LINK, "https://www.postimees.ee")
        self.assertEqual(node, node2)

    def test_txt_not_eq(self):
        node = TextNode("This is some text", TextType.TEXT)
        node2 = TextNode("This is some other text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is some text", TextType.TEXT)
        node2 = TextNode("This is some text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_link_not_eq(self):
        node = TextNode("This is text node", TextType.LINK)
        node2 = TextNode("This is text node", TextType.LINK, "https://www.postimees.ee")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
