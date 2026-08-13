#!/usr/bin/env bash

perl -pi -e s"/lstlisting\}\[firstnumber=1,\]/minted\}\[breaklines=true,frame=single\]\{text\}/g;" pdf/c.tex
perl -pi -e s"/end\{lstlisting\}/end\{minted\}/g;" pdf/c.tex
perl -pi -e s"/lstlisting\}\[language=c\,firstnumber=1\,\]/minted\}\[breaklines=true,frame=single\]\{c\}/g;" pdf/c.tex
perl -pi -e s"/lstlisting\}\[language=cobjdump\,firstnumber=1\,\]/minted\}\[breaklines=true,frame=single\]\{gas\}/g;" pdf/c.tex
perl -pi -e s"/\\\begin{document}/\\\lstset{fancyvrb=false}\n\\\usepackage{minted}\n\\\begin{document}/g;" pdf/c.tex
perl -pi -e s"/\\\begin{lstlisting}\[firstnumber=1,escapeinside={<:}{:>}\]/\\\begin{minted}\[breaklines=true,frame=single\]{text}/g;" pdf/c.tex


TEX_FILE="pdf/c.tex"

# Execute all replacements in a single file-pass
perl -pi -e '
  s|lstlisting\}\[language=c\,firstnumber=1\,\]|minted\}[breaklines=true,frame=single]{c}|g;
  s|lstlisting\}\[language=cobjdump\,firstnumber=1\,\]|minted\}[breaklines=true,frame=single]{gas}|g;
  s|lstlisting\}\[firstnumber=1,\]|minted\}[breaklines=true,frame=single]{text}|g;
  s|\\begin\{lstlisting\}\[firstnumber=1,escapeinside=\{<:\}\{:>\}\]|\\begin{minted}[breaklines=true,frame=single]{text}|g;
  s|end\{lstlisting\}|end{minted}|g;
  s|\\begin\{document\}|\\lstset{fancyvrb=false}\n\\usepackage{minted}\n\\begin{document}|g;
' "$TEX_FILE"

xdotool search --onlyvisible --class "firefox" windowfocus key --window %@ F5
