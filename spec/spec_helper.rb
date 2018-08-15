RSpec.configure do |config|

  config.example_status_persistence_file_path = "spec/examples.txt"
  config.expect_with :rspec do |expectations|
    expectations.syntax = :expect
  end

  config.disable_monkey_patching!

  config.mock_with :rspec do |mocks|
    mocks.syntax = :expect
    mocks.verify_partial_doubles = true
  end

  config.order = :random
  require_relative '../config/boot'
end
