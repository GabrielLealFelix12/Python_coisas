
file_html = open("layout_1.html", "w")

file_html.write('''

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="utf-8"/> 
    <title> Layout </title>
</head>
<body>
<div style='display:flex; flex-direction: column; background-color: pink; max-width: 95%;'>
 navbar
</div>	
<div style='display: flex; min-height: 100vh; min-width: 100wh;'>
   
   <div style='display:flex; flex-direction: column; background-color: red; min-width: 25%; min-height: 90%;'>
    content
   </div>
   
   <div style='display:flex; flex-wrap: wrap; background-color: blue; min-width: 70%; min-height: 90%;'>
     content
   </div>	

</div>


<div style='
  left: 0;
  bottom: 0;
  max-width: 95%;
  background-color: brown;
  color: black;
  text-align: center;'>
footer
</div>	
</body>	
</html>

''')

file_html.close()