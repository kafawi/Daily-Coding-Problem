from typing import Dict, Iterable, List

class Trie:
    class Node:
        is_terminated_ :bool
        child_paths_   :Dict[str, 'Node']  # python does not have a dedicates character type, alternativ we could use int and convert with chr() and ord()

        def __init__(self):
            self.is_terminated_ = False
            self.child_paths_ = dict()

        
        def str_(self, offset=""):
            s =  "("
            s +=  "+" if self.is_terminated_ else "-"
            s += ": [\n" + offset
            for key, val in self.child_paths_.items():
                s += "  " + str(key) + " : " + val.str_("  " + offset) + "\n" + offset
            s += "])" 
            return s
        
        def __str__(self):    
            return self.str_()

    def __init__(self):
        self.root_ = self.Node()
    
    def __str__(self):
        return str(self.root_)

    def add_phrase(self, phrase: str):
        node = self.root_
        for c in phrase:
            if c not in node.child_paths_:
                next_node = self.Node() 
                node.child_paths_[c] = self.Node()
            node = node.child_paths_[c]
        node.is_terminated_ = True
    
    def travers_preorder(self, node :Node, prefix :str, fn: callable):
        fn(node, prefix)
        for ch, child in node.child_paths_.items():
            self.travers_preorder(child, prefix + ch, fn)
    
    def get_node(self, phrase: str):
        node = self.root_
        for c in phrase:
            if c not in node.child_paths_:
                return None
            node = node.child_paths_[c]
        return node


class AutocompleteSystem:
    
    def __init__(self, dictionary: Iterable[str]):
        self.trie_ = Trie()
        for entry in dictionary:
            self.trie_.add_phrase(entry)

    def get_autocomplete_list(self, s :str) -> List[str]:
        bucket = []
        sub_trie = self.trie_.get_node(s);
        if sub_trie:
          self.trie_.travers_preorder(sub_trie, s, lambda n, s: bucket.append(s) if n.is_terminated_ else None )
        return bucket


if __name__=="__main__":
    autocomplete = AutocompleteSystem(['dog', 'deer', 'deal'])
    print(autocomplete.trie_) 
    print(autocomplete.get_autocomplete_list("de"))
    assert(autocomplete.get_autocomplete_list("de"), ['deer', 'deal'])
    
