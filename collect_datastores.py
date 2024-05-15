from pyVmomi import vim
from pyVim.connect import SmartConnect


host: str = ""
port: int = 443
username: str = ""
password: str = ""

try:
    service_instance: vim.ServiceInstance = SmartConnect(host=host, user=username, pwd=password, port=port, disableSslCertValidation=True)
except Exception as e:
    print(f"Error connecting to {host}: {e}")

content = service_instance.RetrieveContent()
container = content.rootFolder
view_type = [vim.Datastore]
recursive = True
container_view = content.viewManager.CreateContainerView(
    container,
    view_type,
    recursive
)
datastores = container_view.view
for datastore in datastores:
    print("Summary:\n---")
    print(datastore.summary)
    print("Info:\n---")
    print(datastore.info)
    print("Host mounts:\n---")
    print(datastore.host)
    print("--------------------\n")