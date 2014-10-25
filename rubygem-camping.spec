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
%dir %{gem_dir}/gems/%{rbname}-%{version}/
%{gem_dir}/gems/%{rbname}-%{version}/bin/
%{gem_dir}/gems/%{rbname}-%{version}/lib/
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
Conflicts:	%{name} < 2.1.532

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{gem_dir}/doc/%{rbname}-%{version}
%{gem_dir}/gems/%{rbname}-%{version}/CHANGELOG
%{gem_dir}/gems/%{rbname}-%{version}/COPYING
%{gem_dir}/gems/%{rbname}-%{version}/README.md
%{gem_dir}/gems/%{rbname}-%{version}/book/

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install
