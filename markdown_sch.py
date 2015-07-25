import re

from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor

class SchExtension(Extension):
    def extendMarkdown(self, md, mg_globals):
        md.postprocessors.add("sch", SchPostprocessor(md), ">raw_html")

class SchPostprocessor(Postprocessor):
    def run(self, html):
        return re.sub(re.compile(r"!(\d+(.\d+)?);(\d+(.\d+)?);(\d+(.?\d+)?);(\d+(.\d+)?);!\(([\w./\\]+)\)"), self._handle, html)

    def _handle(self, match):
        return "<div style=\"width: {2}mm; height: {3}mm; background: url({4}); background-position: -{0}mm -{1}mm;\"><img style=\"opacity: 0.0; width: {2}mm; height: {3}mm;\" src=\"{4}\"></div>".format(float(match.group(1)),
         float(match.group(3)),
         float(match.group(5)) - float(match.group(1)), 
         float(match.group(7)) - float(match.group(3)),
         match.group(9))
