import view
import process

def button_click():
    rezhim = view.inp_mod()
    if rezhim.lower() == 'импорт':
        sern = view.inp_import()
        res_search = process.search(sern)
        # print(res_search)
        if isinstance(res_search, str):
            view.view_import_no()
        else:
            view.view_import(res_search)
    elif rezhim.lower() == 'экспорт':
        result = view.inp_export()
        process.export(result)
            
        

    


    