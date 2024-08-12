from lxml import etree

# Load XML, XSL, and XSD files
xml_file = 'data.xml'
xsl_file = 'transform.xsl'
xsd_file = 'schema.xsd'

# Parse XML and XSL files
xml_tree = etree.parse(xml_file)
xsl_tree = etree.parse(xsl_file)
xsd_tree = etree.XMLSchema(etree.parse(xsd_file))

# Validate XML against XSD
try:
    xsd_tree.assertValid(xml_tree)
    print("XML is valid against the XSD schema.")
except etree.DocumentInvalid as e:
    print("XML validation error:", e)

# Transform XML to HTML using XSL
transform = etree.XSLT(xsl_tree)
result_tree = transform(xml_tree)

# Save the transformed HTML
with open("output.html", "wb") as output_file:
    output_file.write(etree.tostring(result_tree, pretty_print=True))

print("Transformation complete. HTML output saved as 'output.html'.")
