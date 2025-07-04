# Databricks notebook source


# COMMAND ----------

# # %%sql
# # SELECT * FROM sales WHERE region = 'North America' LIMIT 10; 

# print("Hello, Databricks!")
dbutils.widgets.text("input_name", "Default Value", "Enter your name")

# FETCH the widget value
name = dbutils.widgets.get("input_name")

print(f"Hello, {name}!")


# dbutils.widgets.removeAll()

dbutils.widgets.text(
    name="my_text_widget",
    defaultValue="Hello, Databricks!",
    label="Enter some text below:"
)
text = dbutils.widgets.get("my_text_widget")
print("Value of my_text_widget:", text)

dbutils.widgets.dropdown(
    name="my_dropdown",
    defaultValue="VAN 2",
    choices=["CAR", "VAN 2", "JEEP 3"],
    label="Pick one option from dropdown:"
)
dropdown_value = dbutils.widgets.get("my_dropdown")
print("Value of my_dropdown:", dropdown_value)

dbutils.widgets.combobox(
    name="my_combobox",
    defaultValue="apple",
    choices=["apple", "banana", "cherry"],
    label="Select OR type your fruit:"
)
combo_value = dbutils.widgets.get("my_combobox")
print("Value of my_combobox:", combo_value)

dbutils.widgets.multiselect(
    name="my_multiselect",
    defaultValue="red",
    choices=["red", "green", "blue", "yellow"],
    label="Pick multiple colors:"
)
multi_value = dbutils.widgets.get("my_multiselect")
print("Value of my_multiselect:", multi_value)


# Generate a long string of length exactly 2048
long_string = "a" * 22

dbutils.widgets.text(
    name="long_text_widget",
    defaultValue=long_string,
    label="Testing max length of text widget (2048 chars):"
)

# Now fetch it back:
long_value = dbutils.widgets.get("long_text_widget")
print("Length of long_text_widget value:", len(long_value))


# Generating 1023 options instead of 1024
options_list = [f"Item {i}" for i in range(3)]

dbutils.widgets.dropdown(
    name="large_dropdown",
    defaultValue="Item 1",
    choices=options_list,
    label="Dropdown with many options (demo)"
)

dropdown_large_value = dbutils.widgets.get("large_dropdown")
print("Value of large_dropdown:", dropdown_large_value)



# COMMAND ----------

# MAGIC %sql
# MAGIC %
# MAGIC select 1 as id, 'john' as name, '13th Street. 47 W 13th St, New York, NY 10011' as address

# COMMAND ----------

# DBTITLE 1,North America Sales Analysis
# MAGIC %%sql
# MAGIC SELECT * FROM sales WHERE region = 'North America';

# COMMAND ----------

# ------------------------------------------------------------
# TITLE: Databricks Widgets - Full Exploration Demo
# DESCRIPTION:
#   This notebook demonstrates ALL key features of dbutils.widgets,
#   including:
#     - text widgets
#     - dropdown widgets
#     - combobox widgets
#     - multiselect widgets
#     - how to read widget values
#     - how to remove widgets
#     - edge cases & limits
#
# ------------------------------------------------------------


# ------------------------------------------------------------
# STEP 1 - CLEAN UP ANY OLD WIDGETS
# ------------------------------------------------------------

# This removes all widgets from the notebook.
# Good practice because widgets persist between runs
# unless removed. Stale widgets can cause confusion
# if they keep old values.

dbutils.widgets.removeAll()

# No output here - it's just cleaning house.


# ------------------------------------------------------------
# STEP 2 - CREATE A TEXT WIDGET
# ------------------------------------------------------------

# A text widget allows users to enter free-form text.
# Arguments:
#   name: unique name of the widget
#   defaultValue: initial value shown
#   label: label displayed above the widget

dbutils.widgets.text(
    name="my_text_widget",
    defaultValue="Hello, Databricks!",
    label="Enter some text below:"
)


# ------------------------------------------------------------
# STEP 3 - READ VALUE FROM TEXT WIDGET
# ------------------------------------------------------------

# Use .get() to retrieve the current value of a widget
# by its name.

text_value = dbutils.widgets.get("my_text_widget")
print("Value of my_text_widget:", text_value)


# ------------------------------------------------------------
# STEP 4 - CREATE A DROPDOWN WIDGET
# ------------------------------------------------------------

# A dropdown lets you choose ONE option from a fixed list.
# Arguments:
#   name
#   defaultValue
#   choices (list of strings)
#   label

dbutils.widgets.dropdown(
    name="my_dropdown",
    defaultValue="Option 2",
    choices=["Option 1", "Option 2", "Option 3"],
    label="Pick one option from dropdown:"
)


# ------------------------------------------------------------
# STEP 5 - READ VALUE FROM DROPDOWN
# ------------------------------------------------------------

dropdown_value = dbutils.widgets.get("my_dropdown")
print("Value of my_dropdown:", dropdown_value)


# ------------------------------------------------------------
# STEP 6 - CREATE A COMBOBOX WIDGET
# ------------------------------------------------------------

# A combobox is like a dropdown BUT also allows users
# to type a custom value if their option isn't listed.
# Perfect for flexibility.

dbutils.widgets.combobox(
    name="my_combobox",
    defaultValue="apple",
    choices=["apple", "banana", "cherry"],
    label="Select OR type your fruit:"
)


# ------------------------------------------------------------
# STEP 7 - READ VALUE FROM COMBOBOX
# ------------------------------------------------------------

combo_value = dbutils.widgets.get("my_combobox")
print("Value of my_combobox:", combo_value)


# ------------------------------------------------------------
# STEP 8 - CREATE A MULTISELECT WIDGET
# ------------------------------------------------------------

# Multiselect lets users pick MULTIPLE values from a list.
# Selected values are returned as a comma-separated string.

dbutils.widgets.multiselect(
    name="my_multiselect",
    defaultValue="red",
    choices=["red", "green", "blue", "yellow"],
    label="Pick multiple colors:"
)

# ------------------------------------------------------------
# STEP 9 - READ VALUE FROM MULTISELECT
# ------------------------------------------------------------

multi_value = dbutils.widgets.get("my_multiselect")
print("Value of my_multiselect:", multi_value)

# NOTE:
# The returned value will be:
#   - "red" if only red selected
#   - "red,green" if red and green selected, etc.


# ------------------------------------------------------------
# STEP 10 - TEST MAX LENGTH OF TEXT WIDGET
# ------------------------------------------------------------

# By default, text widgets accept up to 2048 characters.
# We'll test the limit.

# Generate a long string of length exactly 2048
long_string = "a" * 2048

dbutils.widgets.text(
    name="long_text_widget",
    defaultValue=long_string,
    label="Testing max length of text widget (2048 chars):"
)

# Now fetch it back:
long_value = dbutils.widgets.get("long_text_widget")
print("Length of long_text_widget value:", len(long_value))


# ------------------------------------------------------------
# STEP 11 - TRY TO BREAK TEXT LIMIT (should fail or truncate)
# ------------------------------------------------------------

# Now let's intentionally go over the 2048-character limit.

too_long_string = "b" * 3000  # exceeds 2048

dbutils.widgets.text(
    name="too_long_text_widget",
    defaultValue=too_long_string,
    label="Trying to exceed limit (expect errors or clipping):"
)

# Fetch back:
too_long_value = dbutils.widgets.get("too_long_text_widget")
print("Length of too_long_text_widget value:", len(too_long_value))


# ------------------------------------------------------------
# STEP 12 - TEST MAX DROPDOWN OPTIONS
# ------------------------------------------------------------

# Dropdown widgets can have up to 1024 choices.
# We'll test a smaller number for performance.

# Generating 50 options instead of 1024
options_list = [f"Item {i}" for i in range(50)]

dbutils.widgets.dropdown(
    name="large_dropdown",
    defaultValue="Item 0",
    choices=options_list,
    label="Dropdown with many options (demo)"
)

dropdown_large_value = dbutils.widgets.get("large_dropdown")
print("Value of large_dropdown:", dropdown_large_value)


# ------------------------------------------------------------
# STEP 13 - CLEAN UP ALL WIDGETS AGAIN
# ------------------------------------------------------------

# Good practice to remove widgets when done to avoid clutter.

dbutils.widgets.removeAll()

print("All widgets removed. Notebook is clean.")



# COMMAND ----------

# Generating 50 options instead of 1024
options_list = [f"Item {i}" for i in range(50)]

dbutils.widgets.dropdown(
    name="large_dropdown",
    defaultValue="Item 0",
    choices=options_list,
    label="Dropdown with many options (demo)"
)

dropdown_large_value = dbutils.widgets.get("large_dropdown")
print("Value of large_dropdown:", dropdown_large_value)
