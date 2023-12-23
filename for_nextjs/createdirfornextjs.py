import os 

x = input('Insira um nome para a pasta:')

#layout_tsx = open(x + "layout_1.html", "w")
#page_tsx = open(x + "layout_1.html", "w")

if os.path.exists(x): 
 print('a pasta '+ x +' já existe')

else:
   os.makedirs(x)
   layout_tsx = open(x + "/layout.tsx", "w")
   page_tsx = open(x + "/page.tsx", "w") 
   layout_tsx.close()
   page_tsx.close()
   print('pasta '+ x +' criada com sucesso')


 