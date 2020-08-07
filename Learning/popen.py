from subprocess import PIPE, Popen


def _getUbootVer():
    # Get U-boot Version
    uboot_version = None
    # uboot_ver_regex = r"^U-Boot\W+(?P<uboot_ver>20\d{2}\.\d{2})\W+.*$"
    # uboot_ver_re = re.compile(uboot_ver_regex)
    # mtd0_str_dump_cmd = ["/usr/bin/strings", "/dev/mtd0"]
    mtd0_str_dump_cmd1 = ["dd", "if=./data-full", "skip=128"]
    mtd0_str_dump_cmd2 = ["strings"]
    data = Popen(mtd0_str_dump_cmd1, stdout=PIPE, universal_newlines=True).stdout
    with Popen(mtd0_str_dump_cmd2, stdin=data, stdout=PIPE, universal_newlines=True) as proc:
        print(proc.stdout.read())

_getUbootVer()