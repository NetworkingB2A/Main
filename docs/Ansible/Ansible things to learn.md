Playbooks
inventory
- dynamic
- static
Ansible runner
Ansible execution environment
- execution-environment.yml
```yaml
version: 3
dependencies:
  ansible_core:
    package_pip: ansible-core==2.14.4
  ansible_runner:
    package_pip: ansible-runner
  galaxy: requirements.yml
  python: requirements.txt

images:
  base_image:
    name: quay.io/ansible/awx-ee:latest

```
- requirements.txt

```yaml


```
- requirements.yml
modules
plugins
roles
collections
ansible builder


Awx
- webhooks
