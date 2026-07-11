%global tl_name functan
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros for functional analysis and PDE theory
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/functan
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/functan.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/functan.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/functan.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a convenient and coherent way to deal with name of
functional spaces (mainly Sobolev spaces) in functional analysis and PDE
theory. It also provides a set of macros for dealing with norms, scalar
products and convergence with some object oriented flavor (it gives the
possibility to override the standard behavior of norms, ...).

