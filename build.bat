pyinstaller main.py ^
    --onefile ^
    --clean ^
    --windowed --noconsole ^
    --hidden-import "clr" --name "Svelte" ^
    --icon "icon.ico" ^
    --paths "E:\PYTHON\pywebview\env\Scripts/" ^
    --add-data "assets;assets" ^
    --add-data "E:\PYTHON\pywebview\env\Lib\site-packages\webview\lib\WebBrowserInterop.x64.dll;./" ^
    --add-data "E:\PYTHON\pywebview\env\Lib\site-packages\webview\lib\WebBrowserInterop.x86.dll;./" ^
    --add-data "E:\PYTHON\pywebview\env\Lib\site-packages\webview\lib\Microsoft.Toolkit.Forms.UI.Controls.WebView.dll;./" ^
    --exclude-module "tkinter" ^
    --exclude-module "pyinstaller"

rm -rf build/
rm -rf Svelte.spec
rm -rf __pycache__

