added_files = [
         ( 'C:\Users\dimitri.sautron\Projet\brain-learning\', '.' ),
         ( 'C:\Users\dimitri.sautron\Projet\brain-learning\Fonction.py', 'fct' )
         ]
options = [ ('v', None, 'OPTION'), ('W ignore', None, 'OPTION') ]
a = Analysis(...
         pathex=['C:\Users\dimitri.sautron\Projet\brain-learning\'],
         datas = added_files,
         binaries=None,
         excludes=None,
         cipher=block_cipher
         )
exe = EXE(pyz,
      a.scripts,
      options,   <--- added line
      exclude_binaries=...
      )
