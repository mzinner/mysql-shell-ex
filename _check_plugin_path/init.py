# _check_plugin_path/init.py
# --------------------------
# Since this plugin collection is using Python `import` in many places, it
# requires the plugins to be loaded as regular Python modules. For that reason
# an __init__.py file has to be placed in every folder that is referenced by
# a Python `import` and the `import` statements need to use the full path,
# starting with main plugin folder name in the ~/.mysqlsh/plugins directory.
#
# For that reason, the plugin collection needs to be installed in a specific
# directory name. For this plugin collection we have chosen the name 'ext'.
#
# This init.py checks if the plugin is actually installed into a folder called
# 'ext' and prints out an descriptive error if this is not the case.
#
# In order to execute this init.py first, it is placed in a folder named
# '_check_plugin_path'. Since it starts with '_' and plugins in sub-folders
# are sorted by folder name first, it will be loaded first.


import os

# Check if the plugin has been downloaded into a plugin folder called 'ext'
plugin_dir = os.path.split(os.path.split(os.path.dirname(__file__))[0])[1]
if plugin_dir != "ext":
    # If not, log and display an error 
    shell.log("ERROR", "The 'ext' plugin collection must be installed in a "
        "folder named 'ext' in the .mysqlsh/plugins directory. Currently it "
        "is installed in a folder called '{0}'.".format(plugin_dir))
    print("\nERROR: The 'ext' plugin collection must be installed in a "
        "folder named 'ext' in the .mysqlsh/plugins directory. Currently it "
        "is installed in a folder called '{0}'.\n".format(plugin_dir))
