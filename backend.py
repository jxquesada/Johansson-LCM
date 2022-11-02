def loadSettings():
        Settings = {
            "DarkTheme" : True
        }
        return Settings

def setColorTheme(Settings):
        if Settings("DarkTheme"):
            backgoundColorDarkLv1 = (0.15, 0.15, 0.15, 1)
            backgoundColorDarkLv2 = (0.125, 0.125, 0.125, 1)
            backgoundColorDarkLv3 = (0.1, 0.1, 0.1, 1)
            menuButtonColor       = (0.15, 0.15, 0.15, 1)
            menuButtonColorHighlight = (0.17, 0.17, 0.17, 1)
            textColorDark         = (1, 1, 1, 1)
            lineColorDark         = (1, 1, 1, 1)
            colorPallete = [backgoundColorDarkLv1, backgoundColorDarkLv2, backgoundColorDarkLv3, menuButtonColor, menuButtonColorHighlight, textColorDark, lineColorDark]
        else:
            backgoundColorDarkLv1 = (0.9, 1, 0.9, 1)
            backgoundColorDarkLv2 = (0.125, 0.125, 0.125, 1)
            backgoundColorDarkLv3 = (0.1, 0.1, 0.1, 1)
            menuButtonColor       = (0.15, 0.15, 0.15, 1)
            menuButtonColorHighlight = (0.17, 0.17, 0.17, 1)
            textColorDark         = (0, 0, 0, 1)
            lineColorDark         = (0, 0, 0, 1)
            colorPallete = [backgoundColorDarkLv1, backgoundColorDarkLv2, backgoundColorDarkLv3, menuButtonColor, menuButtonColorHighlight, textColorDark, lineColorDark]