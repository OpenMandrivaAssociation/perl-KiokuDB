%define upstream_name    KiokuDB
%define upstream_version 0.57

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Common functionality for JSPON
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/DOY/KiokuDB-%{upstream_version}.tar.gz

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
BuildRequires:	perl(Data::UUID)
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
%{_mandir}/man?/*
%{perl_vendorlib}/*
