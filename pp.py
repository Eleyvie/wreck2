import sys
sys.version = '2.7.6 |some idiots put something here| (default, Jun 22 2015, 17:58:13) \n[GCC 4.8.2]'


try:
    import sys # Just in case
    start = sys.version.index('|') # Do we have a modified sys.version?
    end = sys.version.index('|', start + 1)
    version_bak = sys.version # Backup modified sys.version
    sys.version = sys.version.replace(sys.version[start:end+1], '') # Make it legible for platform module
    import platform
    platform.python_implementation() # Ignore result, we just need cache populated
    platform._sys_version_cache[version_bak] = platform._sys_version_cache[sys.version] # Duplicate cache
    sys.version = version_bak # Restore modified version string
except ValueError: # Catch .index() method not finding a pipe
    pass
print platform.python_implementation() # Check that everything works now
