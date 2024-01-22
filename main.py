from Admin import AdminInfo
admin_instance = AdminInfo(name=['name'], email=['email'], password=['password'])
admin_instance.new_admin()
print(f"New admin created: {admin_instance}")