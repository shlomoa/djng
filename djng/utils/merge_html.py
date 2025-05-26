'''
Script for merging two html files, first is the pivot and the other with overrides.

Usage example:
if __name__ == "__main__":
    # Merge file2.html into file1.html, write result to merged.html
    merger = HtmlMerger("file1.html", "file2.html", "merged.html")
    merger.merge()
    print("Files merged successfully.")
'''

from bs4 import BeautifulSoup

class HtmlMerger:
    """
    Merges two full HTML documents into a single HTML file.
    
    The first file acts as the base (pivot), and the second is merged into it.
    Duplicate tags in the <head> are avoided based on tag name and attributes.
    """
    
    def __init__(self, base_file: str, merge_file: str, output_file: str):
        """
        Initializes the HtmlMerger instance.

        Args:
            base_file (str): Path to the base HTML file.
            merge_file (str): Path to the HTML file to be merged into the base.
            output_file (str): Path to the resulting merged HTML output.
        """
        self.base_file = base_file
        self.merge_file = merge_file
        self.output_file = output_file
        self.soup1 = None  # Parsed base HTML document
        self.soup2 = None  # Parsed HTML document to merge

    def load_files(self):
        """
        Loads and parses the base and merge HTML files using BeautifulSoup.
        """
        with open(self.base_file, "r", encoding="utf-8") as f1, open(self.merge_file, "r", encoding="utf-8") as f2:
            self.soup1 = BeautifulSoup(f1, "html.parser")
            self.soup2 = BeautifulSoup(f2, "html.parser")

    def is_duplicate(self, tag, existing_tags) -> bool:
        """
        Checks if a tag is a duplicate of any existing tags in the base.

        Args:
            tag (Tag): A BeautifulSoup Tag object to check.
            existing_tags (list): List of existing Tag objects in the base.

        Returns:
            bool: True if a duplicate exists, False otherwise.
        """
        for existing in existing_tags:
            if tag.name == existing.name and tag.attrs == existing.attrs:
                return True
        return False

    def merge_head(self):
        """
        Merges the <head> section of the second HTML into the base,
        avoiding duplicates based on tag name and attributes.
        """
        if self.soup1.head and self.soup2.head:
            for tag in self.soup2.head.contents:
                if tag.name and not self.is_duplicate(tag, self.soup1.head.find_all(tag.name)):
                    self.soup1.head.append(tag)

    def merge_body(self):
        """
        Merges the <body> content of the second HTML into the base.
        """
        if self.soup1.body and self.soup2.body:
            for content in self.soup2.body.contents:
                self.soup1.body.append(content)

    def write_output(self):
        """
        Writes the merged HTML content to the specified output file.
        """
        with open(self.output_file, "w", encoding="utf-8") as out:
            out.write(self.soup1.prettify())

    def merge(self):
        """
        Executes the full merge process: load → merge <head> → merge <body> → write output.
        """
        self.load_files()
        self.merge_head()
        self.merge_body()
        self.write_output()
