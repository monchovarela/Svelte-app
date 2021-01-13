#!/usr/bin/python3
import sys, os, json
import threading
import webview
import time

frozen = 'not'
if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

window = {}

class Api:

    # debug info
    def debug(self, content):
        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)
        print('------- Debug Python {} --------'.format(time_string))
        print(content)
        print('--------------------------------------')

    # close app
    def close(self, params):
        window.destroy()

    # init
    def init(self, params):
        response = {
            'status': 'Ready'
        }
        return {'data': response}


# - States
# ----------------

# The app is shown
def on_shown():
    print('App is shown')

# the app is closing
def on_closing():
    print('App is closing')

# the app is closed
def on_closed():
    print('App is closing')


if __name__ == '__main__':

    # use api class
    api = Api()

    # create window
    window = webview.create_window(
        'Svelte app',
        'assets/index.html',
        js_api=api,
        width=500,
        height=400,
        resizable=False,
        min_size=(500, 400),
        text_select=True,
        confirm_close=True,
        frameless=True,
        easy_drag=False,
    )
    # states
    window.closed += on_closed
    window.closing += on_closing
    window.shown += on_shown

    # start
    webview.start(http_server=True)
