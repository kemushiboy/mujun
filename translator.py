import OSC

from microsofttranslator import Translator
translator = Translator("twitter_interaction","un+j9nSC3U4tTQvEZmcrj6lDAAc5tIjDqQMDnjwUakI=")

#client = OSC.OSCClient()
text = translator.translate("cat","ja")
print text
