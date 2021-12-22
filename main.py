debug = False
from gui import SilkyArcToolGUI


def test(mode: str) -> None:
    """Test the program. Pick one of the mods:
{"unpack", "pack", "decompress", "compress", "compare_dirs", "compare_files"}"""
    import filecmp
    import os
    from silky_arc import SilkyArc

    arc_file = 'Script.arc'
    true_arc_file = 'Script.arc_good'
    folder = 'Script'
    etalon = "_good"
    good_folder = folder + etalon
    comp_file = 'AP_SCENE_01.MES_i'
    dec_file = "AP_SCENE_01.MES_o"
    true_comp_file = 'AP_SCENE_01.MES_gi'
    true_dec_file = "AP_SCENE_01.MES_go"
    if mode == "unpack":
        arc_archive = SilkyArc(arc_file, folder, integrity_check=True)
        arc_archive.unpack()
    elif mode == "pack":
        arc_archive = SilkyArc(arc_file, folder, integrity_check=True)
        arc_archive.pack()
    elif mode == "decompress":
        with open(comp_file, 'rb') as iner, open(dec_file, 'wb') as outer:
            outer.write(SilkyArc.lzss_decompress(iner.read()))
        print(filecmp.cmp(dec_file, true_dec_file, shallow=False))
    elif mode == "compress":
        with open(comp_file, 'wb') as outer, open(dec_file, 'rb') as iner:
            outer.write(SilkyArc.lzss_compress(iner.read()))
        print(filecmp.cmp(comp_file, true_comp_file, shallow=False))
    elif mode == "compare_dirs":
        for root, dirs, files in os.walk(folder):
            for file in files:
                if not filecmp.cmp(os.path.join(folder, file), os.path.join(good_folder, file), shallow=False):
                    print(file)
    elif mode == "compare_files":
        print("Равны ль файлы? Ответ: {}".format(filecmp.cmp(arc_file, true_arc_file)))


def main():
    new_gui = SilkyArcToolGUI()


if __name__ == '__main__':
    if debug:
        test("compare_files")
    else:
        main()
