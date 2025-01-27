import wolframalpha as wf #wolfram API
import os


def  wolframBasedSearches(query_question):
    client = wf.Client("4WJLW2-R9K8T6V8UW")
    from analyzeWolframBasedSearches import analyzeWolframBasedSearches
    analyzeWolframBasedSearches(query_question)
    try:
        res = client.query(query_question)
        result = next(res.results).text
        from analyzeWolframBasedSearches import analyzeWolframBasedSearches
        analyzeWolframBasedSearches(query_question)
        from displayWolframResult import displayWolframResult
        displayWolframResult(query_question, result)
    except:
        from errorDuringWolframAlphaSearch import errorDuringWolframAlphaSearch
        errorDuringWolframAlphaSearch()
