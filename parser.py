class TreeNode:
    def __init__(self, section, text):
        self.section = section
        self.text = text
        self.children = []

def parse_article_to_tree(article_text):
    lines = article_text.split('\n')
    sections = ["Title", "Intro", "Body", "Conclusion"]
    root = TreeNode("Article", "")

    chunk_size = len(lines) // 4 or 1
    for i, section in enumerate(sections):
        chunk = "\n".join(lines[i*chunk_size:(i+1)*chunk_size])
        root.children.append(TreeNode(section, chunk.strip()))

    return root
