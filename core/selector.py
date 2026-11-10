# BP-X2 मॉडल चयनकर्ता
# तीन मोड: coder, general, mixed

CODE_WORDS = [
    "code", "कोड", "function", "फ़ंक्शन", "फंक्शन", "python", "c#", "bug",
    "error", "एरर", "त्रुटि", "program", "प्रोग्राम", "script", "class",
    "debug", "सुधार", "लिखो", "api बनाओ", "sql", "html", "javascript",
]


def choose_model(question):
    """सवाल देखकर तय करता है कि कौन-सा मॉडल चलेगा।"""
    q = question.lower()
    for word in CODE_WORDS:
        if word in q:
            return "coder"
    return "general"
