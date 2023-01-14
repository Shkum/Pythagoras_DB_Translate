from GoogleTranslate import GoogleTranslate
from functions import split_text
from database import *

# get all info from DB
select_all_query = db.select([general_info])
select_all_result = connection.execute(select_all_query)
db_info = select_all_result.fetchall()

# translate rus_info and record to db
for i in range(len(db_info)):
    txt = db_info[i]['info_ru']
    txt_list = split_text(txt, 2000)
    res_EN = ''
    res_DE = ''
    res_UA = ''
    res_RU = ''
    # due to google translate only short text - split out text and translate part by part
    for txt_part in txt_list:
        t = GoogleTranslate(txt_part)
        res_EN += t.get_translated(t.langRU, t.langEN)
        res_DE += t.get_translated(t.langRU, t.langDE)
        res_UA += t.get_translated(t.langRU, t.langUA)
        res_RU += t.get_translated(t.langRU, t.langRU)
    update_query = \
        db.update(general_info).where(general_info.columns.name == db_info[i]['name']). \
            values(info_en=res_EN). \
            values(info_de=res_DE). \
            values(info_ua=res_UA). \
            values(info_ru=res_RU)
    connection.execute(update_query)
    print(f"{db_info[i]['name']} - done ...")
connection.close()

