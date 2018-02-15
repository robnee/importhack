# importhack

### Pythonista iOS hack for running multi-module projects directly from Working Copy file provider

[Pythonista](http://omz-software.com/pythonista) and [Working Copy](https://workingcopyapp.com/) are great
iOS development tools.  Now with the iOS file provider facilities in iOS 11 one should (theoretically) be
able to work on Pythonista projects with files located directly in Working Copy.  This works as long as
the project is a single file.  Trying to split the project into separate modules results in import errors.
Moving the project files from Working Copy to Pythonista fixes the problem but limits Working Copy's
usefulness.

The problem is iOS's somewhat lame attempt at security.  iOS allows an app to open files located directly
in a file provider but appears to limit searching directories in a file provider.  Attempting an
os.listdir on a file provider's directory from Pythonista results in a permission exception.

Appending a custom Python MetaPathFinder import hook to sys.meta_path can solve the problem.  By
assuming that the files are all located in one place the Finder can try opening the file by name
and tell the import system if it succeeds.  This avoids the normal file search.

This is probably a clumsy solution and can most likely be made more useful.

To try this clone this repositoty in Working Copy and run main.py in Pythonista as an external
file.  It will fail to import the required module that's part of the same project.  Now, uncomment
the instantiation of ImportHack

```
ImportHack()
```

This should now work.


