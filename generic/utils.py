import re

def parse_request(request, regex):

    mat = re.search(
            regex,
            request.META['PATH_INFO'],
            re.I | re.S | re.M
        )
    classname = mat.groups()[0]

    return classname