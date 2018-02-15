
import sys
import importlib


class ImportHack:

    def __init__(self, loc=None):
        # update or append instance
        for i, mp in enumerate(sys.meta_path):
            if mp.__class__.__name__ == 'ImportHack':
                sys.meta_path[i] = self
                return

        sys.meta_path.append(self)

    @staticmethod
    def find_spec(fullname, path, target):
        import_loc = __file__.rpartition('/')[0]
        module_loc = import_loc + '/' + fullname + '.py'

        try:
            # test if target exists in same location without use of additional imports
            f = open(module_loc)
            f.close()
            return importlib.util.spec_from_file_location(fullname, module_loc)
        except Exception:
            pass


# ImportHack()


import module


print(module.MESSAGE)
