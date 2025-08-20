class BookNode:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None

    def add_book(self, title, author):
        new_node = BookNode(title, author)
        new_node.next = self.head
        self.head = new_node

    def find_book(self, title, author=None):
        current = self.head
        while current:
            if current.title.lower() == title.lower():
                if author is None or current.author.lower() == author.lower():
                    return current
            current = current.next
        return None

    def search_by_title(self, title):
        results = []
        current = self.head
        while current:
            if title.lower() in current.title.lower():
                results.append(current)
            current = current.next
        return results

    def search_by_author(self, author):
        results = []
        current = self.head
        while current:
            if author.lower() in current.author.lower():
                results.append(current)
            current = current.next
        return results

    def display_books(self):
        current = self.head
        print("Inventory:")
        while current:
            status = "Available" if current.available else "Borrowed"
            print(f"'{current.title}' by {current.author} - {status}")
            current = current.next
        print()

class ActionStack:
    def __init__(self):
        self.stack = []

    def push(self, action, book):
        self.stack.append((action, book))

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

class Library:
    def __init__(self):
        self.inventory = Inventory()
        self.undo_stack = ActionStack()

    def add_book(self, title, author):
        self.inventory.add_book(title, author)

    def borrow_book(self, title, author=None):
        book = self.inventory.find_book(title, author)
        if book and book.available:
            book.available = False
            self.undo_stack.push('borrow', book)
            print(f"Borrowed '{book.title}' by {book.author}")
        elif book and not book.available:
            print(f"Book '{book.title}' by {book.author} is already borrowed.")
        else:
            print("Book not found.")

    def return_book(self, title, author=None):
        book = self.inventory.find_book(title, author)
        if book and not book.available:
            book.available = True
            self.undo_stack.push('return', book)
            print(f"Returned '{book.title}' by {book.author}")
        elif book and book.available:
            print(f"Book '{book.title}' by {book.author} was not borrowed.")
        else:
            print("Book not found.")

    def undo(self):
        if self.undo_stack.is_empty():
            print("No actions to undo.")
            return

        action, book = self.undo_stack.pop()
        if action == 'borrow':
            book.available = True
            print(f"Undo borrow: '{book.title}' is now available.")
        elif action == 'return':
            book.available = False
            print(f"Undo return: '{book.title}' is now borrowed.")

    def search_title(self, title):
        results = self.inventory.search_by_title(title)
        print(f"Search results for title containing '{title}':")
        for b in results:
            status = "Available" if b.available else "Borrowed"
            print(f"'{b.title}' by {b.author} - {status}")
        if not results:
            print("No books found.")
        print()

    def search_author(self, author):
        results = self.inventory.search_by_author(author)
        print(f"Search results for author containing '{author}':")
        for b in results:
            status = "Available" if b.available else "Borrowed"
            print(f"'{b.title}' by {b.author} - {status}")
        if not results:
            print("No books found.")
        print()

    def show_inventory(self):
        self.inventory.display_books()

lib = Library()

lib.add_book("The Hobbit", "J.R.R. Tolkien")
lib.add_book("The Fellowship of the Ring", "J.R.R. Tolkien")
lib.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
lib.add_book("1984", "George Orwell")

lib.show_inventory()

lib.borrow_book("The Hobbit")
lib.borrow_book("1984")

lib.show_inventory()

lib.return_book("The Hobbit")

lib.show_inventory()

lib.undo()
lib.show_inventory()

lib.undo()
lib.show_inventory()

lib.search_title("the")
lib.search_author("Tolkien")
