# Laboratorio de Reducción de Datos (F503)
Directorio remoto "origin" (git remote add origin git@github.com:MASilva139/LabRedDat.git).
* [git push -u origin main]

## Navegación

Los contenidos de este repositorio son los siguientes:

* [**Tareas:**](Tareas) Contiene las tareas realizadas durante el semestre.
* [**Data:**](Data) Contiene archivos `.csv` de datos que serán utilizados para ejercicios, tareas y prácticas.
* [**Proyectos:**](Proyectos) Contiene los proyectos realizados durante el semestre.
* [**Notas:**](Notas) Contiene las notas de clase.
* [**Repositorio de Clases (Oculto)**](RepC) Contiene el repositorio de clase compartido por el licenciado.

## Comandos de git
```
Comandos de terminal (bash)
├── git status
│   └── Lista un estado actual del repositorio con lista de archivos modificados o agregados.
├── git init
│   └── Iniciamos GIT en la carpeta donde esta el proyecto (local).
├── git clone <url>
│   └── Clonamos el repositorio de github o bitbucket.
├── git git add .
│   └── Añadimos todos los archivos para el commit.
├── git commit -m "Texto que identifique por que se hizo el commit"
│   └── Hace el commit de los archivos.
├── git chekout --<file>
│   └── Quita del HEAD un archivo y le pone el estado de no trabajado.
├── git checkout -b newlocalbranchname origin/branch-name
│   └── Crea un branch en base a uno online.
├── git pull origin <nameBranch>
│   └── Busca los cambios nuevos y actualiza el repositorio.
├── git checkout <nameBranch/tagname>
│   └── Cambiar de branch.
├── git merge <nameBranch>
│   └── Une el branch actual con el especificado.
├── git fetch
│   └── Verifica cambios en el repositorio online con el local.
├── git rm <archivo>
│   └── Borrar un archivo del repositorio.
├── git remote add origin <url>
│   └── Agregar repositorio remoto.
├── git remote set-url origin <url>
│   └── Cambiar de remote.
├── git remote rm <name/origin>
│   └── Remover repositorio.
├── git remote -v
│   └── Muestra lista repositorios.
├── git remote show origin
│   └── Muestra los branches remotos.
├── git remote prune origin
│   └── Limpiar todos los branches eliminados.
├── git branch <nameBranch>
│   └── Crea un branch.
├── git branch
│   └── Lista los branches.
├── git branch -d <nameBranch>
│   └── Comando -d elimina el branch y lo une al master/main.
├── git branch -D <nameBranch>
│   └── Elimina sin preguntar.
├── 
│   └── 
├── 
│   └── 
├── 
│   └── 
└── 
    └── 
```
## Creación de ambiente virtual con 'virtualenv'
"Buscando documentación"