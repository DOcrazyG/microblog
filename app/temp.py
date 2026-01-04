from langdetect import LangDetectException, detect

language = detect(
    "Die Unterschiede zwischen der Erkennung der Kodierung durch Baidu Übersetzung und langdetect bewältigen"
)
print(language)
