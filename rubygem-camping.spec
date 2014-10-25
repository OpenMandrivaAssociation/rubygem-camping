%define rbname camping

Summary:	Minature rails for stay-at-home moms
Name:		rubygem-%{rbname}
Version:	2.1.532
Release:	1
License:	MIT
Group:		Development/Ruby
Url:		https://rubygems.org/gems/%{rbname}
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
Minature rails for stay-at-home moms.

%files
%{_bindir}/camping
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
Conflicts:	%{name} < 2.1.532

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGELOG
%{ruby_gemdir}/gems/%{rbname}-%{version}/COPYING
%{ruby_gemdir}/gems/%{rbname}-%{version}/README.md
%{ruby_gemdir}/gems/%{rbname}-%{version}/book/

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install
