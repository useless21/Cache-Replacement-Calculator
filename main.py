import flet as flt
# from win32api import GetSystemMetrics
method = 0

def myapp(page: flt.Page):
    # Initialise page criteria and components
    page.theme_mode = flt.ThemeMode.LIGHT
    # page.window_left = -10
    # page.window_top = 0
    # page.window_height = GetSystemMetrics(1) - 30
    # page.window_width = GetSystemMetrics(0) + 30
    global method, method1, data1, cl1
    methods=flt.DataTable(
        heading_text_style=flt.TextStyle(weight=flt.FontWeight.NORMAL),
        horizontal_lines=flt.BorderSide(0,"white"),
        columns=[
        flt.DataColumn(flt.Radio(value=1, label='LRU (Least Recently Used)')),
        flt.DataColumn(flt.Radio(value=2, label='FIFO (First in First )')),
        flt.DataColumn(flt.Radio(value=3, label='MRU (Most Recently Used)'))],
        rows=[
            flt.DataRow(
                cells=[
        flt.DataCell(flt.Radio(value=4, label='Optimal Replacement')),
        flt.DataCell(flt.Radio(value=5, label='Least Frequently Used')),
        flt.DataCell(flt.Radio(value=6, label='Best Method'))])])
    dv = flt.Column([methods], scroll=True)
    meth = flt.Row([dv], scroll=True, expand=1, vertical_alignment=flt.CrossAxisAlignment.START)
    method1 = flt.RadioGroup(content=meth)

    data1 = flt.TextField(
        label="Enter Element",
        value="",
        hint_text="eg. 12 14 15 18 24...",
        input_filter=flt.InputFilter(allow=True, regex_string=r"[0-9 ]", replacement_string=""),
        helper_text="Element to be entered into cache",
        tooltip="Enter integers separated by spaces"
    )
    cl1 = flt.TextField(
        label="Cache Line",
        value="",
        hint_text="eg. 8",
        input_filter=flt.NumbersOnlyInputFilter(),
        helper_text="Enter an integer to determine number of cache line",
        tooltip="Enter a single integer for cache line number"
    )

    labels = flt.TextField(
        label="",
        value="",
        border=flt.InputBorder.NONE,
    )
    printer = flt.TextField(
        label="",
        value="hello",
        border=flt.InputBorder.NONE,
    )
    alr = flt.Column(
        controls=[
            flt.Text(
                "Imagine your brain has a tiny notebook to quickly remember things. But it can only hold a few notes at a time. When you learn something new, you need to forget something old to make space.\n\nThe cache replacement calculator helps decide which old note to erase. It considers two things:\n1)The new note's size: Is it short or long? A short note might fit on an existing page, while a long one might need its own page or even erase several notes!\n2)The notebook's page size: Does each page hold one note or many? Smaller pages mean more control over what to erase, but bigger pages are easier to manage (fewer decisions).\n\nThe calculator uses different strategies to remember things you need quickly:\n\nLRU (Least Recently Used):\n\n 1) Evicts the element that hasn't been accessed for the longest time. \n 2)Good for frequently accessed data but can struggle with skewed access patterns. \n 3)Simple to implement and efficient for most workloads. \n\nFIFO (First-In-First-Out): \n\n 1)Evicts the element that arrived in the cache first, regardless of recent use. \n 2)Easy to understand and implement, but can be unfair to frequently accessed elements. \n 3)Not as adaptable as LRU to changing access patterns. \n\nMRU (Most Recently Used): \n\n 1)Evicts the element that was most recently accessed. \n 2)Not generally used in practice because it contradicts the goal of caching frequently accessed data. \n 3)Useful for special cases where recent data may be outdated. \n\nOptimal: \n\n 1)Always evicts the element that will be used furthest in the future, based on perfect knowledge of future access patterns. \n 2)Impossible to implement in real systems, but serves as a theoretical benchmark for other algorithms. \n 3)Helps evaluate the effectiveness of other algorithms. \n\nLFU (Least Frequently Used): \n\n 1)Evicts the element that has been accessed the least number of times overall. \n 2)Useful when access frequencies are uneven and some elements are rarely used. \n 3)Can perform well for certain workloads but may not be as effective as LRU for frequently accessed data.")        ])
    dlg = flt.AlertDialog(
        title=flt.Text("Welcome to our Cache Replacement Calculator"),
        content=flt.Column([alr],scroll=flt.ScrollMode.ADAPTIVE),
    )
    methods.horizontal_lines = flt.border.BorderSide(2, "#fdfcff")
    page.update()
    def theme_changed(e):
        page.theme_mode = (
            flt.ThemeMode.DARK
            if page.theme_mode == flt.ThemeMode.LIGHT
            else flt.ThemeMode.LIGHT
        )

        if(page.theme_mode == flt.ThemeMode.LIGHT):
            methods.horizontal_lines=flt.border.BorderSide(2, "#fdfcff")
        else:
            methods.horizontal_lines.color ="#201c1c"
        switch.label = (
            "Light theme" if page.theme_mode == flt.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()

    page.theme_mode = flt.ThemeMode.LIGHT
    switch = flt.Switch(label="Light theme", on_change=theme_changed)
    help = flt.Row([
        flt.Column([
            flt.Container(
                switch, alignment=flt.alignment.top_left,
            ),
        ]),
        flt.Column([
            flt.Container(
                content=flt.ElevatedButton("Help", on_click=lambda e: open_dlg()),
                padding=5, alignment=flt.alignment.center
            ),
        ]),
    ],
        alignment=flt.MainAxisAlignment.SPACE_BETWEEN
    )

    butang = flt.Row([
        flt.Container(flt.ElevatedButton("Generate",
                                         on_click=lambda e: button_clicked(e, method1, data1, cl1, page, labels,
                                                                           printer), data=0)),

        flt.Container(flt.ElevatedButton("Clear",
                                         on_click=lambda e: clear(data1, method1, cl1, labels))),
    ])

    # Update components to screen
    global scr
    scr = flt.Column()
    scr.controls.append(data1)
    scr.controls.append(cl1)
    scr.controls.append(method1)
    scr.controls.append(butang)
    scr.controls.append(labels)
    page.add(help, scr)

    # Clear selection
    def clear(data1, method1, cl1, labels):
        global ot, rounder
        if (ot != None):
            ot.visible = False
        data1.value = ""
        cl1.value = ""
        labels.value = ""
        method1.value = None
        printer.value = ""
        page.update()

    # Help
    def open_dlg():
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Method algorithm


def LRU(data, cl, page, printer, cl1, labels):
    global method
    leng = [None] * len(data)
    for i in range(len(data)):
        leng[i] = i + 1
    cache = [None] * cl
    cache1 = []
    j = 0
    k = 0
    miss = 0
    for k in range(0, len(data)):
        if data[k] not in cache:
            if (j == cl):
                cache.pop(0)
                cache.append(data[k])
                j = cl - 1
            cache[j] = data[k]
            miss = miss + 1
            j = j + 1
            cache1.append(list(cache[:]))
        elif data[k] in cache:
            if None in cache:
                cache1.append(list(cache[:]))
            else:
                x = len(cache)
                cache.remove(data[k])
                cache.insert(x - 1, data[k])
                cache1.append(list(cache[:]))
    hit = len(data) - miss
    if (method == 6):
        return [hit / len(data), miss / len(data)]
    Maketbl(page, cl, cache1, data, printer, cl1, labels, hit, miss)


def FIFO(data, cl, page, printer, cl1, labels):
    global method
    cache = [None] * cl
    cache1 = []
    j = 0
    k = 0
    miss = 0
    for k in range(0, len(data)):
        if data[k] not in cache:
            if (j == cl):
                cache.pop(0)
                cache.append(data[k])
                j = cl - 1
            cache[j] = data[k]
            miss = miss + 1
            j = j + 1
            cache1.append(list(cache[:]))
        elif data[k] in cache:
            cache1.append(list(cache[:]))
    hit = len(data) - miss
    if (method == 6):
        return [hit / len(data), miss / len(data)]
    Maketbl(page, cl, cache1, data, printer, cl1, labels, hit, miss)


def MRU(data, cl, page, printer, cl1, labels):
    global method
    cache = [None] * cl
    cache1 = []
    j = 0
    k = 0
    miss = 0
    for k in range(0, len(data)):
        if data[k] not in cache:
            if (j == cl):
                a = cache.index(data[k - 1])
                cache[a] = data[k]
                j = cl - 1
            else:
                cache[j] = data[k]
            miss = miss + 1
            j = j + 1
            cache1.append(list(cache[:]))

        elif data[k] in cache:
            cache1.append(list(cache[:]))

    hit = len(data) - miss
    if (method == 6):
        return [hit / len(data), miss / len(data)]
    Maketbl(page, cl, cache1, data, printer, cl1, labels, hit, miss)


def LFU(data, cl, page, printer, cl1, labels):
    global method
    cache = [None] * cl
    cache1 = []
    freq = [None] * cl
    j = 0
    k = 0
    miss = 0
    for k in range(0, len(data)):
        if data[k] not in cache:
            if (j == cl):
                a = freq.index(min(freq))
                cache.pop(a)
                freq.pop(a)
                cache.append(data[k])
                freq.append(1)
                j = cl - 1
            else:
                cache[j] = data[k]
                freq[j] = 1

            miss = miss + 1
            j = j + 1
            cache1.append(list(cache[:]))

        elif data[k] in cache:
            b = cache.index(data[k])
            freq[b] = freq[b] + 1
            cache1.append(list(cache[:]))

    hit = len(data) - miss
    if (method == 6):
        return [hit / len(data), miss / len(data)]
    Maketbl(page, cl, cache1, data, printer, cl1, labels, hit, miss)


def OPTIMAL(data, cl, page, printer, cl1, labels):
    global method
    cache = [None] * cl
    cache1 = []
    check = [None] * cl
    j = 0
    k = 0
    miss = 0
    for k in range(0, len(data)):
        if data[k] not in cache:
            if (j == cl):
                # temp = data[]
                for x in range(0, len(cache)):
                    data.append("Temp")
                    if cache[x] in data[k + 1:len(data) - 1]:
                        a = data.index(cache[x], k + 1, len(data) - 1)
                        check[x] = a
                    else:
                        check[x] = 0
                    data.remove("Temp")
                if (len(check) != len(set(check))):
                    cache.pop(0)
                    cache.append(data[k])
                else:
                    if 0 in check:
                        b = check.index(0)
                        cache.pop(b)
                        cache.append(data[k])
                    else:
                        b = check.index(max(check))
                        cache.pop(b)
                        cache.append(data[k])
                j = cl - 1
            cache[j] = data[k]
            miss = miss + 1
            j = j + 1
            cache1.append(list(cache[:]))

        elif data[k] in cache:
            cache1.append(list(cache[:]))

    hit = len(data) - miss
    if (method == 6):
        return [hit / len(data), miss / len(data)]
    Maketbl(page, cl, cache1, data, printer, cl1, labels, hit, miss)


def bestmeth(data, cl, page, labels, printer, cl1):
    global method
    hit_total = list()
    hit1 = LRU(data, cl, page, printer, cl1, labels)
    hit_total.extend(hit1)
    hit2 = FIFO(data, cl, page, printer, cl1, labels)
    hit_total.extend(hit2)
    hit3 = MRU(data, cl, page, printer, cl1, labels)
    hit_total.extend(hit3)
    hit4 = OPTIMAL(data, cl, page, printer, cl1, labels)
    hit_total.extend(hit4)
    hit5 = LFU(data, cl, page, printer, cl1, labels)
    hit_total.extend(hit5)
    method = hit_total.index(max(hit_total)) + 1
    labels.color = "black"
    if (method == 1):
        labels.value = 'LRU (Least Recently Used)'
        LRU(data, cl, page, printer, cl1, labels)
    elif (method == 2):
        labels.value = 'FIFO (First in First )'
        FIFO(data, cl, page, printer, cl1, labels)
    elif (method == 3):
        labels.value = 'MRU (Most Recently Used)'
        MRU(data, cl, page, printer, cl1, labels)
    elif (method == 4):
        labels.value = 'Optimal Replacement'
        OPTIMAL(data, cl, page, printer, cl1, labels)
    elif (method == 5):
        labels.value = 'Least Frequently Used'
        LFU(data, cl, page, printer, cl1, labels)

    # When generate button is clicked


def button_clicked(e, method1, data1, cl1, page, labels, printer):
    global method
    labels.value = ""
    if (data1.value == ""):
        labels.value = "Insert a valid data elements"
        labels.color = "red"
    else:
        data = list(map(int, data1.value.split()))
        labels.value = ""

        if (cl1.value == ""):
            labels.value = "Insert a valid cache line"
            labels.color = "red"
        else:
            cl = int(cl1.value)
            labels.value = ""

            if (method1.value == None):
                method = 0
                labels.value = "Select a method"
                labels.color = "red"
            else:
                method = int(method1.value)
                labels.value = ""


                if (method == 1):
                    LRU(data, cl, page, printer, cl1, labels)
                elif (method == 2):
                    FIFO(data, cl, page, printer, cl1, labels)
                elif (method == 3):
                    MRU(data, cl, page, printer, cl1, labels)
                elif (method == 4):
                    OPTIMAL(data, cl, page, printer, cl1, labels)
                elif (method == 5):
                    LFU(data, cl, page, printer, cl1, labels)
                elif (method == 6):
                    bestmeth(data, cl, page, labels, printer, cl1)
    page.update()

ot = None
rounder = 0

# Cache replacement table generation
def Maketbl(page, cl, cache1, data, printer, cl1, labels, hit, miss):
    global rounder, ot, dt
    printer.value = "Hit ratio = " + str(round(hit / len(data), 2)) + "\t\t\t" + "Miss ratio = " + str(
        round(miss / len(data), 2))
    lstrow = list()
    baris = list()
    col = [flt.DataColumn(flt.Text(str(i + 1)), tooltip="Data in cache at cycle " + str(i + 1)) for i in
           range(len(data))]

    for i in range(int(cl)):
        for j in range(len(data)):
            lstrow.append(flt.DataCell(flt.Text(str(cache1[j][i]))))
        baris.append(flt.DataRow(lstrow))
        lstrow = []
    dt = flt.DataTable(heading_text_style=flt.TextStyle(weight=flt.FontWeight.BOLD),heading_row_color=flt.colors.AMBER_50,columns=col, rows=baris)
    cv = flt.Column([dt], scroll=True)
    rv = flt.Row([cv],scroll=flt.ScrollMode.ADAPTIVE, expand=1, vertical_alignment=flt.CrossAxisAlignment.START)
    page.add(rv)
    if (rounder > 0):
        page.remove(ot)
        page.remove(printer)
        ot = rv
    else:
        ot = rv
    rounder = rounder + 1
    page.add(printer)
    page.update()

flt.app(target=myapp)
