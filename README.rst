hello_briefcase
===============

hello world for briefcase

Currently this is a test case for:

https://github.com/pybee/briefcase/issues/44
and
https://github.com/pybee/briefcase/issues/46

execute in this order:

    ./briefcase.sh - runs briefcase to create the frozen app
    ./run_from_briefcase.sh - run the app from briefcase - currently shows the error (see issues for a description)
    ./compiled_package_fixup.sh - fixes up the .so files, at least as best we can
    ./run_from_briefcase.sh - rerun - should be OK


This currently fixes the python/package compile issue ('m' vs. nothing), but not the "import SSL" issue.
