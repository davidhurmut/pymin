import ast, keyword, builtins

class Renamer(ast.NodeTransformer):
    def __init__(self):
        self.counter = 0
        self.map = {}
        self.reserved = set(keyword.kwlist + dir(builtins))
    def _new_name(self):
        n = self.counter
        name = ""
        while True:
            name = chr(ord("a") + (n % 26)) + name
            n //= 26
            if n == 0: break
        self.counter += 1
        return name
    def get_name(self, old):
        if old in self.reserved: return old
        if old not in self.map: self.map[old] = self._new_name()
        return self.map[old]
    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Store, ast.Load, ast.Del)):
            node.id = self.get_name(node.id)
        return node
    def visit_FunctionDef(self, node):
        node.name = self.get_name(node.name)
        self.generic_visit(node)
        return node
    def visit_ClassDef(self, node):
        node.name = self.get_name(node.name)
        self.generic_visit(node)
        return node
    def visit_arg(self, node):
        node.arg = self.get_name(node.arg)
        return node
    def visit_Import(self, node):
        for alias in node.names: alias.asname = self.get_name(alias.name)
        return node
    def visit_ImportFrom(self, node):
        for alias in node.names: alias.asname = self.get_name(alias.name)
        return node

def minify(source: str) -> str:
    tree = ast.parse(source)
    tree = Renamer().visit(tree)
    ast.fix_missing_locations(tree)
    code = ast.unparse(tree)
    return "".join(line.strip() for line in code.splitlines() if line.strip())
