# revision 34088
# category Package
# catalog-ctan /systems/enctex
# catalog-date 2014-05-09 09:19:54 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-enctex
Version:	20140509
Release:	3
Summary:	A TeX extension that translates input on its way into TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/enctex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enctex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enctex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
EncTeX is (another) tex extension, written at the change-file
level. It provides means of translating input on the way into
TeX. It allows, for example, translation of multibyte
sequences, such as utf-8 encoding.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/enctex/1250-csf.tex
%{_texmfdistdir}/tex/generic/enctex/1250-il2.tex
%{_texmfdistdir}/tex/generic/enctex/1250-latex.tex
%{_texmfdistdir}/tex/generic/enctex/1250-t1.tex
%{_texmfdistdir}/tex/generic/enctex/852-csf.tex
%{_texmfdistdir}/tex/generic/enctex/852-il2.tex
%{_texmfdistdir}/tex/generic/enctex/852-latex.tex
%{_texmfdistdir}/tex/generic/enctex/852-t1.tex
%{_texmfdistdir}/tex/generic/enctex/csfmacro.tex
%{_texmfdistdir}/tex/generic/enctex/enc-u.tex
%{_texmfdistdir}/tex/generic/enctex/encmacro.tex
%{_texmfdistdir}/tex/generic/enctex/il2-1250.tex
%{_texmfdistdir}/tex/generic/enctex/il2-852.tex
%{_texmfdistdir}/tex/generic/enctex/il2-csf.tex
%{_texmfdistdir}/tex/generic/enctex/il2-kam.tex
%{_texmfdistdir}/tex/generic/enctex/il2-t1.tex
%{_texmfdistdir}/tex/generic/enctex/kam-csf.tex
%{_texmfdistdir}/tex/generic/enctex/kam-il2.tex
%{_texmfdistdir}/tex/generic/enctex/kam-latex.tex
%{_texmfdistdir}/tex/generic/enctex/kam-t1.tex
%{_texmfdistdir}/tex/generic/enctex/mixcodes.tex
%{_texmfdistdir}/tex/generic/enctex/noprefnt.tex
%{_texmfdistdir}/tex/generic/enctex/plain-1250-cs.tex
%{_texmfdistdir}/tex/generic/enctex/plain-852-cs.tex
%{_texmfdistdir}/tex/generic/enctex/plain-il2-cs.tex
%{_texmfdistdir}/tex/generic/enctex/plain-kam-cs.tex
%{_texmfdistdir}/tex/generic/enctex/plain-utf8-cs.tex
%{_texmfdistdir}/tex/generic/enctex/plain-utf8-ec.tex
%{_texmfdistdir}/tex/generic/enctex/polyset.tex
%{_texmfdistdir}/tex/generic/enctex/t1macro.tex
%{_texmfdistdir}/tex/generic/enctex/utf8-csf.tex
%{_texmfdistdir}/tex/generic/enctex/utf8-t1.tex
%{_texmfdistdir}/tex/generic/enctex/utf8cseq.tex
%{_texmfdistdir}/tex/generic/enctex/utf8lat1.tex
%{_texmfdistdir}/tex/generic/enctex/utf8lata.tex
%{_texmfdistdir}/tex/generic/enctex/utf8math.tex
%{_texmfdistdir}/tex/generic/enctex/utf8off.tex
%{_texmfdistdir}/tex/generic/enctex/utf8raw.tex
%{_texmfdistdir}/tex/generic/enctex/utf8unkn.tex
%{_texmfdistdir}/tex/generic/enctex/utf8warn.tex
%doc %{_texmfdistdir}/doc/generic/enctex/COPYING
%doc %{_texmfdistdir}/doc/generic/enctex/COPYING.UCD
%doc %{_texmfdistdir}/doc/generic/enctex/INSTALL
%doc %{_texmfdistdir}/doc/generic/enctex/INSTALL.eng
%doc %{_texmfdistdir}/doc/generic/enctex/README
%doc %{_texmfdistdir}/doc/generic/enctex/changes.txt
%doc %{_texmfdistdir}/doc/generic/enctex/encdoc-e.pdf
%doc %{_texmfdistdir}/doc/generic/enctex/encdoc-e.tex
%doc %{_texmfdistdir}/doc/generic/enctex/encdoc.pdf
%doc %{_texmfdistdir}/doc/generic/enctex/encdoc.tex
%doc %{_texmfdistdir}/doc/generic/enctex/math-example.tex
%doc %{_texmfdistdir}/doc/generic/enctex/unimap.diff
%doc %{_texmfdistdir}/doc/generic/enctex/unimap.py
%doc %{_texmfdistdir}/doc/generic/enctex/vlna.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
