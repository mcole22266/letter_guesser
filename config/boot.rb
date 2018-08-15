require 'rubygems'
require 'bundler/setup'
Bundler.require

Dir.glob("#{File.expand_path('../../lib', __FILE__)}/*.rb") {|f| require f}
