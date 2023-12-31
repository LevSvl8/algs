
def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low <=high:
        mid = (low+high)/2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
if __name__ == '__main__':

    l = [
    "mqusw",
    "fkwhx",
    "xsuwu",
    "rbyod",
    "rdbxs",
    "dgxch",
    "yoisq",
    "fcaiz",
    "tjapc",
    "fvpnc",
    "ibwrw",
    "mquqr",
    "sjjye",
    "isycy",
    "ndamp",
    "ymjnc",
    "tvozz",
    "envym",
    "exstk",
    "qpaqq",
    "lmwvl",
    "hxiat",
    "ohjua",
    "abiry",
    "pbvku",
    "hidgg",
    "tymef",
    "dcbkb",
    "oddin",
    "ockth",
    "xxvgp",
    "fmxze",
    "wruwh",
    "jwobz",
    "fdnjy",
    "yhksf",
    "srgbx",
    "hoqff",
    "zyfsv",
    "tpgqc",
    "nakbf",
    "npvwh",
    "caffr",
    "tnrxw",
    "fkuhu",
    "apgxw",
    "bssvm",
    "gqezd",
    "wkkch",
    "jrsbq",
    "qqtgm",
    "dzpkv",
    "uofje",
    "cteki",
    "npxrc",
    "spnvb",
    "lqrwp",
    "unkcm",
    "yflie",
    "rwfaz",
    "osaik",
    "tdvtw",
    "akuda",
    "hxjbd",
    "ejepg",
    "pexnd",
    "gxlds",
    "fcwti",
    "zyjhk",
    "oveqj",
    "kechh",
    "rupid",
    "zsgvv",
    "qfkva",
    "gwpwc",
    "szhpb",
    "rxvge",
    "qhimr",
    "snqij",
    "vfmxh",
    "llbwy",
    "lkhby",
    "ktqis",
    "zoibs",
    "yilyn",
    "ovfxl",
    "ziiyb",
    "dolaw",
    "usicf",
    "hiwiu",
    "svwcd",
    "rzgin",
    "nicaz",
    "ecsyh",
    "wqxyj",
    "ruhxv",
    "acwmz",
    "byxqv",
    "vcgvx",
    "tdtuk",
    "drbwa",
    "bciop",
    "hqdyx",
    "csvfm",
    "tlvwf",
    "gcvng",
    "drdiq",
    "vkteg",
    "ontlt",
    "bbmwa",
    "imuwn",
    "kovly",
    "wuuaj",
    "elmqq",
    "dtzkw",
    "zkbyw",
    "dyfgy",
    "yplhn",
    "qghcr",
    "fubty",
    "ghxln",
    "csqhv",
    "bblmi",
    "viooh",
    "qqbjg",
    "xhnrc",
    "dvyee",
    "qfpia"
    ]
    sorted_list = (sorted(l,key=str))
    print sorted_list
    print sorted_list[98] # tnrxw
    print binary_search(sorted_list,'viooh') # O(log n) -> n = 128 -> log 128 = 7 -> 7
