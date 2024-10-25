from  MainWindow import Ui_MainWindow
from PySide6.QtWidgets import (
    QApplication, QMainWindow,QLabel, QFrame,QVBoxLayout,QHBoxLayout,QTableWidgetItem,
    QCheckBox,QListWidgetItem,QMessageBox,QHeaderView,
    QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget
)
from PySide6.QtCore import QSize, Slot,Qt
import json
import os
import sys
import webbrowser

# 如下是日志配置
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(handler)
logger.addHandler(console)




exe_dir = os.path.dirname(os.path.realpath(__file__))
if 'python.exe' not in  sys.argv[0]:
    exe_dir = os.path.dirname(os.path.realpath(sys.argv[0]))



# 这里先导入数据
json_path = os.path.join(
     exe_dir,  # 这个脚本所在的目录
	'英雄联盟英雄列表.json')                      # 文件名  
hero_settings = None                              # 所有英雄的信息
with open(json_path, 'r', encoding='utf-8') as f:
    hero_settings=json.load(f)                    # 从文件中读取所有英雄的信息
# 我用数据生成表格标题的原因是，为了以后不修改代码，只修改json就可以了。
HERO_TYPES = list(set([j for i in hero_settings['英雄列表'] for j in hero_settings['英雄列表'][i]['类型']]))   # 英雄的类型
HERO_WAYS = ['上单','中路', '下路', '打野', '辅助']       # 英雄的路线
HERO_NAMES = [i for i in hero_settings['英雄列表']]      # 英雄的名称
HERO_CHECKED = [False for _ in range(len(HERO_NAMES))]  # 这个英雄是否被选择
HERO_SELECTED_COUNT_MAX = 5                             # 最多选择5个英雄
FORE_COLOR = hero_settings['颜色列表']['前景色']         # 前景色
BACK_COLOR = hero_settings['颜色列表']['背景色']         # 背景色





class MyMainWindow(QMainWindow, Ui_MainWindow):
    # 逻辑和界面的分离，这个类里是一堆的逻辑

    def initTblHeros(self):
        # 设置表格，
        self.tblHeros.setRowCount(len(HERO_WAYS))      # 行是路线
        self.tblHeros.setColumnCount(len(HERO_TYPES))  # 列是类型
        self.tblHeros.setHorizontalHeaderLabels(HERO_TYPES)
        self.tblHeros.setVerticalHeaderLabels(HERO_WAYS)
        # 列宽平均,行宽也平均
        self.tblHeros.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tblHeros.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    def initLstHeros(self):
        # 设置列表框，添加英雄，然后添加复选框的
        # 请注意，这里是搜索了英雄的
        _hero_search = self.txtHeroSearch.text()
        _hero_names = [i for i in HERO_NAMES if len(_hero_search) == 0 or _hero_search in i]
        self.lstHeros.clear() # 清空所有的英雄
        for _hero_name in _hero_names:
            box = QCheckBox(_hero_name) # 添加一个选择框
            # 需要看看有哪些选择了。
            _index = HERO_NAMES.index(_hero_name)
            box.setChecked(HERO_CHECKED[_index])
            # 这个选择框点击事件需要添加槽函数，作用是更新HERO_CHECKED，每次点击都会更新右边的
            box.stateChanged.connect(self.hero_checked)
            item = QListWidgetItem()    # 一个item
            self.lstHeros.addItem(item) # 添加到列表框
            self.lstHeros.setItemWidget(item, box) # 把这个选择框加入到item

    def hero_checked(self, state):
        # 英雄选择事件，这里会查询所有的状态
        _hero_name = self.sender().text()       # 取得英雄的名称
        _index = HERO_NAMES.index(_hero_name)   # 下标
        # 根据状态更新
        if state == Qt.CheckState.Checked.value:
            HERO_CHECKED[_index] = True
        elif state == Qt.CheckState.Unchecked.value:
            HERO_CHECKED[_index] = False
        # 更新后，重新绘制一下表格
        self.updateTblHeros()

        pass

    def updateTblHeros(self):
        # 更新表格
        # 清空原先的数据
        self.tblHeros.clearContents()  # 清空所有的内容
        # 先取得有哪些英雄被选中了
        _hero_selected = [HERO_NAMES[i] for i in range(len(HERO_NAMES)) if HERO_CHECKED[i]]
        logger.info(f'被选中的英雄:{_hero_selected}')
        # 判断影星是否超过5个
        if len(_hero_selected) > HERO_SELECTED_COUNT_MAX:
            _hero_selected = _hero_selected[-HERO_SELECTED_COUNT_MAX:]
            QMessageBox.warning(self, '警告', '选择的英雄数量大于5个,只处理最后的5个', QMessageBox.Yes, QMessageBox.Yes)
        # 这里遍历每一个英雄
        i = 0
        for _hero in _hero_selected:
            # 先找到英雄的类目
            _hero_info = hero_settings['英雄列表'][_hero]
            # 然后找到下标
            _type_index_s = [HERO_TYPES.index(i) for i in _hero_info['类型']]
            _way_index_s = [HERO_WAYS.index(i) for i in HERO_WAYS if i in _hero_info['路']]
            for _type_index in _type_index_s:
                for _way_index in _way_index_s:
                    # 这里要判断这个里边是否已经有控件了
                    _widget = self.tblHeros.cellWidget(_way_index, _type_index)
                    if _widget is None:
                        # 如果是None，表示原先没有控件，需要添加
                        _widget = QWidget()         # 创建控件
                        _layout = QVBoxLayout()     # 这个控件的布局 
                        _widget.setLayout(_layout)  # 设置布局
                        self.tblHeros.setCellWidget(_way_index, _type_index, _widget)
                    else:
                        _layout = _widget.layout()  # 取得布局
                    # 布局中添加标签
                    # 创建这个英雄的标签
                    _label = QLabel(_hero)
                    # 设置样式表，
                    _label.setStyleSheet(f'QLabel{{color:{FORE_COLOR[i]};background-color:{BACK_COLOR[i]}}}')
                    _layout.addWidget(_label)
            i += 1


    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.initTblHeros()  # 设置表格的行和列
        self.initLstHeros()  # 设置选择英雄的选择框

    @Slot()
    def linkMyShop(self):
        # 打开我的淘宝店铺
        logger.info('打开我的淘宝店')
        webbrowser.open_new_tab('http://xinyiya.taobao.com')

    @Slot()
    def cancelAllSelected(self):
        # 取消全选，
        for i in range(len(HERO_NAMES)):
            self.lstHeros.itemWidget(self.lstHeros.item(i)).setChecked(False)

    @Slot()
    def heroSearchChanged(self):
        # 搜索的英雄更改文本事件
        self.initLstHeros() # 调用重新初始化的


def custom_exception_handler(type, value, traceback):
    # 处理异常的逻辑
    logger.error('异常处理')
    logger.error(type)
    logger.error(value)
    logger.error(traceback)


sys.excepthook = custom_exception_handler


# 主程序
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    my_form = MyMainWindow()
    # my_form.setWindowTitle('my_form')
    my_form.show()
    sys.exit(app.exec())