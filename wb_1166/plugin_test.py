from compiler import *
register_plugin()
require_plugin('plugin_test2')

export_plugin_globals(
    test_global = 16,
)

injection = {
    'test_injection': [
        (1, 2, 3),
        (4, 5, 6),
    ]
}

def test_operation(destination, operand1, operand2):
    return [
        (store_add, destination, operand1, operand2),
    ]

extend_syntax(test_operation)

def preprocess_entities(glob):
    pass
