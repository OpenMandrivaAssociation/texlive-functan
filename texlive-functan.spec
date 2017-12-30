# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/functan
# catalog-date 2007-01-07 11:47:19 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-functan
Version:	20170414
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
%{_texmfdistdir}/tex/latex/functan/functan.sty
%doc %{_texmfdistdir}/doc/latex/functan/README
%doc %{_texmfdistdir}/doc/latex/functan/functan.pdf
#- source
%doc %{_texmfdistdir}/source/latex/functan/functan.drv
%doc %{_texmfdistdir}/source/latex/functan/functan.dtx
%doc %{_texmfdistdir}/source/latex/functan/functan.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070107-2
+ Revision: 752176
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070107-1
+ Revision: 718514
- texlive-functan
- texlive-functan
- texlive-functan
- texlive-functan

