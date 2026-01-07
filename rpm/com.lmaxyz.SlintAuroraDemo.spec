%define __requires_exclude ^lib.*$
%define __provides_exclude_from ^%{_datadir}/%{name}/lib/.*$

Name:       com.lmaxyz.SlintAuroraDemo
Summary:    Slint Demo
Version:    0.1.0
Release:    1
License:    Apache-2.0
URL:        https://github.com/lmaxyz

%description
%{summary}

%prep

%build

%install
install -Dm 755 %{name} -t %{buildroot}%{_bindir}

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{_sourcedir}/%{name}.desktop

install -Dm 644 %{_sourcedir}/icons/86x86/%{name}.png -t %{buildroot}%{_datadir}/icons/hicolor/86x86/apps
install -Dm 644 %{_sourcedir}/icons/108x108/%{name}.png -t %{buildroot}%{_datadir}/icons/hicolor/108x108/apps
install -Dm 644 %{_sourcedir}/icons/128x128/%{name}.png -t %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -Dm 644 %{_sourcedir}/icons/172x172/%{name}.png -t %{buildroot}%{_datadir}/icons/hicolor/172x172/apps

install -Dm 644 %{_sourcedir}/lib/* -t %{buildroot}%{_datadir}/%{name}/lib/

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%defattr(644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
