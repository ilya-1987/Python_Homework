import view
import process
import log

def button_click():
    rezhim = view.inp_mod()
    if rezhim.lower() == 'импорт':
        sern = view.inp_import()
        res_search = process.search(sern)
        #if not res_search:
            #view.view_import_no()
        #else:
        view.view_import(res_search)
    
    elif rezhim.lower() == 'экспорт':
        result = view.inp_export()
        process.export(result)
    log.log_cash(rezhim)
            
        

    


    