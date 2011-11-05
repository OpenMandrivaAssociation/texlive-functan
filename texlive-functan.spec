# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/functan
# catalog-date 2007-01-07 11:47:19 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-functan
Version:	20070107
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides a convenient and coherent way to deal
with name of functional spaces (mainly Sobolev spaces) in
functional analysis and PDE theory. It also provides a set of
macros for dealing with norms, scalar products and convergence
with some object oriented flavor (it gives the possibility to
override the standard behavior of norms, ...).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
