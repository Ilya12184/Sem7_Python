import view
import process
import log

def buttom_click():
    mode = view.inp_mod()
    if mode.lower() == 'импорт':
        surn = view.inp_import()
        result = process.search(surn)
        if isinstance(result, str):
            view.view_import_no()
        else:
            view.view_import(result)
    elif mode.lower() == 'экспорт':
        result = view.inp_export()
        process.export(result)
        view.view_data(result)
        log.log_cash(result)