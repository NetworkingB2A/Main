creating custom modules.

in order to create a custom module, you need to create a custom python script.
BEST PRACTICE is to create documentation as well and examples. so you can use the `ansible-doc {module-name}` command. This documentation file is created under a modules_utils directory where as the code itself would be stored under the modules directory. one example /usr/lib/python3/dist-packages/ansible/modules/ and /usr/lib/python3/dist-packages/ansible/modules_utils/