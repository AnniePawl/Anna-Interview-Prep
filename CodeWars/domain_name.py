# Given a URL as a string, parse out just domain name and return it as string 

def domain_name(domain):
  position1 = domain.find(".")
  partial_domain = domain[position1 + 1:]
  return partial_domain[:partial_domain.find(".")]


print(domain_name('http://www.github.com')) #  github
print(domain_name("http://www.zombie-bites.com")) #  zombie-bites
print(domain_name("https://www.cnet.com")) #  cnet
