Name:		texlive-functan
Version:	20190228
Release:	1
Summary:	Macros for functional analysis and PDE theory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/functan
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/functan.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/functan.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/functan.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a convenient and coherent way to deal
with name of functional spaces (mainly Sobolev spaces) in
functional analysis and PDE theory. It also provides a set of
macros for dealing with norms, scalar products and convergence
with some object oriented flavor (it gives the possibility to
override the standard behavior of norms, ...).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/functan
%doc %{_texmfdistdir}/doc/latex/functan
#- source
%doc %{_texmfdistdir}/source/latex/functan

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
