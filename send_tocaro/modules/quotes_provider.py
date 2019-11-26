from modules.quote_provider_by_file import QuoteProviderByFile


class QuoteProvider(QuoteProviderByFile):
    def __init__(self):
        super(QuoteProvider, self).__init__("./HarukasQuotes.txt")

    def get_quote(self):
        return super().get_quote()
