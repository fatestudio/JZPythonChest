if __name__ == '__main__':
    import xml.etree.ElementTree as ET

    # Sample XML data as a string
    xml_data = """
    <library>
        <book>
            <title>The Great Gatsby</title>
            <author>F. Scott Fitzgerald</author>
            <year>1925</year>
        </book>
        <book>
            <title>1984</title>
            <author>George Orwell</author>
            <year>1949</year>
        </book>
    </library>
    """

    # Step 1: Parse the XML data
    root = ET.fromstring(xml_data)

    # Step 2: Access and print the data
    for book in root.findall("book"):
        title = book.find("title").text
        author = book.find("author").text
        year = book.find("year").text
        print(f"Title: {title}, Author: {author}, Year: {year}")

    # Step 3: Create a new XML element
    new_book = ET.Element("book")
    title = ET.SubElement(new_book, "title")
    title.text = "Brave New World"
    author = ET.SubElement(new_book, "author")
    author.text = "Aldous Huxley"
    year = ET.SubElement(new_book, "year")
    year.text = "1932"

    # Add the new book to the library
    root.append(new_book)

    # Step 4: Write the modified XML to a file
    tree = ET.ElementTree(root)
    with open("updated_library.xml", "wb") as f:
        tree.write(f)

    # Print the newly added book
    print("\nNew Book Added:")
    print(f"Title: {title.text}, Author: {author.text}, Year: {year.text}")
