%define		_proj_name	nagios-plugins-snmp
Summary:	SNMP checks for nagios
Summary(pl.UTF-8):	Wtyczki nagiosa do odpytywania po SNMP
Name:		nagios-plugins-snmp2
Version:	0.6.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://nagios.manubulon.com/%{_proj_name}-%{version}.tgz
# Source0-md5:	ced0e717220a6ae88099bb4a39645615
Source1:	http://nagios.manubulon.com/nagios-snmp-plugins.1.1.1.tgz
# Source1-md5:	f8aa57ec9224634390919885d16a5b6f
URL:		http://nagios.manubulon.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins

%description
SNMP checks for nagios

%description -l pl.UTF-8
Wtyczki nagiosa do odpytywania po SNMP

%prep
%setup -q -n %{_proj_name}
install -d perl
tar xzf %{SOURCE1} -C perl
mv perl/nagios_plugins/Change{log,Log.perl}
sed -i -e 's,/usr/local/nagios/libexec,%{_plugindir},' perl/nagios_plugins/check_snmp_*.pl

%build
%configure \
	--libexecdir=%{_plugindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install perl/nagios_plugins/check_snmp_*.pl $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README perl/nagios_plugins/ChangeLog.perl perl/nagios_plugins/doc/*
%attr(755,root,root) %{_plugindir}
