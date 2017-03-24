# coding: utf-8
lib = File.expand_path("../lib", __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require "zcred/version"

Gem::Specification.new do |spec|
  spec.name          = "zcred"
  spec.version       = Zcred::VERSION
  spec.authors       = ["Tony Arcieri"]
  spec.email         = ["bascule@gmail.com"]
  spec.authors       = ["Tony Arcieri"]
  spec.email         = ["bascule@gmail.com"]
  spec.licenses      = ["MIT"]
  spec.homepage      = "https://github.com/zcred/zcred/tree/master/ruby/"
  spec.summary       = "A modern authoriZation-centric credential format"
  spec.description   = "Flexible modern credential format built on advanced cryptography"
  spec.files         = `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
  spec.bindir        = "exe"
  spec.executables   = spec.files.grep(%r{^exe/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  spec.required_ruby_version = ">= 2.2.2"

  spec.add_development_dependency "bundler", "~> 1.14"
end
