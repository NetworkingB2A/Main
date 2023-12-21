try:
    import json
except ImportError:
        import simplejson as json

from ansible.module_utils.basic import AnsibleModule
import time
import sys

def main():
    module = AnsibleModule(
        argument_spec= dict(msg=dict(required=True, type='str'))
    )
    msg = module.params['msg']
    
    # You can do one of the following
    # try:
    #     print(json.dumps({"msg": f"{time.strftime('%c')} - {msg}", "changed": True})
    #     sys.exit(0)
    # except:
    #     print(json.dumps({"failed": True, "msg": "failed debugging"}))
    # or
    try:
        module.exit_json(changed=True, msg=f"{time.strftime('%c')} - {msg}")
    except:
        module.exit_json(msg="error")
        

if __name__ == '__main__':
    main()