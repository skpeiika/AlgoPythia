class Node:
    def __init__(self, count, data_name, data_number):
        self.count = count
        self.data_name = data_name
        self.data_number = data_number
        self.next = None


class PhoneBook:
    def __init__(self):
        self.head = None
        self.count = 0  # Initialize count to 0

    def insert(self, str_name, str_number):
        self.count += 1  # Increment count
        new_node = Node(self.count, str_name, str_number)  # Use the updated count
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def delete_entry(self, str_name):
        if self.head is None:
            return  # Empty phone book, nothing to delete

        if self.head.data_name == str_name:
            self.head = self.head.next  # Remove the head node
            self._update_counts()  # Update counts after deletion
            return

        prev_node = self.head
        current_node = self.head.next

        while current_node:
            if current_node.data_name == str_name:
                prev_node.next = current_node.next  # Remove current node
                self._update_counts()  # Update counts after deletion
                return
            prev_node = current_node
            current_node = current_node.next

    def _update_counts(self):
        current_node = self.head
        new_count = 1

        while current_node:
            current_node.count = new_count
            new_count += 1
            current_node = current_node.next

    def search_by_name(self, str_name):
        current_node = self.head
        result = []
        while current_node:
            if current_node.data_name.startswith(str_name):
                result.append([current_node.data_name, current_node.data_number])
            current_node = current_node.next
        return result

    def print_list(self):
        current_node = self.head
        print("+--------------------------------------+")
        print("|  #  | Name            | Number       |")
        print("|-----|-----------------|--------------|")
        while current_node:
            print(
                f"| {str(current_node.count).center(3)} | "
                f"{current_node.data_name.ljust(15)} | "
                f"{current_node.data_number.center(12)} |")
            current_node = current_node.next
        print("+--------------------------------------+")


def test():
    phone_book = PhoneBook()

    phone_book.insert('John Smith', '7801111111')
    phone_book.insert('Jane', '7802222222')
    phone_book.insert('John Tang', '7803333333')
    phone_book.insert('Adam', '7804444444')
    phone_book.insert('Alex', '7805555555')
    phone_book.insert('Anna', '7806666666')
    phone_book.insert('John', '7807777777')
    phone_book.insert('Lisa', '7808888888')
    phone_book.insert('Mark', '7809999999')

    phone_book.print_list()

    # phone_book.insert('NAME', '7800000000')

    # phone_book.print_list()

    # phone_book.delete_entry("John Smith")

    # phone_book.print_list()


test()
