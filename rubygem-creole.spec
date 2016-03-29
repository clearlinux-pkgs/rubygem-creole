#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-creole
Version  : 0.5.0
Release  : 4
URL      : https://rubygems.org/downloads/creole-0.5.0.gem
Source0  : https://rubygems.org/downloads/creole-0.5.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Ruby
BuildRequires : ruby
BuildRequires : rubygem-bacon
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
= Creole
Creole is a Creole-to-HTML converter for Creole, the lightweight markup
language (http://wikicreole.org/). Github uses this converter to render *.creole files.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n creole-0.5.0
gem spec %{SOURCE0} -l --ruby > rubygem-creole.gemspec

%build
gem build rubygem-creole.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
creole-0.5.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/creole-0.5.0 && rake --trace test TESTOPTS="-v" && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/creole-0.5.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/CHANGES
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/README.creole
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/creole.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/lib/creole.rb
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/lib/creole/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/lib/creole/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/creole-0.5.0/test/parser_test.rb
/usr/lib64/ruby/gems/2.3.0/specifications/creole-0.5.0.gemspec
