import board
import neopixel
import requests as r
from get import data


class metarmap:
    def __init__(self):
        self.airports = ["KRBG", "KLMT", "KMFR", "KFOT", "KUKI", "KMOD", "KKIC", "KSBA", "KSAN", "KNYL", "KSDM", "MMLT", "MMSD", "MMLP", "MMSL", "MMSL", "MMLM", "MMCN", "MMGM", "MMHO", "E63", "KTUS", "KFHU", "MMCU", "KELP", "KSVC", "KALM", "KSJN", "KPHX", "KLGF", "KSEE", "KSNA", "KTRM", "KBLH", "KIGM", "KFLG", "KGUP", "KPGA", "KCDC", "KSGU", "KLAS", "KBYS", "KVGT", "KTPH", "KBFL", "KWJF", "KSBD", "KLAX", "KOXR", "KSMX", "KFAT", "KBIH", "KTVL", "KMRY", "KSFO", "KSTS", "KSAC", "KRDD", "KSVE", "KRNO", "KWMC", "KLKV", "KBNO", "KBDN", "KONP", "KEUG", "KPDX", "KAST", "KHQM", "KSEA", "KPAE", "KBVS", "S52", "KMWH", "KOMK", "KEPH", "KPSC", "KLGD", "KONO", "KBOI", "KSUN", "KMUO", "KTWF", "KPIH", "KIDA", "KDLN", "KJAC", "KLGU", "KSLC", "KENV", "KEKO", "05U", "KELY", "41U", "KGJT", "KHDN", "KVEL", "KRKS", "KRIW", "KCOD", "KBZN", "KHLN", "KMSO", "KGIC", "KLWS", "KSFF", "KSZT", "KGPI", "KCTB", "KGTF", "KHVR", "M75", "KGGW", "KSDY", "KMLS", "00U", "KBIL", "KBYG", "KGCC", "KCPR", "KCYS", "KDEN", "KCOS", "KASE", "KDRO", "KFMN ", "KABQ", "KGCK", "KIML", "KSNY", "KVTN", "KPIR", "KRAP", "KHEI", "KMOT", "KBIS", "KABR", "KMHE", "KGRI", "KGBD", "KDDC", "KWWR", "KICT", "KMHK", "KLNK", "KOMA", "KFOD", "KMDS", "KATY", "KMML", "KFAR", "KGFK", "KBJI", "KGPZ", "KBRD", "KSTC", "KMSP", "KRST", "KALO", "KDSM", "KCID", "KMSN", "KCWA", "KRHI", "CYQT", "KDLH", "KEAU", "KOSH", "KGRB", "KSAW", "KCMX", "KISQ", "KPLN",
                         "CYXZ", "KCIU", "KAPN", "KMBS", "KCAD", "KTVC", "KMKG", "KFNT", "KMTC", "KTOL", "KSBN", "KMKE", "KRFD", "KARR", "KGYY", "KFWA", "KMNN", "KCMH", "KDAY", "KMIE", "KLAF", "KCMI", "KIND", "KCVG", "KHTS", "KLEX", "KSDF", "KAJG", "KBMG", "KHUF", "KDEC", "KPIA", "KUIN", "KIJX", "KSTL", "KMDH", "KCKV", "KMKL", "KMEM", "KJBR", "KJEF", "KMCI", "KTOP", "KTUL", "KSGF", "KLIT", "KFSM", "KSWO", "KOKC", "KELK", "KBGD", "KAMA", "KLBB", "KODO", "KFST", "KSJT", "KABI", "KDTO", "KDFW", "KCNW", "KERV", "KSAT", "KLRD", "MMMV", "MMIO", "KHRL", "KCRP", "KVCT", "KHYI", "KAUS", "KSGR", "KLBX", "KBPT", "KLFT", "KAEX", "KSHV", "KPRX", "KSPS", "KADM", "KADF", "KGLH", "KJAN", "KBTR", "KMSY", "KGPT", "KMOB", "KMEI", "KCEW", "KECP", "KTLH", "KAAF", "KTPA", "KCTY", "KVLD", "KMCN", "KAND", "KTYS", "KATL", "KCSG", "KBHM", "KCBM", "KHSV", "KCHA", "KBNA", "KMTH", "KMIA", "KPBI", "KMLB", "KDAB", "KJAX", "KSAV", "KCHS", "KCAE", "KMYR", "KILM", "KFAY", "KCLT", "KGSO", "KRDU", "KNCA", "KMQI", "KNTU", "KRIC", "KLYH", "KMRB", "KBWI", "KDCA", "KCKB", "KPIT", "KYNG", "KERI", "KUNV", "KIPT", "KALB", "KSFM", "KPSM", "KBOS", "KPVC", "KGON", "KISP", "KCEF", "KABE", "KMDT", "KSBY", "KACY", "KPHL", "KLGA", "KPOU", "KSYR", "KROC", "KART", "KRUT", "KMHT", "KEWB", "KPWM", "KBTV", "KHIE", "KBML", "KBHB", "KBGR", "3B1", "KBST", "KRKD", "KMLT", "KPQI", "KEPM", "CYQI", "CYZX", "CYHZ", "CYSJ", "CYFC", "CYQM", "CZBF", "CYGP"]
        self.num_leds = 346
        self.brightness = 0.1
        self.data = data()
        self.outcome = outcome = {"success": 0,
                                  "fail": 0, "targets": len(self.airports)}
        for airport in self.airports:
            try:
                self.data[airport]
                outcome["success"] = outcome["success"] + 1
            except:
                outcome["fail"] = outcome["fail"] + 1
        outcome["hits"] = outcome["success"] + outcome["fail"]
        self.np = neopixel.NeoPixel(board.D18, len(self.airports), brightness=self.brightness,
                                    auto_write=True, pixel_order=neopixel.GRB)

    def america(self):
        print("################### RUNNING AMERICA ###################")
        colors = {
            "white": {"leds": [5, 6, 7, 10, 11, 12, 18, 19, 23, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 49, 50, 51, 53, 54, 55, 124, 125, 126, 127, 130, 131, 132, 136, 137, 139, 140, 141, 142, 146, 147, 148, 149, 155, 156, 157, 158, 161, 162, 163, 166, 167, 168, 172, 175, 176, 177, 178, 179, 180, 181, 184, 185, 197, 198, 199, 200, 208, 209, 210, 211, 212, 213, 216, 217, 218, 219, 220, 221, 222, 223, 224, 233, 234, 239, 240, 241, 242, 243, 244, 245, 246, 256, 261, 263, 264, 265, 268, 269, 274, 275, 276, 280, 281, 288, 290, 291, 293, 294, 295, 296, 306, 307, 308, 316, 321, 322, 323, 324, 325, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 338, 339, 340, 341, 342]},
            "blue": {"leds": [0, 1, 2, 3, 4, 52, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123]}
        }
        for i in range(0, self.num_leds, 1):
            if i in colors['blue']['leds']:
                self.np[i] = (0, 0, 255)
            elif i in colors['white']['leds']:
                self.np[i] = (255, 255, 255)
            else:
                self.np[i] = (255, 0, 0)
        self.colors = {
            "VFR": (0, 255, 0),
            "MVFR": (0, 0, 255),
            "IFR": (255, 0, 0),
            "LIFR": (255, 20, 147),
            "Failed": (0, 255, 255)
        }

    def metars(self):

        print("################### RUNNING METARS ###################")
        for index, airport in enumerate(self.airports):
            try:

                self.np[index] = self.colors[self.data[airport]
                                             ["flight_category"]]
            except:
                self.np[index] = self.colors["Failed"]
        print(self.np)

    def red(self):
        self.np.fill((255, 0, 0))

    def blue(self):
        self.np.fill((0, 0, 255))

    def green(self):
        self.np.fill((0, 255, 0))

    def clear(self):
        self.np.fill((0, 0, 0))

    def loading(self):
        for i in range(0, self.num_leds, 1):
            self.np[i] = (255, 0, 0)
        for i in range(self.num_leds, 0, -1):
            self.np[i] = (52, 107, 235)

    def __repr__(self):
        return str('Unsurpported')
