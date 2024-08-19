import dns.resolver

resolver = dns.resolver.Resolver()

try:
    resultados = resolver.resolve("cancaonova.com.br", "A")
    for resultados in resultados:
            print(resultados)
except:
    print(" Subdominio não existe !! ")