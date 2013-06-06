%define upstream_name    KiokuDB
%define upstream_version 0.52
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.52
Release:	1

Summary:	Common functionality for JSPON
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/DOY/KiokuDB-0.52.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cache::Ref)
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(Data::Stream::Bulk)
BuildRequires:	perl(Data::UUID::LibUUID)
BuildRequires:	perl(Data::Visitor)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Hash::Util::FieldHash::Compat)
BuildRequires:	perl(IO)
BuildRequires:	perl(JSON)
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(Module::Pluggable::Object)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Clone)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(MooseX::YAML)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Search::GIN)
BuildRequires:	perl(Set::Object)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(Throwable)
BuildRequires:	perl(Tie::ToObject)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(YAML::XS)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
the KiokuDB manpage is a Moose based frontend to various data stores,
somewhere in between the Tangram manpage and the Pixie manpage.

Its purpose is to provide persistence for "regular" objects with as little
effort as possible, without sacrificing control over how persistence is
actually done, especially for harder to serialize objects.

the KiokuDB manpage is also non-invasive: it does not use ties, 'AUTOLOAD',
proxy objects, 'sv_magic' or any other type of trickery.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_bindir}/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.500.0-2mdv2011.0
+ Revision: 657123
- fix br
- rebuild for updated spec-helper

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.500.0-1mdv2011.0
+ Revision: 628783
- update to new version 0.50

* Sun Aug 01 2010 Shlomi Fish <shlomif@mandriva.org> 0.480.0-1mdv2011.0
+ Revision: 564859
- Updated to 0.48
- import perl-KiokuDB


* Wed Jul 14 2010 cpan2dist 0.46-1mdv
- initial mdv release, generated with cpan2dist

