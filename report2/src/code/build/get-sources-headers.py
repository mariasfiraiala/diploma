#!/usr/bin/python3

import re
from pathlib import Path

p = Path('.')
origin_p = Path('/home/maria/qemu')

def find_lib(extension):
    lib_dirs = list(p.glob(f'**/*{extension}'))

    for l in lib_dirs:
        files = list(l.glob('**/*.c.o.d'))    
        headers = []

        for f in files:
            with open(str(f), "r") as read_file:
                paths = [word for line in read_file for word in line.split() if word != "\\"]
                paths = paths[1:]

                for path in paths:
                    new_p = Path(path)
                    if not new_p.is_absolute():
                        if str(new_p).startswith(".."):
                            new_p = "/home/maria/qemu" / Path(*new_p.parts[1:])
                        else:
                            new_p = "/home/maria/qemu/build" / new_p
                        headers.append(str(new_p))
                    elif origin_p in new_p.parents:
                        headers.append(str(new_p))

            headers = list(set(headers))
        
        lib = re.search(f'lib(.*){extension}', str(l.name))
        lib = lib.group(1)

        if "fa" in lib:
            pass
        
        headers_parsed = []
        for h in headers:
            if h.endswith(".c"):
                h = h.replace("/home/maria/qemu", f"LIBQEMU_{lib.upper()}_SRCS-y += $(LIBQEMU)")
            else:
                h = h.replace("/home/maria/qemu", f"LIBQEMU_{lib.upper()}_HDRS-y += $(LIBQEMU)")
            headers_parsed.append(h)

        headers_parsed.sort()

        with open(f"Makefile.uk.qemu.{lib}", "w+") as write_file:
            ok = False
            for h in headers_parsed:
                if not ok and "SRCS" in h:
                    h = "\n" + h
                    ok = True
                write_file.write(h + "\n")

            write_file.write(f"\n$(eval $(call _libqemu_import_lib,{lib},$(LIBQEMU_{lib.upper()}_HDRS-y),$(LIBQEMU_{lib.upper()}_SRCS-y)))\n")

find_lib(".fa.p")
find_lib(".a.p")
