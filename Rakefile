#!/usr/bin/rake -T

# For playing nice with mock
File.umask(027)

begin
  require 'simp/rake/pkg'
rescue LoadError
  Dir.glob("#{File.dirname(__FILE__)}/../../../rubygems/*/lib") do |dir|
    $LOAD_PATH.unshift(dir)
  end

  require 'simp/rake/pkg'
end

begin
  require 'puppetlabs_spec_helper/rake_tasks'
rescue LoadError
  puts "== WARNING: Gem puppetlabs_spec_helper not found, spec tests cannot be run! =="
end

# Lint Material
begin
  require 'puppet-lint/tasks/puppet-lint'

  PuppetLint.configuration.send("disable_80chars")
  PuppetLint.configuration.send("disable_variables_not_enclosed")
  PuppetLint.configuration.send("disable_class_parameter_defaults")
rescue LoadError
  puts "== WARNING: Gem puppet-lint not found, lint tests cannot be run! =="
end

Simp::Rake::Pkg.new( File.dirname( __FILE__ ) ) do | t |
  t.clean_list << "#{t.base_dir}/spec/fixtures/hieradata/hiera.yaml"
end
