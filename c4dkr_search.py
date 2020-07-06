#-*- coding: utf-8 -*-

import c4d
import webbrowser
from c4d import gui


class C4DK_Search_Window(gui.GeDialog):

    def CreateLayout(self):

        self.SetTitle("C4D 한국유저그룹 Q&A 검색")
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
                s_keyword = s_keyword.decode('utf-8')
                webbrowser.open(c4dk_uri + s_keyword, new=0, autoraise=True)

        return True

    def DestroyWindow(self):

        print("C4D 한국유저그룹 Q&A 검색 - 스크립트 종료")



if __name__=='__main__':

    c4dKwindow = C4DK_Search_Window()
    c4dKwindow.Open(dlgtype=c4d.DLG_TYPE_ASYNC, xpos=-2, ypos=-2, defaultw=400)

    c4d.EventAdd()
