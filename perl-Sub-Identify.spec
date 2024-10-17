%define modname	Sub-Identify
%define modver 0.14
%ifarch %{x86_64}
# FIXME bug
%global _debugsource_template %{nil}
%endif

Summary:	Retrieve names of code references
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Sub::Identify
Source0:	http://www.cpan.org/modules/by-module/Sub/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
Sub::Identify allows you to retrieve the real name of code references. For
this, it uses perl's introspection mechanism, provided by the B module.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc Changes
%{perl_vendorarch}/Sub
%{perl_vendorarch}/auto/Sub
%{_mandir}/man3/*
