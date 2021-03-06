import os
from get import ip
from pathlib import Path
ip = ip()
backup = ["KRBG", "KLMT", "KMFR", "KFOT", "KUKI", "KMOD", "KKIC", "KSBA", "KSAN", "KNYL", "KSDM", "MMLT", "MMSD", "MMLP", "MMSL", "MMSL", "MMLM", "MMCN", "MMGM", "MMHO", "E63", "KTUS", "KFHU", "MMCU", "KELP", "KSVC", "KALM", "KSJN", "KPHX", "KLGF", "KSEE", "KSNA", "KTRM", "KBLH", "KIGM", "KFLG", "KGUP", "KPGA", "KCDC", "KSGU", "KLAS", "KBYS", "KVGT", "KTPH", "KBFL", "KWJF", "KSBD", "KLAX", "KOXR", "KSMX", "KFAT", "KBIH", "KTVL", "KMRY", "KSFO", "KSTS", "KSAC", "KRDD", "KSVE", "KRNO", "KWMC", "KLKV", "KBNO", "KBDN", "KONP", "KEUG", "KPDX", "KAST", "KHQM", "KSEA", "KPAE", "KBVS", "S52", "KMWH", "KOMK", "KEPH", "KPSC", "KLGD", "KONO", "KBOI", "KSUN", "KMUO", "KTWF", "KPIH", "KIDA", "KDLN", "KJAC", "KLGU", "KSLC", "KENV", "KEKO", "05U", "KELY", "41U", "KGJT", "KHDN", "KVEL", "KRKS", "KRIW", "KCOD", "KBZN", "KHLN", "KMSO", "KGIC", "KLWS", "KSFF", "KSZT", "KGPI", "KCTB", "KGTF", "KHVR", "M75", "KGGW", "KSDY", "KMLS", "00U", "KBIL", "KBYG", "KGCC", "KCPR", "KCYS", "KDEN", "KCOS", "KASE", "KDRO", "KFMN ", "KABQ", "KGCK", "KIML", "KSNY", "KVTN", "KPIR", "KRAP", "KHEI", "KMOT", "KBIS", "KABR", "KMHE", "KGRI", "KGBD", "KDDC", "KWWR", "KICT", "KMHK", "KLNK", "KOMA", "KFOD", "KMDS", "KATY", "KMML", "KFAR", "KGFK", "KBJI", "KGPZ", "KBRD", "KSTC", "KMSP", "KRST", "KALO", "KDSM", "KCID", "KMSN", "KCWA", "KRHI", "CYQT", "KDLH", "KEAU", "KOSH", "KGRB", "KSAW", "KCMX", "KISQ", "KPLN",
          "CYXZ", "KCIU", "KAPN", "KMBS", "KCAD", "KTVC", "KMKG", "KFNT", "KMTC", "KTOL", "KSBN", "KMKE", "KRFD", "KARR", "KGYY", "KFWA", "KMNN", "KCMH", "KDAY", "KMIE", "KLAF", "KCMI", "KIND", "KCVG", "KHTS", "KLEX", "KSDF", "KAJG", "KBMG", "KHUF", "KDEC", "KPIA", "KUIN", "KIJX", "KSTL", "KMDH", "KCKV", "KMKL", "KMEM", "KJBR", "KJEF", "KMCI", "KTOP", "KTUL", "KSGF", "KLIT", "KFSM", "KSWO", "KOKC", "KELK", "KBGD", "KAMA", "KLBB", "KODO", "KFST", "KSJT", "KABI", "KDTO", "KDFW", "KCNW", "KERV", "KSAT", "KLRD", "MMMV", "MMIO", "KHRL", "KCRP", "KVCT", "KHYI", "KAUS", "KSGR", "KLBX", "KBPT", "KLFT", "KAEX", "KSHV", "KPRX", "KSPS", "KADM", "KADF", "KGLH", "KJAN", "KBTR", "KMSY", "KGPT", "KMOB", "KMEI", "KCEW", "KECP", "KTLH", "KAAF", "KTPA", "KCTY", "KVLD", "KMCN", "KAND", "KTYS", "KATL", "KCSG", "KBHM", "KCBM", "KHSV", "KCHA", "KBNA", "KMTH", "KMIA", "KPBI", "KMLB", "KDAB", "KJAX", "KSAV", "KCHS", "KCAE", "KMYR", "KILM", "KFAY", "KCLT", "KGSO", "KRDU", "KNCA", "KMQI", "KNTU", "KRIC", "KLYH", "KMRB", "KBWI", "KDCA", "KCKB", "KPIT", "KYNG", "KERI", "KUNV", "KIPT", "KALB", "KSFM", "KPSM", "KBOS", "KPVC", "KGON", "KISP", "KCEF", "KABE", "KMDT", "KSBY", "KACY", "KPHL", "KLGA", "KPOU", "KSYR", "KROC", "KART", "KRUT", "KMHT", "KEWB", "KPWM", "KBTV", "KHIE", "KBML", "KBHB", "KBGR", "3B1", "KBST", "KRKD", "KMLT", "KPQI", "KEPM", "CYQI", "CYZX", "CYHZ", "CYSJ", "CYFC", "CYQM", "CZBF", "CYGP"]


airports = []


def setter(airports_list):
    airports = list(airports_list.values())
    str = ''
    for i in airports:
        str += i + ', '
    f = open("airports.csv", "w")
    f.write(str)
    f.close()
    print("DONE")


def getter():

    if Path('./airports.csv').exists():
        f = open("airports.csv", "r")
        airports_csv = f.read()
        airports_list = airports_csv.split(", ")
        airport_return = airports_list[:-1]
        print('Running Custom File')
        return airport_return
    else:
        print('Running Defaults')
        return backup


getter()
