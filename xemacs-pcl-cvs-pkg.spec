Summary:	CVS frontend
Summary(pl):	CVS frontend
Name:		xemacs-pcl-cvs-pkg
%define 	srcname	pcl-cvs
Version:	1.41
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		xemacs-pcl-cvs-pkg-info.patch
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
Requires:	xemacs-elib-pkg
Requires:	xemacs-dired-pkg
Prereq:		/usr/sbin/fix-info-dir
BuildRoot:	/tmp/%{name}-%{version}-root

%description


%description -l pl 


%prep
%setup -q -c
%patch0 -p1

%build
(cd man/pcl-cvs; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info* \
	lisp/pcl-cvs/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%post
%{_sbindir}/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
%{_sbindir}/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/pcl-cvs/ChangeLog.gz
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
