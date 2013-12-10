sspp
====

Super Simple Python Plugins is a minimal framework for implementing plugins in Python programs.  There's no setup
or anything, just create a directory and put the \_\_init\_\_.py file in it (turning the directory into a module).
Any Python source files placed in that directory will be automatically loaded when the module is loaded.  The names
of the plugins will be put in the \_\_all\_\_ list variable.  Beyond that, you can do anything you want with the plugins.

Here's an example of how to use it.  Let's assume that there is a single plugins directory, named (logically enough)
'plugins'.  Submodules should define a callable object named 'register' that will be invoked when the plug-in is loaded,
but it's not required.

    import plugins

    for name in plugins.__all__:
        plugin = getattr(plugins, name)
        try:
            # see if the plugin has a 'register' attribute
            register_plugin = plugin.register
        except AttributeError:
            # raise an exception, log a message, 
            # or just ignore the problem
            pass
        else:
            # try to call it, without catching any errors
            register_plugin()
