%global tl_name enctex
%global tl_revision 34957

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A TeX extension that translates input on its way into TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/enctex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enctex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enctex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
EncTeX is (another) TeX extension, written at the change-file level. It
provides means of translating input on the way into TeX. It allows, for
example, translation of multibyte sequences, such as utf-8 encoding.

