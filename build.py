import shutil, os, sys
usage = """
        All names should be passed without extensions.
        All input names will have *.py extension added.
        Entry point output name will have *.pyw extension added.
        Usage:
            > python build.py name_in name_out
                builds name_in as an main entry point and gives it name_out name
            > python build.py name_in
                builds name_in as an main entry point and gives it "main" name
            > python build.py
                builds "main" as an main entry point and gives it "main" name"""


if __name__ == "__main__":
    arglist = sys.argv[1:]

    if len(arglist) == 2:
        EP_in_name = arglist[0] + ".py"
        EP_out_name = arglist[1] + ".pyw"
    elif len(arglist) == 1:
        EP_in_name = arglist[0] + ".py"
        EP_out_name = "main.pyw"
    elif len(arglist) == 0:
        EP_in_name = "main.py"
        EP_out_name = "main.pyw"
    else:
        raise NameError(usage)

    if (len(EP_in_name.split('.')) != 2) or (len(EP_out_name.split('.')) != 2):
        raise NameError(usage)

    catalogue = os.listdir(os.path.join(".","src"))
    if not (EP_in_name in catalogue):
        raise NameError("No file called %s found inside .\src" % EP_in_name)

    try:
        shutil.rmtree(os.path.join(".", "release"))
    except:
        pass

    if not os.path.exists(os.path.join(".","release")):
        os.mkdir("release")

    for element in catalogue:
        # catch and mill every python source file *.py
        if element.endswith(".py"):
            if element == EP_in_name:
                src = os.path.join(".","src",element)
                dst = os.path.join(".","release",EP_out_name)
                shutil.copy(src, dst)
            else:
                src = os.path.join(".","src",element)
                dst = os.path.join(".","release",element)
                shutil.copy(src, dst)

        # catch and mill icon file
        if element.startswith("Icon."):
            src = os.path.join(".","src",element)
            dst = os.path.join(".","release",element)
            shutil.copy(src, dst)
