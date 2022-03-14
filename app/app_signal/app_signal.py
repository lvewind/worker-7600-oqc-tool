from PyQt5.QtCore import QObject, pyqtSignal


class SignalData(QObject):
    add_item = pyqtSignal(dict)


class SignalDialog(QObject):
    pass


class SignalLoadTable(QObject):
    load_products_list = pyqtSignal()
    find_sn_in_products_list = pyqtSignal(str)


class SignalMainUI(QObject):
    refresh_text_browser = pyqtSignal(str)
    refresh_text_browser_ping_100 = pyqtSignal(str)
    refresh_text_browser_ping_254 = pyqtSignal(str)
    refresh_eth = pyqtSignal()
    run_iperf3 = pyqtSignal()
    set_has_output = pyqtSignal()
    check_iot_again = pyqtSignal()
    iperf_all = pyqtSignal()
    show_message = pyqtSignal(str)
    show_input_dialog = pyqtSignal()
    save_bridge_ip = pyqtSignal(str)


class CloseSelf(QObject):
    close_self = pyqtSignal(str)


signal_data = SignalData()
signal_dialog = SignalDialog()
signal_load_table = SignalLoadTable()
signal_main_ui = SignalMainUI()
close_self = CloseSelf()

