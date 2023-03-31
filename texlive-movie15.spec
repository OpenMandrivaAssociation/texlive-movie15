Name:		texlive-movie15
Version:	26473
Release:	2
Summary:	Multimedia inclusion package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/movie15
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/movie15.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/movie15.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides an interface to embed movies, sounds and 3D objects
into PDF documents for use with LaTeX as well as pdfLaTeX.
Defines \includemovie with PDF-1.5 compatibility. Option
'autoplay' causes the media clip to be started right after the
page has loaded. This is useful for side by side movie clips to
be played back synchronously.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/movie15/movie15.sty
%doc %{_texmfdistdir}/doc/latex/movie15/README
%doc %{_texmfdistdir}/doc/latex/movie15/files/3dsystem.fig
%doc %{_texmfdistdir}/doc/latex/movie15/files/3dsystem.pdf
%doc %{_texmfdistdir}/doc/latex/movie15/files/3dsystem.tex
%doc %{_texmfdistdir}/doc/latex/movie15/files/dice.u3d
%doc %{_texmfdistdir}/doc/latex/movie15/files/dice.vws
%doc %{_texmfdistdir}/doc/latex/movie15/files/dice.wrl
%doc %{_texmfdistdir}/doc/latex/movie15/files/mailto.png
%doc %{_texmfdistdir}/doc/latex/movie15/files/random.mpg
%doc %{_texmfdistdir}/doc/latex/movie15/javascript/animation.js
%doc %{_texmfdistdir}/doc/latex/movie15/javascript/lights.js
%doc %{_texmfdistdir}/doc/latex/movie15/javascript/turntable.js
%doc %{_texmfdistdir}/doc/latex/movie15/movie15.pdf
%doc %{_texmfdistdir}/doc/latex/movie15/movie15.tex
%doc %{_texmfdistdir}/doc/latex/movie15/overlay-example.pdf
%doc %{_texmfdistdir}/doc/latex/movie15/overlay-example.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
