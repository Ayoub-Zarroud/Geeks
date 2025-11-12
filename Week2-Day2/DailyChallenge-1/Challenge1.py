import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0  
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 0

    def get_visible_items(self):
        """Return list of items visible on current page."""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    def go_to_page(self, page_num):
        """Go to specific page (1-based). Raise ValueError if invalid."""
        if not 1 <= page_num <= self.total_pages:
            raise ValueError(f"Page {page_num} is out of range (1–{self.total_pages}).")
        self.current_idx = page_num - 1
        return self  

    def first_page(self):
        self.current_idx = 0
        return self
    def last_page(self):
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1
        return self
    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
    def __str__(self):
        """Display current page items, each on a new line."""
        visible = self.get_visible_items()
        if not visible:
            return "(no items to display)"
        return "\n".join(str(item) for item in visible)
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print("Page 1 visible items:", p.get_visible_items())
    p.next_page()
    print("Page 2 visible items:", p.get_visible_items())
    p.last_page()
    print("Last page visible items:", p.get_visible_items())

    print("\nString representation:")
    print(p)  
    print("\nMethod chaining example:")
    print(p.first_page().next_page().next_page().get_visible_items())

    print("\nBonus chaining example:")
    print(p.first_page().next_page().next_page().next_page().get_visible_items())
    try:
        p.go_to_page(10)
    except ValueError as e:
        print("Error:", e)
    try:
        p.go_to_page(0)
    except ValueError as e:
        print("Error:", e)
