fa = []
with open('input.css') as f:
    for line in f:
        read_data = []
        read_data.append(line)
        for line in read_data:
            if line.startswith('.fa-') and 'before' in line:
                fa.append(line[line.find('-')+1:line.find(':')])

my_file = ['<ul>', ]
for elem in fa:
    my_file.append(
        f'<li class="nav-item"> <a class="nav-link" style="color: black;" href="/"><i class="fas fa{elem}"></i>&nbsp; {elem}</i></a></li>')
my_file.append('</ul>')

with open('output.html', 'a') as f2:
    f2.write('''<!DOCTYPE html>

<html lang="en">

<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

</head>

<body>''')
    for line in my_file:
        f2.write(line+'\n')
    f2.write('''
</body>

</html>
    ''')
