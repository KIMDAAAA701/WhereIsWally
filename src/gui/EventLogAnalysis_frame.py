# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
import pandas as pd
import subprocess
# from pprint import pprint
# from src.gui.GUI_Main import mainPage

def connectmain():
    global count
    count += 1

file_name = ""
def getdir(data):
    #def __init__(self,data):
    # global sysdir
    # sysdir.append(data)
    # print("함수안의 sysdir")
    # print(sysdir)
    # for i in range(len(sysdir)):
    #     print(sysdir[i])"
    global file_name
    print("getdir실행")
    file_name = data
    return file_name

#PS 데이터
def fileopen(filename):
    print(filename)
    print("으로 filename실행")
    f = open(".\detected\\" + filename + "\\ps.json", 'r')
    file = json.load(f)
    data = list(file)
    P0_Image = [[], [], []];
    P0_Pid = [[], [], []];
    action = [[], [], []];
    type = [[], [], []]
    level = [[], [], []]
    Time = [[], [], []];
    PName = [[], [], []]
    dd_check = ""
    #f2 = open(".\detected\\" + filename + "\\ps.json", 'r')
    for i in range(len(data)):
        P0_Image[i].append((data[i]['0'][0]['Image']))
        P0_Pid[i].append((data[i]['0'][0]['Pid']))
        level[i].append(0)
        Time[i].append((data[i]['0'][0]['Time']))
        PName[i].append((data[i]['0'][0]['Process Name']))
        try:
            for j in range(len(data[i]['0'][0]['1'][0])):
                P0_Image[i].append((data[i]['0'][0]['1'][j]['Image']))
                P0_Pid[i].append((data[i]['0'][0]['1'][j]['Pid']))
                level[i].append(1)
                Time[i].append((data[i]['0'][0]['1'][j]['Time']))
                PName[i].append((data[i]['0'][0]['1'][j]['Process Name']))
                # action[i].append(data[i]['0'][0]['action'][j]['Image'])
                # type[i].append(data[i]['0'][0]['action'][j]['Type'])
                try:
                    for k in range(len(data[i]['0'][0]['1'][j])):
                        P0_Image[i].append((data[i]['0'][0]['1'][j]['2'][k]['Image']))
                        P0_Pid[i].append((data[i]['0'][0]['1'][j]['2'][k]['Pid']))
                        level[i].append(2)
                        Time[i].append((data[i]['0'][0]['1'][j]['2'][k]['Time']))
                        PName[i].append((data[i]['0'][0]['1'][j]['2'][k]['Process Name']))
                        # print(data[i]['0'][0]['action'][j]['Image'])
                        # action[i].append(data[i]['0'][0]['action'][j]['Image'])
                        # type[i].append(data[i]['0'][0]['action'][j]['Type'])
                        try:
                            for p in range(len(data[i]['0'][0]['1'][j]['2'][k])):  # depth3
                                P0_Image[i].append((data[i]['0'][0]['1'][j]['2'][k]['3'][p]['Image']))
                                P0_Pid[i].append((data[i]['0'][0]['1'][j]['2'][k]['3'][p]['Pid']))
                                level[i].append(3)
                                Time[i].append((data[i]['0'][0]['1'][j]['2'][k]['3'][p]['Time']))
                                PName[i].append((data[i]['0'][0]['1'][j]['2'][k]['3'][p]['Process Name']))
                        except:
                            pass
                except:
                    pass
        except:
            pass
    # print(data[1]['0'][0]['1'][0]['Image'])
    # print(level)
    # print(P0_Image)
    # print(P0_Pid)
    # with open(".\detected\\2020-11-11 16.48.36.489000\\ps.json", 'r') as f:
    #     print("open함수 내의 sysdir")
    #     print(sysdir)
    #     file = json.load(f)
    #     data = list(file)
    #     P0_Image = [[],[],[]];    P0_Pid = [[],[],[]];  action = [[],[],[]];    type = [[],[],[]]
    #     level = [[],[],[]]
    #     dd_check = ""
    #     with open(".\detected\\2020-11-11 16.48.36.489000\\detectedProcess.json", 'r') as f:
    #         for i in range(len(data)):
    #             P0_Image[i].append((data[i]['0'][0]['Image']))
    #             P0_Pid[i].append((data[i]['0'][0]['Pid']))
    #             dd = data[i]['0'][0]['Image']
    #             level[i].append(0)
    #             try:
    #                 for j in range(len(data[i]['0'][0]['1'][0])):
    #                     P0_Image[i].append((data[i]['0'][0]['1'][j]['Image']))
    #                     P0_Pid[i].append((data[i]['0'][0]['1'][j]['Pid']))
    #                     level[i].append(1)
    #                     action[i].append(data[i]['0'][0]['action'][j]['Image'])
    #                     type[i].append(data[i]['0'][0]['action'][j]['Type'])
    #                     try:
    #                         for k in range(len(data[i]['0'][0]['1'][j])):
    #                             P0_Image[i].append((data[i]['0'][0]['1'][j]['2'][k]['Image']))
    #                             P0_Pid[i].append((data[i]['0'][0]['1'][j]['2'][k]['Pid']))
    #                             level[i].append(2)
    #                             # print(data[i]['0'][0]['action'][j]['Image'])
    #                             # action[i].append(data[i]['0'][0]['action'][j]['Image'])
    #                             # type[i].append(data[i]['0'][0]['action'][j]['Type'])
    #                             try:
    #                                 for p in range(len(data[i]['0'][0]['1'][j]['2'][k])):  # depth3
    #                                     P0_Image[i].append((data[i]['0'][0]['1'][j]['2'][k]['3'][p]['Image']))
    #                                     P0_Pid[i].append((data[i]['0'][0]['1'][j]['2'][k]['3'][p]['Pid']))
    #                                     level[i].append(3)
    #                             except:
    #                                 pass
    #                     except:
    #                         pass
    #             except:
    #                 pass
    #     #print(data[1]['0'][0]['1'][0]['Image'])
    #     #print(level)
    #     #print(P0_Image)
    #     #print(P0_Pid)

    detected = [[], []]
    with open(".\detected\\" + file_name + "\\detectedProcess.json")as json_file:
        detected_data = json.load(json_file)
        for detect in detected_data:
            detected[0].append(detect['ActionIndex']) # deteted 된 PID 넘버
            detected[1].append(detect['RuleId'])  # detected 된 RuleID

    Ruledata = [[], []]
    with open("..\\core\\Sysmon\\Rule\\EventId.json", "r", encoding="utf-8")as json_file:
        rule_data = json.load(json_file)
        for ruleid in rule_data:
            Ruledata[0].append(ruleid['RuleId'])
            Ruledata[1].append(ruleid['RuleName'])
    print(P0_Pid)
    print(P0_Image)
    print("fileopen 끝")
    return P0_Image, P0_Pid, action, type, level, detected,Ruledata, data, Time, PName

#액션 데이터
def openaction():
    # 액션
    # Taction : 트리 몇 레벨에 action이 있는지
    Taction0 = [[], [], []]; Taction1 = [[], [], []]; Taction2 = [[], [], []]; Taction3 = [[], [], []]
    Iaction0 = [[], [], []]; Iaction1 = [[], [], []]; Iaction2 = [[], [], []]; Iaction3 = [[], [], []]
    Alevel = [[], [], []]
    with open(".\detected\\" + file_name + "\\detectedAction.json", 'r') as f:
        file = json.load(f)
        data = list(file)
        for i in range(len(data)):
            try:
                for j in range(len(data[i]['0'][0]['action'])):  # 0번액션
                    Taction0[i].append(data[i]['0'][0]['action'][j]['Type'])
                    Iaction0[i].append(data[i]['0'][0]['action'][j]['Image'])
                    Alevel[i].append(0)
                try:
                    for k in range(len(data[i]['0'][0]['1'][0]['action'])):  # 1번액션
                        Taction1[i].append(data[i]['0'][0]['1'][0]['action'][k]["Type"])
                        Iaction1[i].append(data[i]['0'][0]['1'][0]['action'][k]["Image"])
                        Alevel[i].append(1)
                    try:
                        for l in range(len(data[i]['0'][0]['1'][0]['2'])):  # 2번액션
                            Taction2[i].append(data[i]['0'][0]['1'][0]['2'][0]["action"][0]['Type'])
                            Iaction2[i].append(data[i]['0'][0]['1'][0]['2'][0]["action"][0]['Image'])
                            Alevel[i].append(2)
                        try:
                            for t in range(len(data[i]['0'][0]['1'][0]['2'])):  # 3번액션
                                Taction3[i].append(data[i]['0'][0]['1'][0]['2'][0]["3"][0]['action'][0]['Type'])
                                Iaction3[i].append(data[i]['0'][0]['1'][0]['2'][0]["3"][0]['action'][0]['Image'])
                                Alevel[i].append(3)
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
    # print("Taction 출력")
    # print(Taction0)
    # print(Taction1)
    # print(Taction2)
    # print(Taction3)
    # print(Taction0[0])
    # print(Taction0[0][0])
    return Taction0, Taction1, Taction2, Taction3, Iaction0, Iaction1, Iaction2, Iaction3, Alevel

class StWidgetForm(QGroupBox):
    """
    위젯 베이스 클래스
    """

    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.box)

class Sysmon_graph(StWidgetForm):
    # main의 그래프 창에 띄울거 작성
    def __init__(self):
        super(Sysmon_graph, self).__init__()
        self.setStyleSheet("border: 0px")
        self.initUI()

    def initUI(self):
        self.fig = plt.Figure()
        # self.setMaximumHeight(370)
        self.fig.clear()
        filename = getdir(file_name)
        name = []
        count = []
        with open(".\detected\\"+filename+"\\graph.json")as json_file:
            json_data = json.load(json_file)
            for data in json_data:
                name.append(data['name'][11:19])
                count.append(data['count'])

        # detectedProcess.json pid 뽑아오기
        # RuleId = []
        # pid = []
        # with open("..\\core\\Sysmon\\detected\\2020-11-11 16.48.36.489000_detectedProcess.json")as json_file:
        #     detected_data = json.load(json_file)
        #     for detect in detected_data:
        #         RuleId.append(detect['RuleId'])
        #         pid.append(detect['pid'])
        # print(RuleId) #확인
        # print(pid) #확인

        # 2020-11-11 16.48.36.489000_ps.json pid 뽑아오기
        # if __name__ == '__main__':

        ind = np.arange(len(name))
        width = 0.35

        ax = self.fig.add_subplot(111)
        ax.bar(ind, count, width)
        ax.set_xticks(ind + width / 20)
        # ax.set_xticklabels(rotation=45)
        ax.set_xticklabels(name, rotation=70)
        # ax.legend()

        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        # self.canvas.setMaximumHeight(370)
        self.box.addWidget(self.canvas)

class Model(QStandardItemModel):
    """
    사용자 데이터 모델 설정
    [{"type":str, "objects":[str, ...]}, ...]
    위의 데이터 형식을 이용하여 서브 아이템을 가지는 모델을 생성
    """
    def __init__(self, data):
        QStandardItemModel.__init__(self)

        d = data[0]  # Fruit
        item = QStandardItem(d["type"])
        child = QStandardItem(d["objects"][0])  # Apple
        item.appendRow(child)
        child = QStandardItem(d["objects"][1])  # Banana
        item.appendRow(child)
        self.setItem(0, 0, item)

        # for 문을 이용해서 작성했을 경우
        # for j, _type in enumerate(data):
        #    item = QStandardItem(_type["type"])
        #    for obj in _type["objects"]:
        #       child = QStandardItem(obj)
        #       item.appendRow(child)
        #    self.setItem(j, 0, item)

class Tree(StWidgetForm):
    def __init__(self,num):
        self.num = num
        super(Tree, self).__init__()
        self.setStyleSheet("border: 0px")
        self.initUI()

    def initUI(self):
        self.tfunction()

    def tfunction(self):
        QTW = QTreeWidget()
        QTW.setAlternatingRowColors(True)
        QTW.header().setVisible(False)
        itemA = QTreeWidgetItem(QTW)
        Taction0, Taction1, Taction2, Taction3, Iaction0, Iaction1, Iaction2, Iaction3, Alevel = openaction()
        P0_Image, P0_Pid, action, type, level, detected,Ruledata, data, Time, PName = fileopen(file_name)
        for k in range(len(level[self.num])):
            if level[self.num][k] == 0:
                itemA.setText(0, P0_Image[self.num][k])
                if P0_Pid[self.num][k] in detected[0]:
                   itemA.setForeground(0, QBrush(QColor("red")))
            elif level[self.num][k] == 1:
                itemB = QTreeWidgetItem(itemA)
                itemB.setText(0, P0_Image[self.num][k])
                if P0_Pid[self.num][k] in detected[0]:
                   itemB.setForeground(0, QBrush(QColor("red")))
            elif level[self.num][k] == 2:
                itemC = QTreeWidgetItem(itemB)
                itemC.setText(0, P0_Image[self.num][k])
                if P0_Pid[self.num][k] in detected[0]:
                   itemC.setForeground(0, QBrush(QColor("red")))
            elif level[self.num][k] == 3:
                itemD = QTreeWidgetItem(itemC)
                itemD.setText(0, P0_Image[self.num][k])
                if P0_Pid[self.num][k] in detected[0]:
                   itemD.setForeground(0, QBrush(QColor("red")))

        """
        for i in range(len(Taction0)):
            print(i)
            for k in range(len(Taction0[i])):
                print(k)
                print("======")
                print(Taction0[i][k])
                itemB = QTreeWidgetItem(itemA)
                itemB.setText(0, "[action]" + Taction0[i][k])
        """

        self.box.addWidget(QTW, alignment=Qt.AlignVCenter)

class Root1_tree(StWidgetForm):
    def __init__(self):
        super(Root1_tree, self).__init__()
        self.setStyleSheet("border: 0px")
        self.initUI()

    def initUI(self):
        layout_main = QVBoxLayout()
        self.box.addLayout(layout_main)
        layout_main.addWidget(Tree(0))
        layout_main.addWidget(Tree(1))
        layout_main.addWidget(Tree(2))
        # self.resize(self.sizeHint().width(), self.minimumHeight())  #이건뭐지?? 알아보기 -> 지워도 될 듯?

class Sysmon_tree(StWidgetForm):
    # main의 tree구조 창에 띄울거 작성
    def __init__(self):
        super(Sysmon_tree, self).__init__()
        self.initUI()

    def initUI(self):
        layout_main = QVBoxLayout()
        self.box.addLayout(layout_main)
        self.setStyleSheet("background-color: #FFFFF;")
        self.setStyleSheet("border: 10px")


        tabs = QTabWidget()
        tabs.addTab(Root1_tree(), 'tree')
        tabs.setMinimumHeight(500)
        tabs.setMinimumWidth(546)
        tabs.setMaximumHeight(500)
        tabs.setMaximumWidth(546)
        scrollarea = QScrollArea()
        scrollarea.setWidget(tabs)
        layout_main.addWidget(scrollarea)

class Root(StWidgetForm):
    def __init__(self,num):
        self.num = num
        super(Root, self).__init__()
        self.initUI()

    def initUI(self):
        self.function()
        # layout_main = QVBoxLayout() 이거 잘 기억이 안남
        # self.box.addLayout(layout_main)

    def function(self):
        List = ["PID", "Process Name", "Time", "Path", "Rulename"]
        P0_Image, P0_Pid, action, type, level, detected, Ruledata, data, Time, PName = fileopen(file_name)
        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(List)

        table.setColumnWidth(0, 80)
        table.setColumnWidth(1, 130)
        table.setColumnWidth(2, 220)
        table.setColumnWidth(3, 470)
        table.setColumnWidth(4, 230)
        table.setRowCount(len(P0_Image[self.num]))

        for i in range(len(P0_Image[self.num])):
            table.setItem(i, 3, QTableWidgetItem(str(P0_Image[self.num][i])))
            table.setItem(i, 2, QTableWidgetItem(str(Time[self.num][i])))
            table.setItem(i, 1, QTableWidgetItem(str(PName[self.num][i])))
            i = i + 1

        for i in range(len(P0_Pid[self.num])):
            table.setItem(i, 0, QTableWidgetItem(str(P0_Pid[self.num][i])))
            tabledata = []
            tabledata.append(str(P0_Pid[self.num][i]))
            for k in range(len(tabledata)):
                for p in range(len(detected[0])):
                    if int(tabledata[k]) == int(detected[0][p]):  # 액션 인덱스
                        for j in range(len(Ruledata[0])):
                            if detected[1][p] == Ruledata[0][j]:
                                table.setItem(i, 4, QTableWidgetItem(str(Ruledata[1][j])))
            i = i + 1

            #for k in range(len(tabledata)):
            #    print("k")
            #    print(k)
            """
            for p in range(len(detected[0])):
                pirnt("p")
                print(p)
                if int(tabledata) == int(detected[0][p]):
                    for j in range(len(Ruledata[0])):
                        print("j")
                        print(j)
                        if detected[1][p] == Ruledata[0][j]:
                            print("같음")
                            table.setItem(i, 3, QTableWidgetItem(str(Ruledata[1][j])))
                p += 1
            """

        table.setMinimumHeight(500)
        table.setMinimumWidth(800)
        table.setMaximumHeight(500)
        table.setMaximumWidth(800)

        self.box.addWidget(table, alignment=Qt.AlignVCenter | Qt.AlignVCenter)

class Root1(StWidgetForm):
    def __init__(self):
        super(Root1, self).__init__()
        self.setStyleSheet("border: 0px")
        self.initUI()

    def initUI(self):
        layout_main = QVBoxLayout()
        self.box.addLayout(layout_main)
        layout_main.addWidget(Root(0))

class Root2(StWidgetForm):
    def __init__(self):
        super(Root2, self).__init__()
        self.setStyleSheet("border: 0px")  # 지우는거 고려
        self.initUI()

    def initUI(self):
        layout_main = QVBoxLayout()
        self.box.addLayout(layout_main)
        layout_main.addWidget(Root(1))

class Root3(StWidgetForm):
    def __init__(self):
        super(Root3, self).__init__()
        self.setStyleSheet("border: 0px")  # 지우는거 고려
        self.initUI()

    def initUI(self):
        layout_main = QVBoxLayout()
        self.box.addLayout(layout_main)
        layout_main.addWidget(Root(2))

class Sysmon_table(StWidgetForm):
    def __init__(self):
        super(Sysmon_table, self).__init__()
        self.initUI()
        # self.setStyleSheet("background-color: #AAAAAA")

    def initUI(self):
        List = ["PID", "Process Name", "Type", "Rule Name"]
        P0_Image, P0_Pid, action, type, level, detected, Ruledata, data, Time, PName = fileopen(file_name)
        layout_main = QHBoxLayout()
        self.box.addLayout(layout_main)
        self.setStyleSheet("border: 10px")

        tabs = QTabWidget()
        tabs.setStyleSheet("background-color: #FFFFFF")
        tabs.addTab(Root1(), data[0]['0'][0]['Image'])
        tabs.addTab(Root2(), data[1]['0'][0]['Image'])
        tabs.addTab(Root3(), data[2]['0'][0]['Image'])

        #추가한 것
        scrollarea = QScrollArea()
        scrollarea.setWidget(tabs)
        layout_main.addWidget(scrollarea)

        # layout_main.addWidget(tabs)

class Sysmon_under(StWidgetForm):       #여기가 gui 실행하는 곳..? 그럼 다른 함수에서 띄울 필요가 없다
    def __init__(self):
        super(Sysmon_under, self).__init__()
        self.initUI()
        # self.setStyleSheet("background-color: #AAAAAA") 흙흙

    def initUI(self):
        layout_main = QHBoxLayout()
        self.box.addLayout(layout_main)
        self.setStyleSheet("border: 0px")

        sysgraph = Sysmon_tree()
        layout_main.addWidget(sysgraph)
        # sysgraph.setMinimumWidth(600)

        systable = Sysmon_table()
        layout_main.addWidget(systable)

        # 크기
        systable.setMinimumWidth(900)
        systable.setMinimumHeight(545)      #여기가 테이블 큰틀
        systable.setMaximumHeight(545)
        systable.setMaximumWidth(900)
        # systable.setMaximumHeight(100)

class Sys_main(StWidgetForm):
    def __init__(self):
        super(Sys_main, self).__init__()
        # self.setTitle("SYSMON")
        self.setStyleSheet("background-color: white")
        # self.setGeometry(150, 120, 1400, 800) 일단 지워본다
        # self.setStyleSheet("border: 0px")
        self.initUI()
        print("Sysmain")
        print(file_name)


    def initUI(self):
        # 상단바, 기존 화면 레이아웃 생성 및 추가
        layout_bar = QHBoxLayout()
        layout_main = QVBoxLayout()
        layout_top = QHBoxLayout()
        layout_bottom = QHBoxLayout()
        self.box.addLayout(layout_bar)
        self.box.addLayout(layout_main)
        layout_main.addLayout(layout_top)
        layout_main.addLayout(layout_bottom)
        layout_main.addLayout(layout_bar)

        # 상단 이전 버튼 생성 및 부착
        label1 = QPushButton('탐지 시간 : '+ file_name)
        label1.setFont(QFont('나눔고딕', 12, QFont.Bold))
        label1.setMinimumWidth(400)
        label1.setMinimumHeight(50)
        label1.setMaximumWidth(400)
        label1.setMaximumHeight(50)
        label1.setStyleSheet(
            "border-width: 1px;"
            "border-color: #000000;"
            "border-radius: 3px")
        layout_bar.addWidget(label1, alignment=Qt.AlignLeft)

        # 그래프, 트리 출력 창 부착
        graphwid = Sysmon_graph()
        graphwid.setMinimumHeight(300)
        graphwid.setMinimumHeight(300)
        layout_top.addWidget(graphwid)

        treewid = Sysmon_under()
        treewid.setMinimumHeight(570)
        treewid.setMaximumHeight(570)
        layout_bottom.addWidget(treewid)


class MyApp(QMainWindow, QWidget):
    # 크기 및 출력 위치를 변경
    def __init__(self):
        super().__init__()
        self.stk_w = QStackedWidget(self)
        self.setGeometry(150, 120, 1400, 800)
        self.initUI()

    def initUI(self):
        # 레이아웃 시작

        # 레이아웃 생성
        wid = QWidget(self)
        self.setCentralWidget(wid)
        layout1 = QVBoxLayout()

        # AMSI 메인 창 부착
        layout1.addWidget(Sys_main())

        wid.setLayout(layout1)
        layout1.addWidget(Sysmon_graph())
        self.setWindowTitle('Find Wally')
        self.show()


if __name__ == '__main__':  # 큐티파이는 반드시 어플리케이션 오브젝트을 생성해야만 함.
    app = QApplication(sys.argv)  # sys.argv는 파이썬으로 쉘 스크립트
    ex = MyApp()  # 내가 만든 창에 넣을 객체 생성
    sys.exit(app.exec_())  # 이벤트 처리를 위한 메인 루프 실행, 메인루프가 끝날때 exit가 실행됨.