import streamlit as st

# Set page title
st.set_page_config(page_title="MergeMaster")

# Page Header
st.title("MergeMaster")

# Under Construction Notice
st.header("🚧 Under Construction 🚧")

# Introduction and Description
st.markdown("""
Tired of merging your tables using Excel and other programming tools, where you have to remember functions? There should be a simple tool with a few clicks to help you merge tables hassle-free. And here it is! MergeMaster allows you to merge your tables (maximum 5) using a column that you assign as a key column. Not just that, you can do other simple operations before merging such as visualizing your input tables, splitting the column using a separator, visualizing your output table, and downloading it in just a few seconds.
""")

# Key Features
st.subheader("Key Features")
st.markdown("""
- Support for various file formats (.csv, .txt, .xlsx)
- User-friendly interface
- Outputs file in CSV format
""")

# Benefits
st.subheader("Benefits")
st.markdown("""
- Time-saving
- Ease of use
""")

# Feedback Section
st.subheader("We Value Your Feedback")
st.markdown("""
We welcome your feedback and suggestions to improve MergeMaster. Please feel free to create an issue on our GitHub repository to share your thoughts or report any issues you encounter. Your input is invaluable in making MergeMaster better for everyone.

[Create an Issue on GitHub](https://github.com/abzer005/MergeMaster/issues/new)
""")
# Contribution and Follow Us
st.subheader("Contribute and Follow Us")
st.markdown("""
- Interested in contributing? Check out our [GitHub personal page](https://github.com/abzer005).
- For more about our work, visit our [lab's GitHub page](https://github.com/Functional-Metabolomics-Lab).
- Follow us on [Twitter](https://twitter.com/Functional-Metabolomics-Lab) for the latest updates.
""")

# Optional: Footer
st.markdown("---")
st.text("MergeMaster © 2023")
