from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("results"))
template = env.get_template("dhcpd.conf")

# user_list = {"user1":"abc","user2":"cba"}
# for key,value in user_list.items():
#     content = template.render(name=key,password=value)
#     print(content) 


content = template.render(start_addr="172.168.1.100",end_addr="172.168.1.110")
print(content)