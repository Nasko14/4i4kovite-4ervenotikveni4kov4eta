from jinja2 import Environment, FileSystemLoader

content = 'This is home page'

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('homePage.html')

output = template.render(content=content)
print(output)