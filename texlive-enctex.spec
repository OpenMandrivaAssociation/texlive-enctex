Name:		texlive-enctex
Version:	34957
Release:	2
Summary:	A TeX extension that translates input on its way into TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/enctex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enctex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enctex.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/enctex
%doc %{_texmfdistdir}/doc/generic/enctex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
