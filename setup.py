import cx_Freeze
import sys
base=None

if sys.platform=='win32':
    base="Win32GUI"
    
shortcut_table = [
    ("DesktopShortcut",         
     "DesktopFolder",           
     "TheHungryPython",                 
     "TARGETDIR",               
     "[TARGETDIR]TheHungryPython.exe",  
     None,                      
     None,                      
     None,                      
     None,                      
     None,                      
     None,                      
     'TARGETDIR'                
     )
    ]

options = {
    'bdist_msi': {
        'data': {"Shortcut": shortcut_table},
    },
    "build_exe":{"packages":["pygame","time","random","main","score","helpg","os"],
                          "include_files":["score.txt","cursor.png","pic1.png"]},
}

cx_Freeze.setup(
    
    name="TheHungryPython",
    options=options,
    executables=[cx_Freeze.Executable("TheHungryPython.py",base=base,shortcutName="TheHungryPython",shortcutDir="DesktopFolder")]
    )
