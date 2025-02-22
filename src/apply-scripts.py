import tomllib

# community
from jinja2 import Environment, PackageLoader, FileSystemLoader, select_autoescape

def applyTemplate(env, vars, TemplateFname, OutFname):
  template = env.get_template(TemplateFname)

  with open(OutFname,'w') as outfile:
    outfile.write(template.render(vars))


with open('pyproject.toml','rb') as infile:
  pyproject = tomllib.load(infile)
  vars = {
    'PackageName': pyproject["project"]["name"],
    'PackageVersion': pyproject["project"]["version"]
  }
  print (f'package name: {vars["PackageName"]}')

  env = Environment(
      loader=FileSystemLoader("conf/templates"),
      autoescape=select_autoescape()
  )

  applyTemplate(env, vars, 'install.tmpl', 'bin/install')
  applyTemplate(env, vars, 'install-venv.tmpl', 'bin/install-venv')
