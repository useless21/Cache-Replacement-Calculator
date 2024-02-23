import flet as flt
clr=0
method = 0

def myapp(page: flt.Page):
    page.theme_mode = flt.ThemeMode.LIGHT
    page.scroll="always"
    page.window_fullscreen=True
    global method,method1,data1,cl1
    method1 = flt.RadioGroup(content=flt.Column([
        flt.Radio(value=1, label='LRU (Least Recently Used)'),
        flt.Radio(value=2, label='FIFO (First in First )'),
        flt.Radio(value=3, label='MRU (Most Recently Used)'),
        flt.Radio(value=4, label='Optimal Replacement'),
        flt.Radio(value=5, label='Least Frequently Used'),
        flt.Radio(value=6, label='Best Method')]))

    data1 = flt.TextField(
        label="Enter Element",
        value="",
        hint_text="12 14 15 18 24...",
        input_filter=flt.InputFilter(allow=True, regex_string=r"[0-9 ]", replacement_string=""),
        helper_text="Element to be entered into cache",
    )
    cl1 = flt.TextField(
        label="Cache Line",
        value="",
        input_filter=flt.NumbersOnlyInputFilter(),
        helper_text = "Enter an integer to determine number of cache line",
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
    err = flt.TextField(
        label="",
        value="",
        border=flt.InputBorder.NONE,
        color="red"
    )
    dlg = flt.AlertDialog(
        title=flt.Text("Welcome to our Cache Replacement Calculator"),
        content=flt.Text("Imagine your brain has a tiny notebook to quickly remember things. But it can only hold a few notes at a time. When you learn something new, you need to forget something old to make space.\n\nThe cache replacement calculator helps decide which old note to erase. It considers two things:\n\t\t\t\t\t\t\t1)The new note's size: Is it short or long? A short note might fit on an existing page, while a long one might need its own page or even erase several notes!\n\t\t\t\t\t\t\t2)The notebook's page size: Does each page hold one note or many? Smaller pages mean more control over what to erase, but bigger pages are easier to manage (fewer decisions).\n\nThe calculator uses different strategies to remember things you need quickly:\nLRU (Least Recently Used):\n\t\t\t\t\t\t\t1) Evicts the element that hasn't been accessed for the longest time. \n\t\t\t\t\t\t 2)Good for frequently accessed data but can struggle with skewed access patterns. \n\t\t\t\t\t\t 3)Simple to implement and efficient for most workloads. \n\nFIFO (First-In-First-Out): \n\t\t\t\t\t\t 1)Evicts the element that arrived in the cache first, regardless of recent use. \n\t\t\t\t\t\t 2)Easy to understand and implement, but can be unfair to frequently accessed elements. \n\t\t\t\t\t\t 3)Not as adaptable as LRU to changing access patterns. \n\nMRU (Most Recently Used): \n\t\t\t\t\t\t 1)Evicts the element that was most recently accessed. \n\t\t\t\t\t\t 2)Not generally used in practice because it contradicts the goal of caching frequently accessed data. \n\t\t\t\t\t\t 3)Useful for special cases where recent data may be outdated. \n\nOptimal: \n\t\t\t\t\t\t 1)Always evicts the element that will be used furthest in the future, based on perfect knowledge of future access patterns. \n\t\t\t\t\t\t 2)Impossible to implement in real systems, but serves as a theoretical benchmark for other algorithms. \n\t\t\t\t\t\t 3)Helps evaluate the effectiveness of other algorithms. \n\nLFU (Least Frequently Used): \n\t\t\t\t\t\t 1)Evicts the element that has been accessed the least number of times overall. \n\t\t\t\t\t\t 2)Useful when access frequencies are uneven and some elements are rarely used. \n\t\t\t\t\t\t 3)Can perform well for certain workloads but may not be as effective as LRU for frequently accessed data."),

    )
    def theme_changed(e):
        page.theme_mode = (
            flt.ThemeMode.DARK
            if page.theme_mode == flt.ThemeMode.LIGHT
            else flt.ThemeMode.LIGHT
        )
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
                padding=5, alignment=flt.alignment.center,
            ),
        ]),
    ],
        alignment=flt.MainAxisAlignment.SPACE_BETWEEN
    )
    closer = flt.Row([
        flt.Column([
            flt.Row([
                flt.Container(
                    content=flt.ElevatedButton("-", on_click=lambda e: minim(), bgcolor="green", color="black"),
                    padding=5, alignment=flt.alignment.top_right, ),
                flt.Container(
                    content=flt.ElevatedButton("■", on_click=lambda e: kecil(), bgcolor="yellow", color="black"),
                    padding=5, alignment=flt.alignment.top_right, ),
                flt.Container(
                    content=flt.ElevatedButton("X", on_click=lambda e: keluar(), bgcolor="red", color="black"),
                    padding=5, alignment=flt.alignment.top_right, ),

            ])


        ])

    ],
        alignment=flt.MainAxisAlignment.END
    )

    butang = flt.Row(
        [
            flt.Container(flt.ElevatedButton("Generate",
                                             on_click=lambda e: button_clicked(e, method1, data1, cl1, page,
                                                                               labels, printer,err), data=0)
                          ),

            flt.Container(flt.ElevatedButton("Clear",
                                             on_click=lambda e: clear(data1,method1,cl1,labels))
                          ),

        ]
    )

    global scr
    scr= flt.Column(scroll="always")
    scr.controls.append(data1)
    scr.controls.append(cl1)
    scr.controls.append(method1)
    scr.controls.append(err)
    scr.controls.append(butang)
    scr.controls.append(labels)
    page.add(help,scr)




    def clear(data1,method1,cl1,labels):
        global clr
        global ot
        global rounder
        # flt.app(target=myapp)
        # page.window_close()
        if (ot!=None):
            ot.visible = False
        data1.value=""
        cl1.value=""
        labels.value = ""
        method1.value=None
        clr=1
        err.value=""
        printer.value=""
        page.update()
    def kecil():
        print(page.window_height)
        page.window_height=400
        print(page.window_height)
        page.window_width=500
        page.update()
    def minim():
        page.window.hide()
        print(page.window_minimized)
        page.update()
    def keluar():
        page.window_close()
    def open_dlg():
        page.dialog = dlg
        dlg.open = True
        page.update()


def LRU(data, cl, page, printer,cl1,labels):
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
    printer.value = "Hit ratio = " + str(hit / len(data)) + "\t\t\t" + "Miss ratio = " + str(miss / len(data))

    Maketbl(page, cl, cache1, data, printer,cl1,labels)


def FIFO(data, cl, page, printer,cl1,labels):
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
    printer.value = "Hit ratio = " + str(hit / len(data)) + "\t\t\t" + "Miss ratio = " + str(miss / len(data))

    Maketbl(page, cl, cache1, data, printer,cl1,labels)


def MRU(data, cl, page, printer,cl1,labels):
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
    printer.value = "Hit ratio = " + str(hit / len(data)) + "\t\t\t" + "Miss ratio = " + str(miss / len(data))
    Maketbl(page, cl, cache1, data, printer,cl1,labels)


def LFU(data, cl, page, printer,cl1,labels):
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
    printer.value = "Hit ratio = " + str(hit / len(data)) + "\t\t\t" + "Miss ratio = " + str(miss / len(data))

    Maketbl(page, cl, cache1, data, printer,cl1,labels)


def OPTIMAL(data, cl, page, printer,cl1,labels):
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
    printer.value = "Hit ratio = " + str(hit / len(data)) + "\t\t\t" + "Miss ratio = " + str(miss / len(data))

    Maketbl(page, cl, cache1, data, printer,cl1,labels)


def bestmeth(data, cl, page, labels, printer,cl1):
    global method
    hit_total = [[None for j in range(2)] for i in range(5)]
    hit1 = LRU(data, cl, page, printer,cl1,labels)
    hit_total[0][0] = hit1[0]
    hit_total[0][1] = hit1[1]
    hit2 = FIFO(data, cl, page, printer,cl1,labels)
    hit_total[1][0] = hit2[0]
    hit_total[1][1] = hit2[1]
    hit3 = MRU(data, cl, page, printer,cl1,labels)
    hit_total[2][0] = hit3[0]
    hit_total[2][1] = hit3[1]
    hit4 = OPTIMAL(data, cl, page, printer,cl1,labels)
    hit_total[3][0] = hit4[0]
    hit_total[3][1] = hit4[1]
    hit5 = LFU(data, cl, page, printer,cl1,labels)
    hit_total[4][0] = hit5[0]
    hit_total[4][1] = hit5[1]
    num = hit_total.index(max(hit_total))
    method = num + 1
    if (method == 1):
        labels.value = 'LRU (Least Recently Used)'
        LRU(data, cl, page, printer,cl1,labels)
    elif (method == 2):
        labels.value = 'FIFO (First in First )'
        FIFO(data, cl, page, printer,cl1,labels)
    elif (method == 3):
        labels.value = 'MRU (Most Recently Used)'
        MRU(data, cl, page, printer,cl1,labels)
    elif (method == 4):
        labels.value = 'Optimal Replacement'
        OPTIMAL(data, cl, page, printer,cl1,labels)
    elif (method == 5):
        labels.value = 'Least Frequently Used'
        LFU(data, cl, page, printer,cl1,labels)



def button_clicked(e, method1, data1, cl1, page, labels, printer,err):
    global method
    global clr
    clr=0
    labels.value = ""
    if (method1.value==None):
        method=0
        err.value = "Select a method"
    else:
        method = int(method1.value)
        err.value = ""
        if (cl1.value==""):
            err.value = "Insert a valid cache line"
        else:
            cl = int(cl1.value)
            err.value = ""
            if (data1.value == ""):
                err.value = "Insert a valid data elements"
            else:
                data = list(map(int, data1.value.split()))
                err.value = ""

                if (method == 1):
                    LRU(data, cl, page, printer,cl1,labels)
                elif (method == 2):
                    FIFO(data, cl, page, printer,cl1,labels)
                elif (method == 3):
                    MRU(data, cl, page, printer,cl1,labels)
                elif (method == 4):
                    OPTIMAL(data, cl, page, printer,cl1,labels)
                elif (method == 5):
                    LFU(data, cl, page, printer,cl1,labels)
                elif (method == 6):
                    bestmeth(data, cl, page, labels, printer,cl1)

    page.update()


ot = None
rounder = 0


def Maketbl(page, cl, cache1, data, printer,cl1,labels):
    global rounder, ot
    checker = [0] * 100
    checker1 = [0] * 10
    x = [flt.DataColumn(flt.Text("-1"))] * 100
    for i in range(len(data)):
        x[i] = flt.DataColumn(flt.Text(str(i + 1)))
        checker[i] = 1
    for i in range(cl):
        checker1[i] = 1
    buf = [[-1 for j in range(10)] for i in range(100)]
    buf[10][1] = -5
    for j in range(100):
        for i in range(9):
            if (j < len(data) and i < cl):
                buf[j][i] = cache1[j][i]
    global dt
    dt = flt.DataTable(
        columns=[x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15],
                 x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[23], x[24], x[25], x[26], x[27], x[28], x[29],
                 x[30], x[31], x[32], x[33], x[34], x[35], x[36], x[37], x[38], x[39], x[40], x[41], x[42], x[43],
                 x[44], x[45], x[46], x[47], x[48], x[49], x[50], x[51], x[52], x[53], x[54], x[55], x[56], x[57],
                 x[58], x[59], x[60], x[61], x[62], x[63], x[64], x[65], x[66], x[67], x[68], x[69], x[70], x[71],
                 x[72], x[73], x[74], x[75], x[76], x[77], x[78], x[79], x[80], x[81], x[82], x[83], x[84], x[85],
                 x[86], x[87], x[88], x[89], x[90], x[91], x[92], x[93], x[94], x[95], x[96], x[97], x[98], x[99]]
        ,
        rows=[
            flt.DataRow(
                cells=[
                    flt.DataCell(flt.Text(str(buf[0][0]))), flt.DataCell(flt.Text(str(buf[1][0]))),
                    flt.DataCell(flt.Text(str(buf[2][0]))), flt.DataCell(flt.Text(str(buf[3][0]))),
                    flt.DataCell(flt.Text(str(buf[4][0]))), flt.DataCell(flt.Text(str(buf[5][0]))),
                    flt.DataCell(flt.Text(str(buf[6][0]))), flt.DataCell(flt.Text(str(buf[7][0]))),
                    flt.DataCell(flt.Text(str(buf[8][0]))), flt.DataCell(flt.Text(str(buf[9][0]))),
                    flt.DataCell(flt.Text(str(buf[10][0]))), flt.DataCell(flt.Text(str(buf[11][0]))),
                    flt.DataCell(flt.Text(str(buf[12][0]))), flt.DataCell(flt.Text(str(buf[13][0]))),
                    flt.DataCell(flt.Text(str(buf[14][0]))), flt.DataCell(flt.Text(str(buf[15][0]))),
                    flt.DataCell(flt.Text(str(buf[16][0]))), flt.DataCell(flt.Text(str(buf[17][0]))),
                    flt.DataCell(flt.Text(str(buf[18][0]))), flt.DataCell(flt.Text(str(buf[19][0]))),
                    flt.DataCell(flt.Text(str(buf[20][0]))), flt.DataCell(flt.Text(str(buf[21][0]))),
                    flt.DataCell(flt.Text(str(buf[22][0]))), flt.DataCell(flt.Text(str(buf[23][0]))),
                    flt.DataCell(flt.Text(str(buf[24][0]))), flt.DataCell(flt.Text(str(buf[25][0]))),
                    flt.DataCell(flt.Text(str(buf[26][0]))), flt.DataCell(flt.Text(str(buf[27][0]))),
                    flt.DataCell(flt.Text(str(buf[28][0]))), flt.DataCell(flt.Text(str(buf[29][0]))),
                    flt.DataCell(flt.Text(str(buf[30][0]))), flt.DataCell(flt.Text(str(buf[31][0]))),
                    flt.DataCell(flt.Text(str(buf[32][0]))), flt.DataCell(flt.Text(str(buf[33][0]))),
                    flt.DataCell(flt.Text(str(buf[34][0]))), flt.DataCell(flt.Text(str(buf[35][0]))),
                    flt.DataCell(flt.Text(str(buf[36][0]))), flt.DataCell(flt.Text(str(buf[37][0]))),
                    flt.DataCell(flt.Text(str(buf[38][0]))), flt.DataCell(flt.Text(str(buf[39][0]))),
                    flt.DataCell(flt.Text(str(buf[40][0]))), flt.DataCell(flt.Text(str(buf[41][0]))),
                    flt.DataCell(flt.Text(str(buf[42][0]))), flt.DataCell(flt.Text(str(buf[43][0]))),
                    flt.DataCell(flt.Text(str(buf[44][0]))), flt.DataCell(flt.Text(str(buf[45][0]))),
                    flt.DataCell(flt.Text(str(buf[46][0]))), flt.DataCell(flt.Text(str(buf[47][0]))),
                    flt.DataCell(flt.Text(str(buf[48][0]))), flt.DataCell(flt.Text(str(buf[49][0]))),
                    flt.DataCell(flt.Text(str(buf[50][0]))), flt.DataCell(flt.Text(str(buf[51][0]))),
                    flt.DataCell(flt.Text(str(buf[52][0]))), flt.DataCell(flt.Text(str(buf[53][0]))),
                    flt.DataCell(flt.Text(str(buf[54][0]))), flt.DataCell(flt.Text(str(buf[55][0]))),
                    flt.DataCell(flt.Text(str(buf[56][0]))), flt.DataCell(flt.Text(str(buf[57][0]))),
                    flt.DataCell(flt.Text(str(buf[58][0]))), flt.DataCell(flt.Text(str(buf[59][0]))),
                    flt.DataCell(flt.Text(str(buf[60][0]))), flt.DataCell(flt.Text(str(buf[61][0]))),
                    flt.DataCell(flt.Text(str(buf[62][0]))), flt.DataCell(flt.Text(str(buf[63][0]))),
                    flt.DataCell(flt.Text(str(buf[64][0]))), flt.DataCell(flt.Text(str(buf[65][0]))),
                    flt.DataCell(flt.Text(str(buf[66][0]))), flt.DataCell(flt.Text(str(buf[67][0]))),
                    flt.DataCell(flt.Text(str(buf[68][0]))), flt.DataCell(flt.Text(str(buf[69][0]))),
                    flt.DataCell(flt.Text(str(buf[70][0]))), flt.DataCell(flt.Text(str(buf[71][0]))),
                    flt.DataCell(flt.Text(str(buf[72][0]))), flt.DataCell(flt.Text(str(buf[73][0]))),
                    flt.DataCell(flt.Text(str(buf[74][0]))), flt.DataCell(flt.Text(str(buf[75][0]))),
                    flt.DataCell(flt.Text(str(buf[76][0]))), flt.DataCell(flt.Text(str(buf[77][0]))),
                    flt.DataCell(flt.Text(str(buf[78][0]))), flt.DataCell(flt.Text(str(buf[79][0]))),
                    flt.DataCell(flt.Text(str(buf[80][0]))), flt.DataCell(flt.Text(str(buf[81][0]))),
                    flt.DataCell(flt.Text(str(buf[82][0]))), flt.DataCell(flt.Text(str(buf[83][0]))),
                    flt.DataCell(flt.Text(str(buf[84][0]))), flt.DataCell(flt.Text(str(buf[85][0]))),
                    flt.DataCell(flt.Text(str(buf[86][0]))), flt.DataCell(flt.Text(str(buf[87][0]))),
                    flt.DataCell(flt.Text(str(buf[88][0]))), flt.DataCell(flt.Text(str(buf[89][0]))),
                    flt.DataCell(flt.Text(str(buf[90][0]))), flt.DataCell(flt.Text(str(buf[91][0]))),
                    flt.DataCell(flt.Text(str(buf[92][0]))), flt.DataCell(flt.Text(str(buf[93][0]))),
                    flt.DataCell(flt.Text(str(buf[94][0]))), flt.DataCell(flt.Text(str(buf[95][0]))),
                    flt.DataCell(flt.Text(str(buf[96][0]))), flt.DataCell(flt.Text(str(buf[97][0]))),
                    flt.DataCell(flt.Text(str(buf[98][0]))), flt.DataCell(flt.Text(str(buf[99][0]))),

                ],
            ),
            flt.DataRow(
                cells=[
                    flt.DataCell(flt.Text(str(buf[0][1]))), flt.DataCell(flt.Text(str(buf[1][1]))),
                    flt.DataCell(flt.Text(str(buf[2][1]))), flt.DataCell(flt.Text(str(buf[3][1]))),
                    flt.DataCell(flt.Text(str(buf[4][1]))), flt.DataCell(flt.Text(str(buf[5][1]))),
                    flt.DataCell(flt.Text(str(buf[6][1]))), flt.DataCell(flt.Text(str(buf[7][1]))),
                    flt.DataCell(flt.Text(str(buf[8][1]))), flt.DataCell(flt.Text(str(buf[9][1]))),
                    flt.DataCell(flt.Text(str(buf[10][1]))), flt.DataCell(flt.Text(str(buf[11][1]))),
                    flt.DataCell(flt.Text(str(buf[12][1]))), flt.DataCell(flt.Text(str(buf[13][1]))),
                    flt.DataCell(flt.Text(str(buf[14][1]))), flt.DataCell(flt.Text(str(buf[15][1]))),
                    flt.DataCell(flt.Text(str(buf[16][1]))), flt.DataCell(flt.Text(str(buf[17][1]))),
                    flt.DataCell(flt.Text(str(buf[18][1]))), flt.DataCell(flt.Text(str(buf[19][1]))),
                    flt.DataCell(flt.Text(str(buf[20][1]))), flt.DataCell(flt.Text(str(buf[21][1]))),
                    flt.DataCell(flt.Text(str(buf[22][1]))), flt.DataCell(flt.Text(str(buf[23][1]))),
                    flt.DataCell(flt.Text(str(buf[24][1]))), flt.DataCell(flt.Text(str(buf[25][1]))),
                    flt.DataCell(flt.Text(str(buf[26][1]))), flt.DataCell(flt.Text(str(buf[27][1]))),
                    flt.DataCell(flt.Text(str(buf[28][1]))), flt.DataCell(flt.Text(str(buf[29][1]))),
                    flt.DataCell(flt.Text(str(buf[30][1]))), flt.DataCell(flt.Text(str(buf[31][1]))),
                    flt.DataCell(flt.Text(str(buf[32][1]))), flt.DataCell(flt.Text(str(buf[33][1]))),
                    flt.DataCell(flt.Text(str(buf[34][1]))), flt.DataCell(flt.Text(str(buf[35][1]))),
                    flt.DataCell(flt.Text(str(buf[36][1]))), flt.DataCell(flt.Text(str(buf[37][1]))),
                    flt.DataCell(flt.Text(str(buf[38][1]))), flt.DataCell(flt.Text(str(buf[39][1]))),
                    flt.DataCell(flt.Text(str(buf[40][1]))), flt.DataCell(flt.Text(str(buf[41][1]))),
                    flt.DataCell(flt.Text(str(buf[42][1]))), flt.DataCell(flt.Text(str(buf[43][1]))),
                    flt.DataCell(flt.Text(str(buf[44][1]))), flt.DataCell(flt.Text(str(buf[45][1]))),
                    flt.DataCell(flt.Text(str(buf[46][1]))), flt.DataCell(flt.Text(str(buf[47][1]))),
                    flt.DataCell(flt.Text(str(buf[48][1]))), flt.DataCell(flt.Text(str(buf[49][1]))),
                    flt.DataCell(flt.Text(str(buf[50][1]))), flt.DataCell(flt.Text(str(buf[51][1]))),
                    flt.DataCell(flt.Text(str(buf[52][1]))), flt.DataCell(flt.Text(str(buf[53][1]))),
                    flt.DataCell(flt.Text(str(buf[54][1]))), flt.DataCell(flt.Text(str(buf[55][1]))),
                    flt.DataCell(flt.Text(str(buf[56][1]))), flt.DataCell(flt.Text(str(buf[57][1]))),
                    flt.DataCell(flt.Text(str(buf[58][1]))), flt.DataCell(flt.Text(str(buf[59][1]))),
                    flt.DataCell(flt.Text(str(buf[60][1]))), flt.DataCell(flt.Text(str(buf[61][1]))),
                    flt.DataCell(flt.Text(str(buf[62][1]))), flt.DataCell(flt.Text(str(buf[63][1]))),
                    flt.DataCell(flt.Text(str(buf[64][1]))), flt.DataCell(flt.Text(str(buf[65][1]))),
                    flt.DataCell(flt.Text(str(buf[66][1]))), flt.DataCell(flt.Text(str(buf[67][1]))),
                    flt.DataCell(flt.Text(str(buf[68][1]))), flt.DataCell(flt.Text(str(buf[69][1]))),
                    flt.DataCell(flt.Text(str(buf[70][1]))), flt.DataCell(flt.Text(str(buf[71][1]))),
                    flt.DataCell(flt.Text(str(buf[72][1]))), flt.DataCell(flt.Text(str(buf[73][1]))),
                    flt.DataCell(flt.Text(str(buf[74][1]))), flt.DataCell(flt.Text(str(buf[75][1]))),
                    flt.DataCell(flt.Text(str(buf[76][1]))), flt.DataCell(flt.Text(str(buf[77][1]))),
                    flt.DataCell(flt.Text(str(buf[78][1]))), flt.DataCell(flt.Text(str(buf[79][1]))),
                    flt.DataCell(flt.Text(str(buf[80][1]))), flt.DataCell(flt.Text(str(buf[81][1]))),
                    flt.DataCell(flt.Text(str(buf[82][1]))), flt.DataCell(flt.Text(str(buf[83][1]))),
                    flt.DataCell(flt.Text(str(buf[84][1]))), flt.DataCell(flt.Text(str(buf[85][1]))),
                    flt.DataCell(flt.Text(str(buf[86][1]))), flt.DataCell(flt.Text(str(buf[87][1]))),
                    flt.DataCell(flt.Text(str(buf[88][1]))), flt.DataCell(flt.Text(str(buf[89][1]))),
                    flt.DataCell(flt.Text(str(buf[90][1]))), flt.DataCell(flt.Text(str(buf[91][1]))),
                    flt.DataCell(flt.Text(str(buf[92][1]))), flt.DataCell(flt.Text(str(buf[93][1]))),
                    flt.DataCell(flt.Text(str(buf[94][1]))), flt.DataCell(flt.Text(str(buf[95][1]))),
                    flt.DataCell(flt.Text(str(buf[96][1]))), flt.DataCell(flt.Text(str(buf[97][1]))),
                    flt.DataCell(flt.Text(str(buf[98][1]))), flt.DataCell(flt.Text(str(buf[99][1]))),

                ],
            ),
            flt.DataRow(
                cells=[
                    flt.DataCell(flt.Text(str(buf[0][2]))), flt.DataCell(flt.Text(str(buf[1][2]))),
                    flt.DataCell(flt.Text(str(buf[2][2]))), flt.DataCell(flt.Text(str(buf[3][2]))),
                    flt.DataCell(flt.Text(str(buf[4][2]))), flt.DataCell(flt.Text(str(buf[5][2]))),
                    flt.DataCell(flt.Text(str(buf[6][2]))), flt.DataCell(flt.Text(str(buf[7][2]))),
                    flt.DataCell(flt.Text(str(buf[8][2]))), flt.DataCell(flt.Text(str(buf[9][2]))),
                    flt.DataCell(flt.Text(str(buf[10][2]))), flt.DataCell(flt.Text(str(buf[11][2]))),
                    flt.DataCell(flt.Text(str(buf[12][2]))), flt.DataCell(flt.Text(str(buf[13][2]))),
                    flt.DataCell(flt.Text(str(buf[14][2]))), flt.DataCell(flt.Text(str(buf[15][2]))),
                    flt.DataCell(flt.Text(str(buf[16][2]))), flt.DataCell(flt.Text(str(buf[17][2]))),
                    flt.DataCell(flt.Text(str(buf[18][2]))), flt.DataCell(flt.Text(str(buf[19][2]))),
                    flt.DataCell(flt.Text(str(buf[20][2]))), flt.DataCell(flt.Text(str(buf[21][2]))),
                    flt.DataCell(flt.Text(str(buf[22][2]))), flt.DataCell(flt.Text(str(buf[23][2]))),
                    flt.DataCell(flt.Text(str(buf[24][2]))), flt.DataCell(flt.Text(str(buf[25][2]))),
                    flt.DataCell(flt.Text(str(buf[26][2]))), flt.DataCell(flt.Text(str(buf[27][2]))),
                    flt.DataCell(flt.Text(str(buf[28][2]))), flt.DataCell(flt.Text(str(buf[29][2]))),
                    flt.DataCell(flt.Text(str(buf[30][2]))), flt.DataCell(flt.Text(str(buf[31][2]))),
                    flt.DataCell(flt.Text(str(buf[32][2]))), flt.DataCell(flt.Text(str(buf[33][2]))),
                    flt.DataCell(flt.Text(str(buf[34][2]))), flt.DataCell(flt.Text(str(buf[35][2]))),
                    flt.DataCell(flt.Text(str(buf[36][2]))), flt.DataCell(flt.Text(str(buf[37][2]))),
                    flt.DataCell(flt.Text(str(buf[38][2]))), flt.DataCell(flt.Text(str(buf[39][2]))),
                    flt.DataCell(flt.Text(str(buf[40][2]))), flt.DataCell(flt.Text(str(buf[41][2]))),
                    flt.DataCell(flt.Text(str(buf[42][2]))), flt.DataCell(flt.Text(str(buf[43][2]))),
                    flt.DataCell(flt.Text(str(buf[44][2]))), flt.DataCell(flt.Text(str(buf[45][2]))),
                    flt.DataCell(flt.Text(str(buf[46][2]))), flt.DataCell(flt.Text(str(buf[47][2]))),
                    flt.DataCell(flt.Text(str(buf[48][2]))), flt.DataCell(flt.Text(str(buf[49][2]))),
                    flt.DataCell(flt.Text(str(buf[50][2]))), flt.DataCell(flt.Text(str(buf[51][2]))),
                    flt.DataCell(flt.Text(str(buf[52][2]))), flt.DataCell(flt.Text(str(buf[53][2]))),
                    flt.DataCell(flt.Text(str(buf[54][2]))), flt.DataCell(flt.Text(str(buf[55][2]))),
                    flt.DataCell(flt.Text(str(buf[56][2]))), flt.DataCell(flt.Text(str(buf[57][2]))),
                    flt.DataCell(flt.Text(str(buf[58][2]))), flt.DataCell(flt.Text(str(buf[59][2]))),
                    flt.DataCell(flt.Text(str(buf[60][2]))), flt.DataCell(flt.Text(str(buf[61][2]))),
                    flt.DataCell(flt.Text(str(buf[62][2]))), flt.DataCell(flt.Text(str(buf[63][2]))),
                    flt.DataCell(flt.Text(str(buf[64][2]))), flt.DataCell(flt.Text(str(buf[65][2]))),
                    flt.DataCell(flt.Text(str(buf[66][2]))), flt.DataCell(flt.Text(str(buf[67][2]))),
                    flt.DataCell(flt.Text(str(buf[68][2]))), flt.DataCell(flt.Text(str(buf[69][2]))),
                    flt.DataCell(flt.Text(str(buf[70][2]))), flt.DataCell(flt.Text(str(buf[71][2]))),
                    flt.DataCell(flt.Text(str(buf[72][2]))), flt.DataCell(flt.Text(str(buf[73][2]))),
                    flt.DataCell(flt.Text(str(buf[74][2]))), flt.DataCell(flt.Text(str(buf[75][2]))),
                    flt.DataCell(flt.Text(str(buf[76][2]))), flt.DataCell(flt.Text(str(buf[77][2]))),
                    flt.DataCell(flt.Text(str(buf[78][2]))), flt.DataCell(flt.Text(str(buf[79][2]))),
                    flt.DataCell(flt.Text(str(buf[80][2]))), flt.DataCell(flt.Text(str(buf[81][2]))),
                    flt.DataCell(flt.Text(str(buf[82][2]))), flt.DataCell(flt.Text(str(buf[83][2]))),
                    flt.DataCell(flt.Text(str(buf[84][2]))), flt.DataCell(flt.Text(str(buf[85][2]))),
                    flt.DataCell(flt.Text(str(buf[86][2]))), flt.DataCell(flt.Text(str(buf[87][2]))),
                    flt.DataCell(flt.Text(str(buf[88][2]))), flt.DataCell(flt.Text(str(buf[89][2]))),
                    flt.DataCell(flt.Text(str(buf[90][2]))), flt.DataCell(flt.Text(str(buf[91][2]))),
                    flt.DataCell(flt.Text(str(buf[92][2]))), flt.DataCell(flt.Text(str(buf[93][2]))),
                    flt.DataCell(flt.Text(str(buf[94][2]))), flt.DataCell(flt.Text(str(buf[95][2]))),
                    flt.DataCell(flt.Text(str(buf[96][2]))), flt.DataCell(flt.Text(str(buf[97][2]))),
                    flt.DataCell(flt.Text(str(buf[98][2]))), flt.DataCell(flt.Text(str(buf[99][2]))),

                ],
            ),
            flt.DataRow(
                cells=[
                    flt.DataCell(flt.Text(str(buf[0][3]))), flt.DataCell(flt.Text(str(buf[1][3]))),
                    flt.DataCell(flt.Text(str(buf[2][3]))), flt.DataCell(flt.Text(str(buf[3][3]))),
                    flt.DataCell(flt.Text(str(buf[4][3]))), flt.DataCell(flt.Text(str(buf[5][3]))),
                    flt.DataCell(flt.Text(str(buf[6][3]))), flt.DataCell(flt.Text(str(buf[7][3]))),
                    flt.DataCell(flt.Text(str(buf[8][3]))), flt.DataCell(flt.Text(str(buf[9][3]))),
                    flt.DataCell(flt.Text(str(buf[10][3]))), flt.DataCell(flt.Text(str(buf[11][3]))),
                    flt.DataCell(flt.Text(str(buf[12][3]))), flt.DataCell(flt.Text(str(buf[13][3]))),
                    flt.DataCell(flt.Text(str(buf[14][3]))), flt.DataCell(flt.Text(str(buf[15][3]))),
                    flt.DataCell(flt.Text(str(buf[16][3]))), flt.DataCell(flt.Text(str(buf[17][3]))),
                    flt.DataCell(flt.Text(str(buf[18][3]))), flt.DataCell(flt.Text(str(buf[19][3]))),
                    flt.DataCell(flt.Text(str(buf[20][3]))), flt.DataCell(flt.Text(str(buf[21][3]))),
                    flt.DataCell(flt.Text(str(buf[22][3]))), flt.DataCell(flt.Text(str(buf[23][3]))),
                    flt.DataCell(flt.Text(str(buf[24][3]))), flt.DataCell(flt.Text(str(buf[25][3]))),
                    flt.DataCell(flt.Text(str(buf[26][3]))), flt.DataCell(flt.Text(str(buf[27][3]))),
                    flt.DataCell(flt.Text(str(buf[28][3]))), flt.DataCell(flt.Text(str(buf[29][3]))),
                    flt.DataCell(flt.Text(str(buf[30][3]))), flt.DataCell(flt.Text(str(buf[31][3]))),
                    flt.DataCell(flt.Text(str(buf[32][3]))), flt.DataCell(flt.Text(str(buf[33][3]))),
                    flt.DataCell(flt.Text(str(buf[34][3]))), flt.DataCell(flt.Text(str(buf[35][3]))),
                    flt.DataCell(flt.Text(str(buf[36][3]))), flt.DataCell(flt.Text(str(buf[37][3]))),
                    flt.DataCell(flt.Text(str(buf[38][3]))), flt.DataCell(flt.Text(str(buf[39][3]))),
                    flt.DataCell(flt.Text(str(buf[40][3]))), flt.DataCell(flt.Text(str(buf[41][3]))),
                    flt.DataCell(flt.Text(str(buf[42][3]))), flt.DataCell(flt.Text(str(buf[43][3]))),
                    flt.DataCell(flt.Text(str(buf[44][3]))), flt.DataCell(flt.Text(str(buf[45][3]))),
                    flt.DataCell(flt.Text(str(buf[46][3]))), flt.DataCell(flt.Text(str(buf[47][3]))),
                    flt.DataCell(flt.Text(str(buf[48][3]))), flt.DataCell(flt.Text(str(buf[49][3]))),
                    flt.DataCell(flt.Text(str(buf[50][3]))), flt.DataCell(flt.Text(str(buf[51][3]))),
                    flt.DataCell(flt.Text(str(buf[52][3]))), flt.DataCell(flt.Text(str(buf[53][3]))),
                    flt.DataCell(flt.Text(str(buf[54][3]))), flt.DataCell(flt.Text(str(buf[55][3]))),
                    flt.DataCell(flt.Text(str(buf[56][3]))), flt.DataCell(flt.Text(str(buf[57][3]))),
                    flt.DataCell(flt.Text(str(buf[58][3]))), flt.DataCell(flt.Text(str(buf[59][3]))),
                    flt.DataCell(flt.Text(str(buf[60][3]))), flt.DataCell(flt.Text(str(buf[61][3]))),
                    flt.DataCell(flt.Text(str(buf[62][3]))), flt.DataCell(flt.Text(str(buf[63][3]))),
                    flt.DataCell(flt.Text(str(buf[64][3]))), flt.DataCell(flt.Text(str(buf[65][3]))),
                    flt.DataCell(flt.Text(str(buf[66][3]))), flt.DataCell(flt.Text(str(buf[67][3]))),
                    flt.DataCell(flt.Text(str(buf[68][3]))), flt.DataCell(flt.Text(str(buf[69][3]))),
                    flt.DataCell(flt.Text(str(buf[70][3]))), flt.DataCell(flt.Text(str(buf[71][3]))),
                    flt.DataCell(flt.Text(str(buf[72][3]))), flt.DataCell(flt.Text(str(buf[73][3]))),
                    flt.DataCell(flt.Text(str(buf[74][3]))), flt.DataCell(flt.Text(str(buf[75][3]))),
                    flt.DataCell(flt.Text(str(buf[76][3]))), flt.DataCell(flt.Text(str(buf[77][3]))),
                    flt.DataCell(flt.Text(str(buf[78][3]))), flt.DataCell(flt.Text(str(buf[79][3]))),
                    flt.DataCell(flt.Text(str(buf[80][3]))), flt.DataCell(flt.Text(str(buf[81][3]))),
                    flt.DataCell(flt.Text(str(buf[82][3]))), flt.DataCell(flt.Text(str(buf[83][3]))),
                    flt.DataCell(flt.Text(str(buf[84][3]))), flt.DataCell(flt.Text(str(buf[85][3]))),
                    flt.DataCell(flt.Text(str(buf[86][3]))), flt.DataCell(flt.Text(str(buf[87][3]))),
                    flt.DataCell(flt.Text(str(buf[88][3]))), flt.DataCell(flt.Text(str(buf[89][3]))),
                    flt.DataCell(flt.Text(str(buf[90][3]))), flt.DataCell(flt.Text(str(buf[91][3]))),
                    flt.DataCell(flt.Text(str(buf[92][3]))), flt.DataCell(flt.Text(str(buf[93][3]))),
                    flt.DataCell(flt.Text(str(buf[94][3]))), flt.DataCell(flt.Text(str(buf[95][3]))),
                    flt.DataCell(flt.Text(str(buf[96][3]))), flt.DataCell(flt.Text(str(buf[97][3]))),
                    flt.DataCell(flt.Text(str(buf[98][3]))), flt.DataCell(flt.Text(str(buf[99][3]))),

                ],
            ),
            flt.DataRow(
                cells=[
                    flt.DataCell(flt.Text(str(buf[0][4]))), flt.DataCell(flt.Text(str(buf[1][4]))),
                    flt.DataCell(flt.Text(str(buf[2][4]))), flt.DataCell(flt.Text(str(buf[3][4]))),
                    flt.DataCell(flt.Text(str(buf[4][4]))), flt.DataCell(flt.Text(str(buf[5][4]))),
                    flt.DataCell(flt.Text(str(buf[6][4]))), flt.DataCell(flt.Text(str(buf[7][4]))),
                    flt.DataCell(flt.Text(str(buf[8][4]))), flt.DataCell(flt.Text(str(buf[9][4]))),
                    flt.DataCell(flt.Text(str(buf[10][4]))), flt.DataCell(flt.Text(str(buf[11][4]))),
                    flt.DataCell(flt.Text(str(buf[12][4]))), flt.DataCell(flt.Text(str(buf[13][4]))),
                    flt.DataCell(flt.Text(str(buf[14][4]))), flt.DataCell(flt.Text(str(buf[15][4]))),
                    flt.DataCell(flt.Text(str(buf[16][4]))), flt.DataCell(flt.Text(str(buf[17][4]))),
                    flt.DataCell(flt.Text(str(buf[18][4]))), flt.DataCell(flt.Text(str(buf[19][4]))),
                    flt.DataCell(flt.Text(str(buf[20][4]))), flt.DataCell(flt.Text(str(buf[21][4]))),
                    flt.DataCell(flt.Text(str(buf[22][4]))), flt.DataCell(flt.Text(str(buf[23][4]))),
                    flt.DataCell(flt.Text(str(buf[24][4]))), flt.DataCell(flt.Text(str(buf[25][4]))),
                    flt.DataCell(flt.Text(str(buf[26][4]))), flt.DataCell(flt.Text(str(buf[27][4]))),
                    flt.DataCell(flt.Text(str(buf[28][4]))), flt.DataCell(flt.Text(str(buf[29][4]))),
                    flt.DataCell(flt.Text(str(buf[30][4]))), flt.DataCell(flt.Text(str(buf[31][4]))),
                    flt.DataCell(flt.Text(str(buf[32][4]))), flt.DataCell(flt.Text(str(buf[33][4]))),
                    flt.DataCell(flt.Text(str(buf[34][4]))), flt.DataCell(flt.Text(str(buf[35][4]))),
                    flt.DataCell(flt.Text(str(buf[36][4]))), flt.DataCell(flt.Text(str(buf[37][4]))),
                    flt.DataCell(flt.Text(str(buf[38][4]))), flt.DataCell(flt.Text(str(buf[39][4]))),
                    flt.DataCell(flt.Text(str(buf[40][4]))), flt.DataCell(flt.Text(str(buf[41][4]))),
                    flt.DataCell(flt.Text(str(buf[42][4]))), flt.DataCell(flt.Text(str(buf[43][4]))),
                    flt.DataCell(flt.Text(str(buf[44][4]))), flt.DataCell(flt.Text(str(buf[45][4]))),
                    flt.DataCell(flt.Text(str(buf[46][4]))), flt.DataCell(flt.Text(str(buf[47][4]))),
                    flt.DataCell(flt.Text(str(buf[48][4]))), flt.DataCell(flt.Text(str(buf[49][4]))),
                    flt.DataCell(flt.Text(str(buf[50][4]))), flt.DataCell(flt.Text(str(buf[51][4]))),
                    flt.DataCell(flt.Text(str(buf[52][4]))), flt.DataCell(flt.Text(str(buf[53][4]))),
                    flt.DataCell(flt.Text(str(buf[54][4]))), flt.DataCell(flt.Text(str(buf[55][4]))),
                    flt.DataCell(flt.Text(str(buf[56][4]))), flt.DataCell(flt.Text(str(buf[57][4]))),
                    flt.DataCell(flt.Text(str(buf[58][4]))), flt.DataCell(flt.Text(str(buf[59][4]))),
                    flt.DataCell(flt.Text(str(buf[60][4]))), flt.DataCell(flt.Text(str(buf[61][4]))),
                    flt.DataCell(flt.Text(str(buf[62][4]))), flt.DataCell(flt.Text(str(buf[63][4]))),
                    flt.DataCell(flt.Text(str(buf[64][4]))), flt.DataCell(flt.Text(str(buf[65][4]))),
                    flt.DataCell(flt.Text(str(buf[66][4]))), flt.DataCell(flt.Text(str(buf[67][4]))),
                    flt.DataCell(flt.Text(str(buf[68][4]))), flt.DataCell(flt.Text(str(buf[69][4]))),
                    flt.DataCell(flt.Text(str(buf[70][4]))), flt.DataCell(flt.Text(str(buf[71][4]))),
                    flt.DataCell(flt.Text(str(buf[72][4]))), flt.DataCell(flt.Text(str(buf[73][4]))),
                    flt.DataCell(flt.Text(str(buf[74][4]))), flt.DataCell(flt.Text(str(buf[75][4]))),
                    flt.DataCell(flt.Text(str(buf[76][4]))), flt.DataCell(flt.Text(str(buf[77][4]))),
                    flt.DataCell(flt.Text(str(buf[78][4]))), flt.DataCell(flt.Text(str(buf[79][4]))),
                    flt.DataCell(flt.Text(str(buf[80][4]))), flt.DataCell(flt.Text(str(buf[81][4]))),
                    flt.DataCell(flt.Text(str(buf[82][4]))), flt.DataCell(flt.Text(str(buf[83][4]))),
                    flt.DataCell(flt.Text(str(buf[84][4]))), flt.DataCell(flt.Text(str(buf[85][4]))),
                    flt.DataCell(flt.Text(str(buf[86][4]))), flt.DataCell(flt.Text(str(buf[87][4]))),
                    flt.DataCell(flt.Text(str(buf[88][4]))), flt.DataCell(flt.Text(str(buf[89][4]))),
                    flt.DataCell(flt.Text(str(buf[90][4]))), flt.DataCell(flt.Text(str(buf[91][4]))),
                    flt.DataCell(flt.Text(str(buf[92][4]))), flt.DataCell(flt.Text(str(buf[93][4]))),
                    flt.DataCell(flt.Text(str(buf[94][4]))), flt.DataCell(flt.Text(str(buf[95][4]))),
                    flt.DataCell(flt.Text(str(buf[96][4]))), flt.DataCell(flt.Text(str(buf[97][4]))),
                    flt.DataCell(flt.Text(str(buf[98][4]))), flt.DataCell(flt.Text(str(buf[99][4]))),

                ],
            ),
            flt.DataRow(
                cells=[
                    flt.DataCell(flt.Text(str(buf[0][5]))), flt.DataCell(flt.Text(str(buf[1][5]))),
                    flt.DataCell(flt.Text(str(buf[2][5]))), flt.DataCell(flt.Text(str(buf[3][5]))),
                    flt.DataCell(flt.Text(str(buf[4][5]))), flt.DataCell(flt.Text(str(buf[5][5]))),
                    flt.DataCell(flt.Text(str(buf[6][5]))), flt.DataCell(flt.Text(str(buf[7][5]))),
                    flt.DataCell(flt.Text(str(buf[8][5]))), flt.DataCell(flt.Text(str(buf[9][5]))),
                    flt.DataCell(flt.Text(str(buf[10][5]))), flt.DataCell(flt.Text(str(buf[11][5]))),
                    flt.DataCell(flt.Text(str(buf[12][5]))), flt.DataCell(flt.Text(str(buf[13][5]))),
                    flt.DataCell(flt.Text(str(buf[14][5]))), flt.DataCell(flt.Text(str(buf[15][5]))),
                    flt.DataCell(flt.Text(str(buf[16][5]))), flt.DataCell(flt.Text(str(buf[17][5]))),
                    flt.DataCell(flt.Text(str(buf[18][5]))), flt.DataCell(flt.Text(str(buf[19][5]))),
                    flt.DataCell(flt.Text(str(buf[20][5]))), flt.DataCell(flt.Text(str(buf[21][5]))),
                    flt.DataCell(flt.Text(str(buf[22][5]))), flt.DataCell(flt.Text(str(buf[23][5]))),
                    flt.DataCell(flt.Text(str(buf[24][5]))), flt.DataCell(flt.Text(str(buf[25][5]))),
                    flt.DataCell(flt.Text(str(buf[26][5]))), flt.DataCell(flt.Text(str(buf[27][5]))),
                    flt.DataCell(flt.Text(str(buf[28][5]))), flt.DataCell(flt.Text(str(buf[29][5]))),
                    flt.DataCell(flt.Text(str(buf[30][5]))), flt.DataCell(flt.Text(str(buf[31][5]))),
                    flt.DataCell(flt.Text(str(buf[32][5]))), flt.DataCell(flt.Text(str(buf[33][5]))),
                    flt.DataCell(flt.Text(str(buf[34][5]))), flt.DataCell(flt.Text(str(buf[35][5]))),
                    flt.DataCell(flt.Text(str(buf[36][5]))), flt.DataCell(flt.Text(str(buf[37][5]))),
                    flt.DataCell(flt.Text(str(buf[38][5]))), flt.DataCell(flt.Text(str(buf[39][5]))),
                    flt.DataCell(flt.Text(str(buf[40][5]))), flt.DataCell(flt.Text(str(buf[41][5]))),
                    flt.DataCell(flt.Text(str(buf[42][5]))), flt.DataCell(flt.Text(str(buf[43][5]))),
                    flt.DataCell(flt.Text(str(buf[44][5]))), flt.DataCell(flt.Text(str(buf[45][5]))),
                    flt.DataCell(flt.Text(str(buf[46][5]))), flt.DataCell(flt.Text(str(buf[47][5]))),
                    flt.DataCell(flt.Text(str(buf[48][5]))), flt.DataCell(flt.Text(str(buf[49][5]))),
                    flt.DataCell(flt.Text(str(buf[50][5]))), flt.DataCell(flt.Text(str(buf[51][5]))),
                    flt.DataCell(flt.Text(str(buf[52][5]))), flt.DataCell(flt.Text(str(buf[53][5]))),
                    flt.DataCell(flt.Text(str(buf[54][5]))), flt.DataCell(flt.Text(str(buf[55][5]))),
                    flt.DataCell(flt.Text(str(buf[56][5]))), flt.DataCell(flt.Text(str(buf[57][5]))),
                    flt.DataCell(flt.Text(str(buf[58][5]))), flt.DataCell(flt.Text(str(buf[59][5]))),
                    flt.DataCell(flt.Text(str(buf[60][5]))), flt.DataCell(flt.Text(str(buf[61][5]))),
                    flt.DataCell(flt.Text(str(buf[62][5]))), flt.DataCell(flt.Text(str(buf[63][5]))),
                    flt.DataCell(flt.Text(str(buf[64][5]))), flt.DataCell(flt.Text(str(buf[65][5]))),
                    flt.DataCell(flt.Text(str(buf[66][5]))), flt.DataCell(flt.Text(str(buf[67][5]))),
                    flt.DataCell(flt.Text(str(buf[68][5]))), flt.DataCell(flt.Text(str(buf[69][5]))),
                    flt.DataCell(flt.Text(str(buf[70][5]))), flt.DataCell(flt.Text(str(buf[71][5]))),
                    flt.DataCell(flt.Text(str(buf[72][5]))), flt.DataCell(flt.Text(str(buf[73][5]))),
                    flt.DataCell(flt.Text(str(buf[74][5]))), flt.DataCell(flt.Text(str(buf[75][5]))),
                    flt.DataCell(flt.Text(str(buf[76][5]))), flt.DataCell(flt.Text(str(buf[77][5]))),
                    flt.DataCell(flt.Text(str(buf[78][5]))), flt.DataCell(flt.Text(str(buf[79][5]))),
                    flt.DataCell(flt.Text(str(buf[80][5]))), flt.DataCell(flt.Text(str(buf[81][5]))),
                    flt.DataCell(flt.Text(str(buf[82][5]))), flt.DataCell(flt.Text(str(buf[83][5]))),
                    flt.DataCell(flt.Text(str(buf[84][5]))), flt.DataCell(flt.Text(str(buf[85][5]))),
                    flt.DataCell(flt.Text(str(buf[86][5]))), flt.DataCell(flt.Text(str(buf[87][5]))),
                    flt.DataCell(flt.Text(str(buf[88][5]))), flt.DataCell(flt.Text(str(buf[89][5]))),
                    flt.DataCell(flt.Text(str(buf[90][5]))), flt.DataCell(flt.Text(str(buf[91][5]))),
                    flt.DataCell(flt.Text(str(buf[92][5]))), flt.DataCell(flt.Text(str(buf[93][5]))),
                    flt.DataCell(flt.Text(str(buf[94][5]))), flt.DataCell(flt.Text(str(buf[95][5]))),
                    flt.DataCell(flt.Text(str(buf[96][5]))), flt.DataCell(flt.Text(str(buf[97][5]))),
                    flt.DataCell(flt.Text(str(buf[98][5]))), flt.DataCell(flt.Text(str(buf[99][5]))),

                ],
            ),
            flt.DataRow(
                cells=[
                    flt.DataCell(flt.Text(str(buf[0][6]))), flt.DataCell(flt.Text(str(buf[1][6]))),
                    flt.DataCell(flt.Text(str(buf[2][6]))), flt.DataCell(flt.Text(str(buf[3][6]))),
                    flt.DataCell(flt.Text(str(buf[4][6]))), flt.DataCell(flt.Text(str(buf[5][6]))),
                    flt.DataCell(flt.Text(str(buf[6][6]))), flt.DataCell(flt.Text(str(buf[7][6]))),
                    flt.DataCell(flt.Text(str(buf[8][6]))), flt.DataCell(flt.Text(str(buf[9][6]))),
                    flt.DataCell(flt.Text(str(buf[10][6]))), flt.DataCell(flt.Text(str(buf[11][6]))),
                    flt.DataCell(flt.Text(str(buf[12][6]))), flt.DataCell(flt.Text(str(buf[13][6]))),
                    flt.DataCell(flt.Text(str(buf[14][6]))), flt.DataCell(flt.Text(str(buf[15][6]))),
                    flt.DataCell(flt.Text(str(buf[16][6]))), flt.DataCell(flt.Text(str(buf[17][6]))),
                    flt.DataCell(flt.Text(str(buf[18][6]))), flt.DataCell(flt.Text(str(buf[19][6]))),
                    flt.DataCell(flt.Text(str(buf[20][6]))), flt.DataCell(flt.Text(str(buf[21][6]))),
                    flt.DataCell(flt.Text(str(buf[22][6]))), flt.DataCell(flt.Text(str(buf[23][6]))),
                    flt.DataCell(flt.Text(str(buf[24][6]))), flt.DataCell(flt.Text(str(buf[25][6]))),
                    flt.DataCell(flt.Text(str(buf[26][6]))), flt.DataCell(flt.Text(str(buf[27][6]))),
                    flt.DataCell(flt.Text(str(buf[28][6]))), flt.DataCell(flt.Text(str(buf[29][6]))),
                    flt.DataCell(flt.Text(str(buf[30][6]))), flt.DataCell(flt.Text(str(buf[31][6]))),
                    flt.DataCell(flt.Text(str(buf[32][6]))), flt.DataCell(flt.Text(str(buf[33][6]))),
                    flt.DataCell(flt.Text(str(buf[34][6]))), flt.DataCell(flt.Text(str(buf[35][6]))),
                    flt.DataCell(flt.Text(str(buf[36][6]))), flt.DataCell(flt.Text(str(buf[37][6]))),
                    flt.DataCell(flt.Text(str(buf[38][6]))), flt.DataCell(flt.Text(str(buf[39][6]))),
                    flt.DataCell(flt.Text(str(buf[40][6]))), flt.DataCell(flt.Text(str(buf[41][6]))),
                    flt.DataCell(flt.Text(str(buf[42][6]))), flt.DataCell(flt.Text(str(buf[43][6]))),
                    flt.DataCell(flt.Text(str(buf[44][6]))), flt.DataCell(flt.Text(str(buf[45][6]))),
                    flt.DataCell(flt.Text(str(buf[46][6]))), flt.DataCell(flt.Text(str(buf[47][6]))),
                    flt.DataCell(flt.Text(str(buf[48][6]))), flt.DataCell(flt.Text(str(buf[49][6]))),
                    flt.DataCell(flt.Text(str(buf[50][6]))), flt.DataCell(flt.Text(str(buf[51][6]))),
                    flt.DataCell(flt.Text(str(buf[52][6]))), flt.DataCell(flt.Text(str(buf[53][6]))),
                    flt.DataCell(flt.Text(str(buf[54][6]))), flt.DataCell(flt.Text(str(buf[55][6]))),
                    flt.DataCell(flt.Text(str(buf[56][6]))), flt.DataCell(flt.Text(str(buf[57][6]))),
                    flt.DataCell(flt.Text(str(buf[58][6]))), flt.DataCell(flt.Text(str(buf[59][6]))),
                    flt.DataCell(flt.Text(str(buf[60][6]))), flt.DataCell(flt.Text(str(buf[61][6]))),
                    flt.DataCell(flt.Text(str(buf[62][6]))), flt.DataCell(flt.Text(str(buf[63][6]))),
                    flt.DataCell(flt.Text(str(buf[64][6]))), flt.DataCell(flt.Text(str(buf[65][6]))),
                    flt.DataCell(flt.Text(str(buf[66][6]))), flt.DataCell(flt.Text(str(buf[67][6]))),
                    flt.DataCell(flt.Text(str(buf[68][6]))), flt.DataCell(flt.Text(str(buf[69][6]))),
                    flt.DataCell(flt.Text(str(buf[70][6]))), flt.DataCell(flt.Text(str(buf[71][6]))),
                    flt.DataCell(flt.Text(str(buf[72][6]))), flt.DataCell(flt.Text(str(buf[73][6]))),
                    flt.DataCell(flt.Text(str(buf[74][6]))), flt.DataCell(flt.Text(str(buf[75][6]))),
                    flt.DataCell(flt.Text(str(buf[76][6]))), flt.DataCell(flt.Text(str(buf[77][6]))),
                    flt.DataCell(flt.Text(str(buf[78][6]))), flt.DataCell(flt.Text(str(buf[79][6]))),
                    flt.DataCell(flt.Text(str(buf[80][6]))), flt.DataCell(flt.Text(str(buf[81][6]))),
                    flt.DataCell(flt.Text(str(buf[82][6]))), flt.DataCell(flt.Text(str(buf[83][6]))),
                    flt.DataCell(flt.Text(str(buf[84][6]))), flt.DataCell(flt.Text(str(buf[85][6]))),
                    flt.DataCell(flt.Text(str(buf[86][6]))), flt.DataCell(flt.Text(str(buf[87][6]))),
                    flt.DataCell(flt.Text(str(buf[88][6]))), flt.DataCell(flt.Text(str(buf[89][6]))),
                    flt.DataCell(flt.Text(str(buf[90][6]))), flt.DataCell(flt.Text(str(buf[91][6]))),
                    flt.DataCell(flt.Text(str(buf[92][6]))), flt.DataCell(flt.Text(str(buf[93][6]))),
                    flt.DataCell(flt.Text(str(buf[94][6]))), flt.DataCell(flt.Text(str(buf[95][6]))),
                    flt.DataCell(flt.Text(str(buf[96][6]))), flt.DataCell(flt.Text(str(buf[97][6]))),
                    flt.DataCell(flt.Text(str(buf[98][6]))), flt.DataCell(flt.Text(str(buf[99][6]))),

                ],
            ),
            flt.DataRow(
                cells=[
                    flt.DataCell(flt.Text(str(buf[0][7]))), flt.DataCell(flt.Text(str(buf[1][7]))),
                    flt.DataCell(flt.Text(str(buf[2][7]))), flt.DataCell(flt.Text(str(buf[3][7]))),
                    flt.DataCell(flt.Text(str(buf[4][7]))), flt.DataCell(flt.Text(str(buf[5][7]))),
                    flt.DataCell(flt.Text(str(buf[6][7]))), flt.DataCell(flt.Text(str(buf[7][7]))),
                    flt.DataCell(flt.Text(str(buf[8][7]))), flt.DataCell(flt.Text(str(buf[9][7]))),
                    flt.DataCell(flt.Text(str(buf[10][7]))), flt.DataCell(flt.Text(str(buf[11][7]))),
                    flt.DataCell(flt.Text(str(buf[12][7]))), flt.DataCell(flt.Text(str(buf[13][7]))),
                    flt.DataCell(flt.Text(str(buf[14][7]))), flt.DataCell(flt.Text(str(buf[15][7]))),
                    flt.DataCell(flt.Text(str(buf[16][7]))), flt.DataCell(flt.Text(str(buf[17][7]))),
                    flt.DataCell(flt.Text(str(buf[18][7]))), flt.DataCell(flt.Text(str(buf[19][7]))),
                    flt.DataCell(flt.Text(str(buf[20][7]))), flt.DataCell(flt.Text(str(buf[21][7]))),
                    flt.DataCell(flt.Text(str(buf[22][7]))), flt.DataCell(flt.Text(str(buf[23][7]))),
                    flt.DataCell(flt.Text(str(buf[24][7]))), flt.DataCell(flt.Text(str(buf[25][7]))),
                    flt.DataCell(flt.Text(str(buf[26][7]))), flt.DataCell(flt.Text(str(buf[27][7]))),
                    flt.DataCell(flt.Text(str(buf[28][7]))), flt.DataCell(flt.Text(str(buf[29][7]))),
                    flt.DataCell(flt.Text(str(buf[30][7]))), flt.DataCell(flt.Text(str(buf[31][7]))),
                    flt.DataCell(flt.Text(str(buf[32][7]))), flt.DataCell(flt.Text(str(buf[33][7]))),
                    flt.DataCell(flt.Text(str(buf[34][7]))), flt.DataCell(flt.Text(str(buf[35][7]))),
                    flt.DataCell(flt.Text(str(buf[36][7]))), flt.DataCell(flt.Text(str(buf[37][7]))),
                    flt.DataCell(flt.Text(str(buf[38][7]))), flt.DataCell(flt.Text(str(buf[39][7]))),
                    flt.DataCell(flt.Text(str(buf[40][7]))), flt.DataCell(flt.Text(str(buf[41][7]))),
                    flt.DataCell(flt.Text(str(buf[42][7]))), flt.DataCell(flt.Text(str(buf[43][7]))),
                    flt.DataCell(flt.Text(str(buf[44][7]))), flt.DataCell(flt.Text(str(buf[45][7]))),
                    flt.DataCell(flt.Text(str(buf[46][7]))), flt.DataCell(flt.Text(str(buf[47][7]))),
                    flt.DataCell(flt.Text(str(buf[48][7]))), flt.DataCell(flt.Text(str(buf[49][7]))),
                    flt.DataCell(flt.Text(str(buf[50][7]))), flt.DataCell(flt.Text(str(buf[51][7]))),
                    flt.DataCell(flt.Text(str(buf[52][7]))), flt.DataCell(flt.Text(str(buf[53][7]))),
                    flt.DataCell(flt.Text(str(buf[54][7]))), flt.DataCell(flt.Text(str(buf[55][7]))),
                    flt.DataCell(flt.Text(str(buf[56][7]))), flt.DataCell(flt.Text(str(buf[57][7]))),
                    flt.DataCell(flt.Text(str(buf[58][7]))), flt.DataCell(flt.Text(str(buf[59][7]))),
                    flt.DataCell(flt.Text(str(buf[60][7]))), flt.DataCell(flt.Text(str(buf[61][7]))),
                    flt.DataCell(flt.Text(str(buf[62][7]))), flt.DataCell(flt.Text(str(buf[63][7]))),
                    flt.DataCell(flt.Text(str(buf[64][7]))), flt.DataCell(flt.Text(str(buf[65][7]))),
                    flt.DataCell(flt.Text(str(buf[66][7]))), flt.DataCell(flt.Text(str(buf[67][7]))),
                    flt.DataCell(flt.Text(str(buf[68][7]))), flt.DataCell(flt.Text(str(buf[69][7]))),
                    flt.DataCell(flt.Text(str(buf[70][7]))), flt.DataCell(flt.Text(str(buf[71][7]))),
                    flt.DataCell(flt.Text(str(buf[72][7]))), flt.DataCell(flt.Text(str(buf[73][7]))),
                    flt.DataCell(flt.Text(str(buf[74][7]))), flt.DataCell(flt.Text(str(buf[75][7]))),
                    flt.DataCell(flt.Text(str(buf[76][7]))), flt.DataCell(flt.Text(str(buf[77][7]))),
                    flt.DataCell(flt.Text(str(buf[78][7]))), flt.DataCell(flt.Text(str(buf[79][7]))),
                    flt.DataCell(flt.Text(str(buf[80][7]))), flt.DataCell(flt.Text(str(buf[81][7]))),
                    flt.DataCell(flt.Text(str(buf[82][7]))), flt.DataCell(flt.Text(str(buf[83][7]))),
                    flt.DataCell(flt.Text(str(buf[84][7]))), flt.DataCell(flt.Text(str(buf[85][7]))),
                    flt.DataCell(flt.Text(str(buf[86][7]))), flt.DataCell(flt.Text(str(buf[87][7]))),
                    flt.DataCell(flt.Text(str(buf[88][7]))), flt.DataCell(flt.Text(str(buf[89][7]))),
                    flt.DataCell(flt.Text(str(buf[90][7]))), flt.DataCell(flt.Text(str(buf[91][7]))),
                    flt.DataCell(flt.Text(str(buf[92][7]))), flt.DataCell(flt.Text(str(buf[93][7]))),
                    flt.DataCell(flt.Text(str(buf[94][7]))), flt.DataCell(flt.Text(str(buf[95][7]))),
                    flt.DataCell(flt.Text(str(buf[96][7]))), flt.DataCell(flt.Text(str(buf[97][7]))),
                    flt.DataCell(flt.Text(str(buf[98][7]))), flt.DataCell(flt.Text(str(buf[99][7]))),

                ],
            ),
            flt.DataRow(
                cells=[
                    flt.DataCell(flt.Text(str(buf[0][8]))), flt.DataCell(flt.Text(str(buf[1][8]))),
                    flt.DataCell(flt.Text(str(buf[2][8]))), flt.DataCell(flt.Text(str(buf[3][8]))),
                    flt.DataCell(flt.Text(str(buf[4][8]))), flt.DataCell(flt.Text(str(buf[5][8]))),
                    flt.DataCell(flt.Text(str(buf[6][8]))), flt.DataCell(flt.Text(str(buf[7][8]))),
                    flt.DataCell(flt.Text(str(buf[8][8]))), flt.DataCell(flt.Text(str(buf[9][8]))),
                    flt.DataCell(flt.Text(str(buf[10][8]))), flt.DataCell(flt.Text(str(buf[11][8]))),
                    flt.DataCell(flt.Text(str(buf[12][8]))), flt.DataCell(flt.Text(str(buf[13][8]))),
                    flt.DataCell(flt.Text(str(buf[14][8]))), flt.DataCell(flt.Text(str(buf[15][8]))),
                    flt.DataCell(flt.Text(str(buf[16][8]))), flt.DataCell(flt.Text(str(buf[17][8]))),
                    flt.DataCell(flt.Text(str(buf[18][8]))), flt.DataCell(flt.Text(str(buf[19][8]))),
                    flt.DataCell(flt.Text(str(buf[20][8]))), flt.DataCell(flt.Text(str(buf[21][8]))),
                    flt.DataCell(flt.Text(str(buf[22][8]))), flt.DataCell(flt.Text(str(buf[23][8]))),
                    flt.DataCell(flt.Text(str(buf[24][8]))), flt.DataCell(flt.Text(str(buf[25][8]))),
                    flt.DataCell(flt.Text(str(buf[26][8]))), flt.DataCell(flt.Text(str(buf[27][8]))),
                    flt.DataCell(flt.Text(str(buf[28][8]))), flt.DataCell(flt.Text(str(buf[29][8]))),
                    flt.DataCell(flt.Text(str(buf[30][8]))), flt.DataCell(flt.Text(str(buf[31][8]))),
                    flt.DataCell(flt.Text(str(buf[32][8]))), flt.DataCell(flt.Text(str(buf[33][8]))),
                    flt.DataCell(flt.Text(str(buf[34][8]))), flt.DataCell(flt.Text(str(buf[35][8]))),
                    flt.DataCell(flt.Text(str(buf[36][8]))), flt.DataCell(flt.Text(str(buf[37][8]))),
                    flt.DataCell(flt.Text(str(buf[38][8]))), flt.DataCell(flt.Text(str(buf[39][8]))),
                    flt.DataCell(flt.Text(str(buf[40][8]))), flt.DataCell(flt.Text(str(buf[41][8]))),
                    flt.DataCell(flt.Text(str(buf[42][8]))), flt.DataCell(flt.Text(str(buf[43][8]))),
                    flt.DataCell(flt.Text(str(buf[44][8]))), flt.DataCell(flt.Text(str(buf[45][8]))),
                    flt.DataCell(flt.Text(str(buf[46][8]))), flt.DataCell(flt.Text(str(buf[47][8]))),
                    flt.DataCell(flt.Text(str(buf[48][8]))), flt.DataCell(flt.Text(str(buf[49][8]))),
                    flt.DataCell(flt.Text(str(buf[50][8]))), flt.DataCell(flt.Text(str(buf[51][8]))),
                    flt.DataCell(flt.Text(str(buf[52][8]))), flt.DataCell(flt.Text(str(buf[53][8]))),
                    flt.DataCell(flt.Text(str(buf[54][8]))), flt.DataCell(flt.Text(str(buf[55][8]))),
                    flt.DataCell(flt.Text(str(buf[56][8]))), flt.DataCell(flt.Text(str(buf[57][8]))),
                    flt.DataCell(flt.Text(str(buf[58][8]))), flt.DataCell(flt.Text(str(buf[59][8]))),
                    flt.DataCell(flt.Text(str(buf[60][8]))), flt.DataCell(flt.Text(str(buf[61][8]))),
                    flt.DataCell(flt.Text(str(buf[62][8]))), flt.DataCell(flt.Text(str(buf[63][8]))),
                    flt.DataCell(flt.Text(str(buf[64][8]))), flt.DataCell(flt.Text(str(buf[65][8]))),
                    flt.DataCell(flt.Text(str(buf[66][8]))), flt.DataCell(flt.Text(str(buf[67][8]))),
                    flt.DataCell(flt.Text(str(buf[68][8]))), flt.DataCell(flt.Text(str(buf[69][8]))),
                    flt.DataCell(flt.Text(str(buf[70][8]))), flt.DataCell(flt.Text(str(buf[71][8]))),
                    flt.DataCell(flt.Text(str(buf[72][8]))), flt.DataCell(flt.Text(str(buf[73][8]))),
                    flt.DataCell(flt.Text(str(buf[74][8]))), flt.DataCell(flt.Text(str(buf[75][8]))),
                    flt.DataCell(flt.Text(str(buf[76][8]))), flt.DataCell(flt.Text(str(buf[77][8]))),
                    flt.DataCell(flt.Text(str(buf[78][8]))), flt.DataCell(flt.Text(str(buf[79][8]))),
                    flt.DataCell(flt.Text(str(buf[80][8]))), flt.DataCell(flt.Text(str(buf[81][8]))),
                    flt.DataCell(flt.Text(str(buf[82][8]))), flt.DataCell(flt.Text(str(buf[83][8]))),
                    flt.DataCell(flt.Text(str(buf[84][8]))), flt.DataCell(flt.Text(str(buf[85][8]))),
                    flt.DataCell(flt.Text(str(buf[86][8]))), flt.DataCell(flt.Text(str(buf[87][8]))),
                    flt.DataCell(flt.Text(str(buf[88][8]))), flt.DataCell(flt.Text(str(buf[89][8]))),
                    flt.DataCell(flt.Text(str(buf[90][8]))), flt.DataCell(flt.Text(str(buf[91][8]))),
                    flt.DataCell(flt.Text(str(buf[92][8]))), flt.DataCell(flt.Text(str(buf[93][8]))),
                    flt.DataCell(flt.Text(str(buf[94][8]))), flt.DataCell(flt.Text(str(buf[95][8]))),
                    flt.DataCell(flt.Text(str(buf[96][8]))), flt.DataCell(flt.Text(str(buf[97][8]))),
                    flt.DataCell(flt.Text(str(buf[98][8]))), flt.DataCell(flt.Text(str(buf[99][8]))),

                ],
            ),

        ],
    )

    scr.controls.append(dt)
    if(clr==0):
        info(page, cl, cache1, data, printer,cl1,checker,checker1,labels)
    elif(clr==1):
        labels.value="Memory cleared"

def info(page, cl, cache1, data, printer,cl1,checker,checker1,labels):
    global ot
    global rounder
    for i in range(100):
        if checker[i] == 0:
            dt.columns[i].visible = False
        else:
            dt.columns[i].visible = True

    for i in range(9):
        if checker1[i] == 0:
            dt.rows[i].visible = False
        else:
            dt.rows[i].visible = True

    if (rounder > 0):
        ot.visible = False
        page.remove(printer)
        ot = dt
    else:
        ot = dt
    if(cl1.value.isnumeric()):
        rounder = rounder + 1
        page.add(printer)
    page.update()


flt.app(target=myapp)
