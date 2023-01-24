import datetime
import process
import view

def log_cash(rezhim):
    if rezhim.lower() == 'импорт':
        sern = view.inp_import()
        res_search = process.search(sern)
        if isinstance(res_search, str):
            view.view_import_no()
        else:
            view.view_import(res_search)
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f'{rezhim} {res_search}. Время запроса: {str(datetime.datetime.now())} \n')
    elif rezhim.lower() == 'экспорт':
        result = view.inp_export()
        process.export(result)
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f'{rezhim} {result}. Время запроса: {str(datetime.datetime.now())} \n')
    