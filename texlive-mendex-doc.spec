%global tl_name mendex-doc
%global tl_revision 77843

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Documentation for Mendex index processor
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/mendex-doc
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mendex-doc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mendex-doc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mendex-doc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides documentation for Mendex (Japanese index
processor). The source code of the program is not included, it can be
obtained from TeX Live subversion repository.

