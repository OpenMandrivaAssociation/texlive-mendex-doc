Name:		texlive-mendex-doc
Version:	62914
Release:	2
Summary:	Documentation for Mendex index processor
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mendex-doc
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mendex-doc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mendex-doc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mendex-doc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides documentation for Mendex (Japanese index
processor). The source code of the program is not included, it
can be obtained from TeX Live subversion repository.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mendex-doc
%{_texmfdistdir}/makeindex/mendex-doc
%doc %{_texmfdistdir}/doc/support/mendex-doc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
