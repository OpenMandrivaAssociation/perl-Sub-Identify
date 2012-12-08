%define upstream_name	 Sub-Identify
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 5

Summary:	Retrieve names of code references
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Sub::Identify allows you to retrieve the real name of code references. For
this, it uses perl's introspection mechanism, provided by the B module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorarch}/Sub
%{perl_vendorarch}/auto/Sub
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-5mdv2012.0
+ Revision: 765662
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-4
+ Revision: 764173
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-3
+ Revision: 667315
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 556150
- rebuild for perl 5.12

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 401607
- rebuild using %%perl_convert_version
- fixed license field

* Wed Dec 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
+ Revision: 315123
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2009.0
+ Revision: 268728
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
+ Revision: 209332
- update to new version 0.03

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.02-3mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.02-3mdv2008.0
+ Revision: 23889
- rebuild


* Fri May 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.02-1mdk
- Initial Mandriva release.

