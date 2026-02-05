import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is an example of some text")
        self.assertEqual(
            "HTMLNode(tag: p, value: This is an example of some text, children: None, props: None)",
            repr(node),
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_to_html(self):
        node = HTMLNode(
            "a", "This is a webpage", None, {"href": "https://www.google.com"}
        )
        self.assertRaises(NotImplementedError, node.to_html)

    def test_eq_props_to_HTML(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )


if __name__ == "__main__":
    unittest.main()
