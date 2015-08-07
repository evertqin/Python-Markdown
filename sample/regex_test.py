import re

test = re.compile(r'(?:\s*)*t', re.VERBOSE)
te = '   t'
ma = re.search(test, te)
print(ma.group(0))


FENCED_BLOCK_RE = re.compile(r'''
(?P<fence_begin>^(?:[\s\t]*~{3,}|`{3,}))[ ]*         # Opening ``` or ~~~
(\{?\.?(?P<lang>[a-zA-Z0-9_+-]*))?[ ]*  # Optional {, and lang
# Optional highlight lines, single- or double-quote-delimited
(hl_lines=(?P<quot>"|')(?P<hl_lines>.*?)(?P=quot))?[ ]*
}?[ ]*\n                                # Optional closing }
(?P<code>.*?)(?<=\n)
(?P<fence_end>^(?:[\s\t]*~{3,}|`{3,}))[ ]*
$''', re.MULTILINE | re.DOTALL | re.VERBOSE)

text = '''
 ~~~~{.cpp}
struct OneDimRetArray
{
	double* content;
	int size;
};

typedef struct OneDimRetArray OneDimRetArray_t;
      ~~~~
'''

m = re.search(FENCED_BLOCK_RE, text)
print(m.group(0))
