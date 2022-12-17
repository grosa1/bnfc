# https://fedoraproject.org/wiki/Packaging:Haskell

Name:           BNFC
Version:        2.9.5
Release:        1%{?dist}
Summary:        A compiler front-end generator

License:        BSD3
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  alex
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  happy
# End cabal-rpm deps

%description
The BNF Converter is a compiler construction tool generating a compiler
front-end from a Labelled BNF grammar. It was originally written to generate
Haskell, but starting from Version 2.0, it can also be used for generating
Java, C++, and C.

Given a Labelled BNF grammar the tool produces: an abstract syntax as a
Haskell/C++/C module or Java directory, a case skeleton for the abstract syntax
in the same language, an Alex, JLex, or Flex lexer generator file, a Happy,
CUP, or Bison parser generator file, a pretty-printer as a Haskell/Java/C++/C
module, a Latex file containing a readable specification of the language.


%prep
%setup -q


%build
%ghc_bin_build


%install
%ghc_bin_install


%files
%doc LICENSE
%doc TODO
%{_bindir}/bnfc


%changelog
* Fri Sep 13 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 2.5.0.0-1
- spec file generated by cabal-rpm-0.8.3
