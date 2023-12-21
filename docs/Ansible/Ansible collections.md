
TODO:


README.md: What is this collection about
galaxy.yml: Contains metadata about your collection
docs/: local documentation for the collection
playbooks/: playbooks reside here not created but typical
playbooks/tasks/: this holds 'task list files' for include_tasks/import_tasks usage
plugins/: all ansible plugins and modules go here, each in its own subdir
(example) plugins/modules/: ansible modules
(example) plugins/lookups/: lookup plugins
(example) plugins/filters/: Jinja2 filter plugins
plugins/... rest of plugins
README.md: a description of the new functionality provided by the plugins
roles/: directory for ansible roles