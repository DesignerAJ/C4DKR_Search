#-*- coding: utf-8 -*-
#
# C4D Korean User Group Q&A Search Plug-in (Ver.1.0) by AJ
# E-mail : narshe@naver.com

import os
import webbrowser
import c4d
from c4d import bitmaps, gui, plugins


PLUGIN_ID = 1059741


class C4DKUGSearchWindow(gui.GeDialog):

    def CreateLayout(self):

        self.SetTitle("C4D 한국유저그룹 Q&A 게시판 검색")
        self.GroupBegin(1000, c4d.BFH_SCALEFIT, 3, 1, groupflags=0)
        self.GroupBorderNoTitle(borderstyle=c4d.BORDER_NONE)
        self.GroupBorderSpace(5, 5, 5, 5)
        self.AddEditText(1001, c4d.BFH_SCALEFIT, 240, 20, editflags=c4d.EDITTEXT_HELPTEXT)
        self.SetString(1001, value="검색어를 입력하세요.", flags=c4d.EDITTEXT_HELPTEXT)
        self.AddButton(1002, c4d.BFH_RIGHT, 100, 20, "검색")
        self.GroupEnd()

        return True

    def Command(self, id, msg):

        if id == 1002:
            s_keyword = self.GetString(1001)

            if s_keyword == "":
                gui.MessageDialog("  검색어를 입력하세요!", type=c4d.GEMB_ICONASTERISK)
            else:
                print("'" + s_keyword + "'을/를 검색합니다.")
                c4dk_uri = "http://www.cinema4d.co.kr/?_filter=search&act=&vid=&mid=qna&category=&search_target=title_content&search_keyword="
                # s_keyword = s_keyword.decode('utf-8')
                webbrowser.open(c4dk_uri + s_keyword, new=0, autoraise=True)

        return True



class C4DKUGSearchData(plugins.CommandData):

    dialog = None

    def Execute(self, doc):
        if self.dialog is None: self.dialog = C4DKUGSearchWindow()
        return self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=PLUGIN_ID, defaultw=350, defaulth=200)

    def RestoreLayout(self, sec_ref):
        if self.dialog is None: self.dialog = C4DKUGSearchWindow()
        return self.dialog.Restore(pluginid=PLUGIN_ID, secret=sec_ref)



if __name__=='__main__':

    pluginstr = "KUG Q&A Search"
    bmp = bitmaps.BaseBitmap()
    dir, f = os.path.split(__file__)
    fn = os.path.join(dir, "res", "KUG_Search.png")
    bmp.InitWith(fn)

    ex = plugins.RegisterCommandPlugin(id=PLUGIN_ID,
                                        str=pluginstr,
                                        info=0,
                                        icon=bmp,
                                        help="C4D 한국유저그룹 Q&A 게시판 검색",
                                        dat=C4DKUGSearchData())

    if (ex):
        print(pluginstr + " 초기화 완료.")
    else: print(pluginstr + " 초기화 에러.")